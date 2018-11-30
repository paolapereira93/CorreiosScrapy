# CorreiosScrapy

## Environment

- Anaconda is used to manage environment (version with Python 3.7 https://www.anaconda.com/download/#linux)
- Once installed Anaconda, run on terminal:
```
export PATH="/[anaconda_path]/anaconda3/bin:$PATH"
conda create --name ScrapyEnvironment python=3.7.1 scrapy
source activate ScrapyEnvironment
```

## To run

- Clone this repository
- Go to /CorreiosScrapy/spiders and run:
```
scrapy crawl CorreiosSpider
```

## Results

- To see the collected data do to: /CorreiosScrapy/result_data/
