#############################
#  BMSL: HTML parser module
#############################

# packages
from html.parser import HTMLParser

# HTML parser class
class BMSLParser(HTMLParser):
    # search query
    query = []
    
    # search result match
    match = {}
    
    # results list
    results = []
    
    # handle opening tag
    def handle_starttag(self, tag, attr):
        self.match['name'] = tag
        self.match['attr'] = attr
    
    # handle data within a tag
    def handle_data(self, data):
        # init query tag
        tag = self.query[0]
        
        # init attr query
        attr = self.query[1]
        
        # init query output
        text = self.query[-1]
        
        try:
            # found tag name
            if self.match['name'] == tag:
                # attributes are not specified in query
                if not len(attr):
                    # on tag text node query
                    if text == 'text':
                        self.results.append(data)
                    
                    # on tag attrbute data query
                    else:
                        # loop over attributes list
                        for item in self.match['attr']:
                            # init attr key and value
                            key = item[0]
                            val = item[1]
                            
                            # query output is within attr's key
                            if text == key:
                                self.results.append(val)
            
                # attributes are specified in query
                else:
                    # loop over attributes list
                    for item in self.match['attr']:
                        # init available attr key and value
                        key = item[0]
                        val = item[1]
                        
                        # init query attr key and value
                        q_key = attr[0]
                        q_val = attr[1]
    
                        # match key and value pairs
                        if q_key == key and q_val == val:
                            # on tag text node query
                            if text == 'text':
                                self.results.append(data)
                            
                            # on tag attrbute data query
                            else:
                                # loop over attributes list
                                for item in self.match['attr']:
                                    # init attr key and value
                                    key = item[0]
                                    val = item[1]
                                    
                                    # query output is within attr's key
                                    if text == key:
                                        self.results.append(val)
        
        except:
            pass
    
    # handle closing tag
    def handle_endtag(self, tag):
        # reset result match after matching closing tag
        self.match = {}

# parse content
def find(content, query):
    # create parser instance
    parser = BMSLParser()
    
    # reset previous results
    parser.results = []
    
    # init query
    parser.query = query
    
    # find matching results
    parser.feed(content)

    # close parser
    parser.close()
    
    # return results
    return parser.results
    
    
    
    
    
    
    
    
    
    
