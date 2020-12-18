
# Python imposrts
import os

# Local imports 
from Factory import Factory
from WebRequest import web_request
from WriteTextFile import write_text_file
from AttackMethodology import attack_methodology
from UrlContainsParams import url_contains_params
from AttackWithPayloads import attack_with_payloads
from SourceCodeAnalysis import source_code_analysis
from GenerateFormUrls import generate_form_urls_with_payloads
from CategorizationIntoContexts import categorization_into_contexts

#  Program Input is a URL or List of URLs
program_input_url_list = ['https://www.zentechnologies.com', 'https://www.kickstarter.com']

def user_input():
    input_url = input('Please Enter the URL: ')
    return input_url


if __name__ == "__main__":

    url_has_params = False
    web_url = program_input_url_list[0]
    # web_url = user_input()
    while not web_url:
        web_url = user_input()


    """                         """
    """     Creating Objects    """    
    """                         """

    # Factory -> It is the  "Object Storage"  for this program
    # Object/instance created of any class is available through Factory
    factory = Factory.get_instance()   

    # WebRequest -> Send Request to Web Server with the given URL (user_input)
    Web = web_request()
    Web.initialize(web_url,'get')
    factory.add_item(Web, Web.toString())

    # WriteTextFile -> For Writing Report on the website-url
    Write_To_TextFile = write_text_file(web_url)
    factory.add_item(Write_To_TextFile, Write_To_TextFile.toString())
    
    # GenerateFormUrls -> GenerateFormUrlsWithTestStrings -> Creates links with parameters and Test Strings
    GetFormParameters = generate_form_urls_with_payloads()
    factory.add_item(GetFormParameters, GetFormParameters.toString())

    # CategorizationintoContexts -> Categorizes the Response in 4 Contexts (Attribute, HTML, Script, URL)
    Contexts = categorization_into_contexts()
    factory.add_item(Contexts, Contexts.toString())

    # SourceCodeAnalysis -> Checks the Encoding and filtering of the special chars (', ", <, /)
    SourceCodeAnalyis = source_code_analysis()
    factory.add_item(SourceCodeAnalyis, SourceCodeAnalyis.toString())
        
    # AttackMethodology -> Selecting Attack Methods for the website-url
    AM = attack_methodology()
    factory.add_item(AM, AM.toString())

    # AttackWithPayloads -> Launching Attacks with Minimal Payloads against the website-url
    AP = attack_with_payloads()
    factory.add_item(AP, AP.toString())

    """                         """
    """     Objects Created     """
    """                         """

    # Chcek if the URL contains GET Parameters                   
    if web_url and web_url.__contains__('?'):
        url_has_params = True
        Get_url_params = url_contains_params()
        get_params, links = Get_url_params.start(web_url)
    
        """ STEP-1 and STEP-2 are Completed as Params are already Given in URL
        """
    else:
        """ STEP-1: Collect the source code of website against web url(s) 
        """ 
        page_source = Web.get_source()

        """ STEP-2: Generate Links from GET-Forms and Add Harmless String
        """ 
        get_params, links = GetFormParameters.start_search(web_url, page_source)


    """     STEP-3: Submit GET-Forms / Links to Web Server and Collect Response 
    """

    if not links: 
        print( '\n No Get Parameters  \n')

    for link in links:
        Web.initialize(link, 'get')
        page_source = Web.get_source()

        """ STEP-4: Categorization of Response into 4 Contexts (Attribute, HTML, Script, URL)
        """
        attr_context, html_context, script_context, url_context = Contexts.find_contexts( page_source)
        
        """ *** Saving Context-Data in Text File
        """
        Write_To_TextFile.write_contexts(link, attr_context, html_context, script_context, url_context)

        """ STEP-5: Source Code Analysis (SCA)
            STEP-6: Attack w.r.t SCA  
            STEP-7: Verify Attack
        """

        # Attribute Context
        for attr in attr_context:   
            """ Source Code Analysis  
            """
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'ATTR', attr)
            # Write Source Code Analysis to Text Files
            Write_To_TextFile.write_encoding(' ATTR ', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)

            """ Attack Methodology
            """ 
            attack_flag, attack_payloads = AM.get_attack_payload('ATTR', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            # Write Attack Payloads to Text Files
            attack_flag and Write_To_TextFile.write_attack_payloads(attack_payloads)

            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'ATTR', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)

        # HTML Context
        for html in html_context:   
            """ Source Code Analysis
            """
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'HTML', html)
            # Write Source Code Analysis to Text Files
            Write_To_TextFile.write_encoding(' HTML ', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
           
            """ Attack Methodology
            """
            attack_flag, attack_payloads = AM.get_attack_payload('HTML', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            # Write Attack Payloads to Text Files
            attack_flag and Write_To_TextFile.write_attack_payloads(attack_payloads)

            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'HTML', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
        
        # Script Context
        for script in script_context:   
            """ Source Code Analysis
            """
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'SCRIPT', script)
            # Write Source Code Analysis to Text Files
            Write_To_TextFile.write_encoding('SCRIPT', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
            
            """ Attack Methodology
            """
            attack_flag, attack_payloads = AM.get_attack_payload('SCRIPT', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            # Write Attack Payloads to Text Files
            attack_flag and Write_To_TextFile.write_attack_payloads(attack_payloads)
            
            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'SCRIPT', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
        
        # URL Context
        for url in url_context:  
            """ Source Code Analysis
            """ 
            presence, double_quotes, single_quotes, lessthan_sign, forwardslash = SourceCodeAnalyis.encoding_analyzer( 'URL', url)
            # Write Source Code Analysis to Text Files
            Write_To_TextFile.write_encoding('URL', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
            
            """ Attack Methodology 
            """
            attack_flag, attack_payloads = AM.get_attack_payload('URL', presence, double_quotes, single_quotes, lessthan_sign, forwardslash )
            # Write Attack Payloads to Text Files
            attack_flag and Write_To_TextFile.write_attack_payloads(attack_payloads)
            
            """ Attacking with Real Payloads
            """
            AP.attack(attack_flag, attack_payloads, link, 'URL', presence, double_quotes, single_quotes, lessthan_sign, forwardslash)
        
    print('Objects Created During The Execution Of Program \n')    
    count = 1
    for item in factory.get_item_list(): 
        print( str(count) + '. ' + item.get_description())
        count += 1
    print()



"""     TASKS
    1. Generate Report
    2. GenerateFormUrls -> GenerateFormUrlsWithTestStrings 
"""

"""     REPORT STRUCTURE 
    . GET Parameters 
    . Context Distribution 
    . Source Code Analysis

"""