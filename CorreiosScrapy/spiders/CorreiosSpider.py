# -*- coding: utf-8 -*-
import scrapy
import json

class CorreiosSpider(scrapy.Spider):
    name = "CorreiosSpider"
    ufs = []
    ufs_pages = {}
    uf_url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
    start_url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    
    def start_requests(self):    
        yield scrapy.Request(url=self.start_url, callback=self.parse_ufs)       

    def parse_ufs(self, response):        
        self.ufs = response.css('select[name="UF"] option::attr(value)').extract()
        
        for uf in self.ufs:
            if uf: 
                data = {'UF' : uf,
                        'qtdrow' : '100',
                        'pagini' : '1',
                        'pagfim' : '101',
                }        
                yield scrapy.FormRequest(url=self.uf_url, formdata=data, callback=self.parse_uf_details)       
        
                   
    def parse_uf_details(self, response):
        uf = response.xpath('//*[contains(@class, "tmptabela")][1]//tr[2]//td[1]/text()').extract_first()
        if uf:
            file_name = '../result_data/' + uf + '.jsonl'
            with open(file_name, 'w') as file:
                for row in response.xpath('//*[contains(@class, "tmptabela")][2]//tr'):
                    
                    data = {'Localidade' : row.xpath('td[1]/text()').extract_first(),
                            'Faixa de CEP': row.xpath('td[2]/text()').extract_first(),
                    }
                    
                    if data['Localidade'] and data['Faixa de CEP']:
                        json.dump(data, file, sort_keys=True, ensure_ascii=False)
                        file.write("\n")