############################
# BMSL: HTTP requests module
############################

# packages
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode

# make HTTP GET request
def get(url, payload, headers):
    # parse payload
    payload = urlencode(payload)
    
    # generate URL
    url = url + '?' + payload
    
    # try to make HTTP GET request
    try:
        # create request object
        request = Request(url=url, headers=headers, method='GET')
        
        # create response object
        response = urlopen(request)
    
        # return HTML content
        return response.read().decode('utf-8')
    
    except Exception as e:
        print('(BMSL) Request ERROR:', e)
        
        # return empty content
        return 'No content available!'

# make HTTP POST request
def post(url, payload, headers):
    # parse payload
    payload = urlencode(payload)
    
    # try to make HTTP GET request
    try:
        # create request object
        request = Request(url=url, data=payload.encode(), headers=headers, method='POST')
        
        # create response object
        response = urlopen(request)
    
        # return HTML content
        return response.read().decode('utf-8')
    
    except Exception as e:
        print('(BMSL) Request ERROR:', e)
        
        # return empty content
        return 'No content available!'















