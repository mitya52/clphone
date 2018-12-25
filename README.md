Simple scrapy usage example: collect and visualize current prices of phones from citilink.ru

1) parse data from site:
crapy crawl spoody -t csv -o phones.csv

2) visualize collected data:
python parse-and-visualize.py phones.csv
