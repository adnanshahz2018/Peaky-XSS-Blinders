
# Local imports
from RegularExpression import regular_expression
import HarmlessTestString

class categorization_into_contexts:
    R = None 
    url = ''
    payload = HarmlessTestString.harmless_test_string

    def find_contexts(self, pagesource):    
        R = regular_expression(pagesource)

        attrs   = R.RegExpAttribute()
        htmls   = R.RegExpHtml()
        scripts = R.RegExpScript()
        urls    = R.RegExpURI()

        same_attrs    = R.RegExpSameAttribute()
        same_htmls    = R.RegExpSameHtml()
        same_scripts  = R.RegExpSameScript()
        same_urls     = R.RegExpSameURI()
        
        # Display the Context Values on the Console 
        # self.display(attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls)
        return attrs, htmls, scripts, urls

    def display(self, attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls):
        print('Attribute Context [' , len(attrs)        ,  ']\n' , attrs)
        print('HTML Context ['      , len(htmls)        ,  ']\n' , htmls)
        print('Script Context ['    , len(scripts)      ,  ']\n' , scripts)
        print('URI Context ['       , len(urls)         ,  ']\n' , urls)
        
        # print('SAME Attribute ['    , len(same_attrs)   ,  ']\n' , same_attrs)
        # print('SAME HTML ['         , len(same_htmls)   ,  ']\n' , same_htmls)
        # print('SAME Script ['       , len(same_scripts) ,  ']\n' , same_scripts)
        # print('SAME URI ['          , len(same_urls)    ,  ']\n' , same_urls)
        
    def toString(self):
        return 'CategorizationintoContexts'

if __name__ == "__main__":
    print('{FindContext}')


