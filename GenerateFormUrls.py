
import re
import os
import requests
from requests import Request, Session
from bs4 import BeautifulSoup

# Local imports
from CategorizationIntoContexts import categorization_into_contexts
from WebRequest import web_request
import HarmlessTestString

class generate_form_urls_with_payloads:
    payload = HarmlessTestString.harmless_test_string
    complete_link = original_url = ''
    formvalues = {}
    get_params = []

    def start_search(self,link, source):
        complete_links = []
        self.core_url(link)
       
        self.get_params = []
        complete_links = self.analyse_forms(source, 'get') 
        params = []
        for x in self.get_params:   # Removing Duplicates
            if x not in params: 
                params.append(x) 

        return params, complete_links
    
    def core_url(self,link):
        exp = re.compile('https?:\/\/[\w]+?\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(link)
        if not core: return ''
        self.complete_link = core[0]
        self.original_url = core[0]
        return core

    def analyse_forms(self, source, method):
        forms = []
        links = []
        inputs = query = ''
        soup = BeautifulSoup(source, features="lxml")
        forms = soup.find_all('form')
        # forms = soup.find_all('form', attrs = {'method' : method.upper() })
        # forms = forms + soup.find_all('form', attrs = {'method' : method.lower() })
        # print('\n Forms \n', forms)
        for form in forms:
            flag, form_links = self.check_get_urls(form)
            if flag:    
                links += form_links  
        return links
        
    def check_get_urls(self, form):
        # find = categorization_into_contexts()
        if not form: 
            return False, ['']
        fields = form.find_all('input')
        if not fields: 
            return False, ['No InputFields']
        links = []
        formdata = {}
        for field in fields:
            if ( field.get('type') != 'checkbox' and field.get('type') != 'submit' and field.get('type') != 'color'
                and field.get('type') != 'button' and field.get('type') != 'reset' and field.get('type') != 'date'
                and field.get('type') != 'file' and field.get('type') != 'datetime-local' and field.get('type') != 'tel' 
                and field.get('type') != 'number' and field.get('type') != 'time' and field.get('type') != 'image'):
                self.get_params.append(field.get('name'))
                formdata[field.get('name')] = field.get('value')
        # print('\nformdata = ' , formdata)
        if not form.get('action'): 
            return False, ['No FormAction']
        # print('form-action: ' , form.get('action'))
        url = self.make_link(form.get('action'))
        self.formvalues = formdata.copy()
        num_inputs = len(formdata)
        # print('\t\t' + 'Form-Inputs:', num_inputs)
        for f in formdata:
            formdata[f] = self.payload
            data = self.merge(form.get('action'), formdata)
            # print('URL: ', url)
            get_url = url + data
            links.append(get_url)
            formdata = self.formvalues.copy()
        return True, links

    def merge(self, action, formdata):
        data = '?'
        if action.__contains__('?'):    data = '&'
        for f in formdata:
            # print('Generate form urls: fdata = ', formdata[f])
            # print('Generate form urls: f = ', f)  
            if formdata[f] and f:
                # print('inside if ')
                data += f + '=' + formdata[f] + '&' 
            elif f:
                # print('else part')   
                data += f + '=' + '' + '&'
        # print('form_data = ', data[:-1])
        form_data = data[:-1]
        return form_data
    
    def make_link(self,form_action):
        if not len(form_action) > 0 : 
            return 
        form_action = form_action.strip()
        self.complete_link = self.original_url 
        if not len(self.complete_link) > 0: 
            return
        if self.if_complete_link(form_action):  
            self.complete_link = form_action
        elif self.complete_link[-1] == '/' and form_action[0] == '/': 
            self.complete_link = self.complete_link[:-1] + form_action
        elif self.complete_link[-1] != '/' and form_action[0] == '/': 
            self.complete_link = self.complete_link + form_action
        elif self.complete_link[-1] != '/' and form_action[0] != '/': 
            self.complete_link = self.complete_link + '/' + form_action
        else:   
            self.complete_link = self.complete_link + form_action
        if self.complete_link[0] == '/' and self.complete_link[1] == '/': 
            self.complete_link = 'https:' + self.complete_link
        return self.complete_link
    
    def if_complete_link(self,action):
        if action.__contains__('https') or action.__contains__('www') :
            return True
        else:
            return False 

    def toString(self):
        return 'GenerateFormUrls'

if __name__ == '__main__':
    links = list()

    # link = 'https://www.wayfair.com'
    # link = 'https://www.lowes.com/'
    # link = 'https://www.husqvarna.com/'
    # link = 'http://www.beistle.com'
    # link = 'https://www.nobleworkscards.com'
    # link = 'https://alicescottage.com'

#   ---------------------------- Successfully Done -------------------------------- 

    # link = 'https://www.discountpartysupplies.com/'
    # link = 'https://www.earthsunmoon.com/'
    # link = 'https://www.ethanallen.com/'
    # link = 'https://www.frigidaire.com'
    # link = 'https://www.swarovski.com'
    # link = 'https://www.oscardo.com'
    # link = 'https://www.graphics3inc.com/'
    # link = 'https://www.bdiusa.com'
    # link = 'https://www.frigidaire.com'
    # link = 'https://calspas.com'                                                                                                  

    # link = 'https://www.britannica.com/search?query='
    # link = 'https://www.ediblearrangements.com/fruit-arrangements?SearchText="xyz%27yxz&lt;/zxy'
    # link = 'https://huel.com/pages/search-results?q=%22xyz'
    # link = 'https://www.harryanddavid.com/'           # Done well 
    # link = 'https://www.nearlynatural.com/'           # Done well
    # # link = 'https://www.cat.com/en_US'              # Done well
    # link = 'https://leica-geosystems.com/'            # No <form with method='get'
    # link = 'https://www.burpee.com/'                    # Done Well
    # link = 'https://www.equinenow.com/'                 # Failure: action="#"
    # link = 'https://everythingaustralian.com.au/'       # Done well
    # link = 'https://africaimports.com/'                 # Done well
    # link = 'https://www.serrv.org/'                     # No <form with method='get'
    # link = 'https://www.shamansmarket.com/'                 # No <form with method='get'
    # link = 'https://www.scotweb.co.uk/'                 # No <form with method='get'
    # link = 'https://www.countrystorecatalog.com/'       # No <form with method='get', 228 hidden inputs in post form. Failed to detect form in source 
    # link = 'https://tulumba.com/'               # No <form with method='get', blocks payloads and goes back to default page 
    # link = 'https://www.yelp.com/'               # A sencond Input Field was to be selected by user, so it was Not defined Already {Location}
    # link = 'https://www.digitaltrends.com/'         # Does Not work with payload having special chars { ', ", <, /}, No post forms
    # link = 'https://www.engadget.com/'              # No <form with method='get', has post and adding payload works, gives results

    # links.append( '' )
    # links.append( '' )
    # links.append( '' )
    # links.append( '' )
    # links.append( '' )   

    # links.append( 'https://www.wayfair.com/' )            # Fails to capture the GET Form
    # links.append( 'https://www.lowes.com/' )              # Request Times Out / Fails
    # links.append( 'https://www.uncommongoods.com/' )           # No <form with method='get' 
    # links.append( 'https://www.potterybarn.com/' )        # Fails to Detect get Form
    # links.append( 'https://www.williams-sonoma.com/' )    # Failed with "urllib" and Source Code of "Requests" doesn't have GET Form [failed]
    # link = 'https://www.williams-sonoma.com/'               # Failure

    # link = 'https://www.westelm.com/'           # Source Code downloaded doesn't have GET Form
    # link = 'https://www.dyson.com/en.html'      # Request Times Out
    # link = 'http://acehardware.com/'            # Detects <form with method='get', but there is no input field in it
    # link = 'https://www.surlatable.com/'        # Program worked fine, but website doesn't tolerates special chars {', ", <, /}
    # link = 'https://www.lampsplus.com/'           # No <form with method='get' , has post and we can use isformtrue = true => payload

    # link = 'https://www.containerstore.com/welcome.htm'     # Source Code downloaded doesn't have GET Form

    # link = 'https://www.moma.org/'              # Done Well
    # link = 'https://casper.com/home/'           # No <form with method='get'
    # link = 'https://www.pbteen.com/'            # Failed with "urllib" and Source Code of "Requests" doesn't have GET Form [failed]
    # link = 'https://www.yankeecandle.com/'      # No <form with method='get', No post
    # link = 'https://www.kirklands.com/'         # Done Well
    # link = 'https://www.1000bulbs.com/'         
    # link = 'https://www.ajmadison.com/'         # No <form with method='get' no post
    # link = 'https://www.repairclinic.com/'      # No <form with method='get' No post
    # link = 'https://www.architecturaldepot.com/' # There is a Robot Check , Failed with "urllib" and Source Code of "Requests" doesn't have GET Form  
    # link = 'https://www.roomandboard.com/'       # There is No Atrribute action="" in <form 
    # link = 'https://www.potterybarn.com/' 
    # link = 'https://www.wayfair.com/'            # Failure
    # link = 'https://www.partygameideas.com/'    # Done Well
    # link = 'https://readymadepubquiz.com/'
    # link = 'https://cardsagainsthumanity.com/'
    # link = 'https://www.keh.com/'
    # link = 'https://developers.google.com/chart/infographics/docs/post_requests'
    # link = ''

    print('\n------------------------STARTED---------------------\n')
    link = 'https://www.piceramic.com'                #Done Well

    # -------------------------Creating the Object-------------------------------
    G = generate_form_urls_with_payloads()
    a , b = G.start_search(link)
    print(a)
    print(b)

"""         Any Ideas or Algorithm, Post'em Here 
Failures:
1. https://www.yesasia.com/global/search/xyz/0-0-0-q.xyz_bpt.48-en/list.html
2. https://www.novica.com/xyz/s/
3. https://www.fragonard.com/en/search/xyz

"""
