
# Python imposrts
import os

# Local imports 
from WebRequest import web_request
from WriteTextFile import write_text_file
from AttackMethodology import attack_methodology
from UrlContainsParams import url_contains_params
from AttackWithPayloads import attack_with_payloads
from SourceCodeAnalysis import source_code_analysis
from GenerateFormUrls import generate_form_urls_with_payloads
from CategorizationIntoContexts import categorization_into_contexts

#  Program Input is a URL or List of URLs
program_input_url_list = ['https://www.zentechnologies.com']

if __name__ == "__main__":
    url_has_params = False
    web_url = program_input_url_list[0]

    # Chcek if the URL contains GET Parameters                   
    if web_url.__contains__('?'):
        url_has_params = True
        Get_url_params = url_contains_params()
        get_params, links = Get_url_params.start(web_url)
    
        """ STEP-1 and STEP-2 are Completed as Params are already Given in URL
        """
    else:
        """ STEP-1: Collect the source code of website against web url(s) 
        """ 
        Web = web_request(web_url,'get')
        page_source = Web.get_source()

        """ STEP-2: Generate Links from GET-Forms and Add Harmless String
        """ 
        GetFormParameters = generate_form_urls_with_payloads()
        get_params, links = GetFormParameters.start_search(web_url, page_source)

    """     STEP-3: Submit GET-Forms / Links to Web Server and Collect Response 
    """
    # Create Text File Handle for Our Website
    Write_To_TextFile = write_text_file(web_url)
    SourceCodeAnalyis = source_code_analysis()

    for link in links:
        Web = web_request(link, 'get')
        page_source = Web.get_source()
        # print(page_source)

        """ STEP-4: Categorization of Response into 4 Contexts (Attribute, HTML, Script, URL)
        """
        Contexts = categorization_into_contexts()
        attr_context, html_context, script_context, url_context = Contexts.find_contexts( page_source)
        
        """ Saving Context-Data in Text File
        """
        Write_To_TextFile.write_contexts(link, attr_context, html_context, script_context, url_context)

        """ STEP-5: Source Code Analysis (SCA)
            STEP-6: Attack w.r.t SCA  
            STEP-7: Verify Attack
        """
        # Creating Object for the class Attack Methodology
        AM = attack_methodology()

        # Attacking with Payloads
        AP = attack_with_payloads()

        # Attribute Context
        for attr in attr_context:   
            """ Source Code Analysis  
            """
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'ATTR', attr)
            """ Attack Methodology
            """ 
            attack_flag, attack_payloads = AM.get_attack_payload('ATTR', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'ATTR', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)

        # HTML Context
        for html in html_context:   
            """ Source Code Analysis
            """
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'HTML', attr)
            """ Attack Methodology
            """
            attack_flag, attack_payloads = AM.get_attack_payload('HTML', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'HTML', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
        
        # Script Context
        for script in script_context:   
            """ Source Code Analysis
            """
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'SCRIPT', attr)
            """ Attack Methodology
            """
            attack_flag, attack_payloads = AM.get_attack_payload('SCRIPT', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'SCRIPT', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
        
        # URL Context
        for url in url_context:  
            """ Source Code Analysis
            """ 
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'URL', attr)
            """ Attack Methodology 
            """
            attack_flag, attack_payloads = AM.get_attack_payload('URL', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'URL', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
        


"""     Updates 
"""