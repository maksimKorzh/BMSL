# NEW VERSION
https://github.com/maksimKorzh/tiny_scraper

# BMSL
Bare minimum web scraping library

# Disclaimer
Please don't take it too serious - it's made more like for educational purposes rather than for production

# How to use
```python
########################################
#
# Test script showing how to use BMSL
#
#                 by
#
# scraping http://quotes.toscrape.com/
#
########################################

# import packages assuming "BMSL" folder containing files "request.py" and "parser.py"
# is located in current working directory along with this file "quotes.py".
# Please see /src/BMSL/test folder for the example project layout

from BMSL import request
from BMSL import parser
import csv

# make HTTP GET request
html = request.get(url='http://quotes.toscrape.com/', payload={}, headers={})

# data extraction logic
quotes = parser.find(content=html, query=['span', ('class', 'text'), 'text'])
authors = parser.find(content=html, query=['small', ('class', 'author'), 'text'])
about = []

# extract all links
about_text = parser.find(content=html, query=['a', (), 'text'])
about_href = parser.find(content=html, query=['a', (), 'href'])

# extract "about" links
for index in range(0, len(about_href)):
    if about_text[index] == '(about)':
        about.append(about_href[index])

# loop over all items
for index in range(0, len(quotes)):
    # write output to CSV file
    with open('quotes.csv', 'a') as f:
        # create CSV writer
        writer = csv.writer(f)
        
        # write line
        writer.writerow([quotes[index], authors[index], about[index]])
```

# Implementing "request.py"
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/fcnxo3iCaa0/0.jpg)](https://www.youtube.com/watch?v=fcnxo3iCaa0)

# Implementing "parser.py"
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/PwjP0berJR0/0.jpg)](https://youtu.be/PwjP0berJR0)

