

""" Returns the Base for a web_url """ 

# Input:  'https://www.abc.com/index.php' 
# Output: 'abc.com'

def base_url(web_url):
    link = web_url
    link = link.replace('http://www','')
    link = link.replace('https://www','')
    link = link.replace('http://','')
    link = link.replace('https://','')
    if link.__contains__('/'): 
        parts = link.split('/')
        link = parts[0]
    return link