
"""
    Component Implemented for STEP-2 
    This class/component helps in extracting the GET Parameters from a web url
    returns the web url with payloads inserted in it
"""

# Local import
import HarmlessTestString


#  EXAMPLE URL: www.abc.com/index.php?value="new"

class url_contains_params:
    payload = HarmlessTestString.harmless_test_string
    getparam_key_value_pairs = {}

    def start(self, url):
        params = {}
        get_params = []

        url = str(url)          # applying str function for dealing with any non-ascii chararcters in url
        part = url.split('?')   # splitting upon the url params i.e. abc.com/index.php?value="new" => value="new"
        key_value_pairs = part[1].split('&')  # for multiple params i.e. value="new"&name="author"
        if len(key_value_pairs) > 1:
            for pair in key_value_pairs:
                p = pair.split('=')     # splitting the key-value pair => p[0]=value, p[1]="new"
                if len(p) == 2:
                    if p[1]:    
                        params[p[0]] = p[1] # putting key-value pairs in a dictionary
                    else:   
                        params[p[0]] = ''
                else:   
                    params[p[0]] = ''
        else:   
            p = key_value_pairs[0].split('=')
            if len(p) == 2:
                if p[1]:    
                    params[p[0]] = p[1]
                else:   
                    params[p[0]] = ''
            else:   
                params[p[0]] = ''

        self.getparam_key_value_pairs = params.copy()
        # Copying all parameter pairs into get_param array
        for p in params: 
            get_params.append(p)
        print('\nparams = ', get_params, '\n')

        # links are equal to number of distint key-value pairs 
        # part[0] is the url part before ? i.e. => www.abc.com/index.php
        # "add_payload" function adds payload to each distinct link and returns an array of links
        links = self.add_payload(part[0], params)       

        return  get_params, links

    def add_payload(self, part, params):
        links = []
        for p in params:
            params[p] = self.payload
            link = self.make_links(part, params)
            links.append(link)
            params = self.getparam_key_value_pairs.copy()
        return links

    def make_links(self, part, params):
        data = part + '?'
        for p in params:
            if params[p] and p: 
                data += p + '=' + params[p] + '&' 
            elif p: 
                data += p + '=' + '' + '&'
        form_data = data[:-1]
        return form_data

    def toString(self):
        return 'UrlContainsParams'

        
if __name__ == "__main__":
    print('UrlContainsParams')
#   http://db.etree.org/shnlist.php?artist&artist_group_key=1&year=
