# BMSL
Bare minimum web scraping library

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

# packages
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
