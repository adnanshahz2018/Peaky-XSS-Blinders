
# Python imports
import re

# Local imports
from WriteTextFile import write_text_file

class source_code_analysis:
    double_quotes = single_quotes = lessthan_sign = False 
    forwardslash = presence = False
    Text = None

    def display(self,context):
        for value in context:   
            print(value)

    def initialzie_context_encoding_variables(self):
        self.double_quotes = self.single_quotes = self.lessthan_sign = self.forwardslash = self.presence = False

    def encoding_analyzer(self, context_name, context_value):  
        self.initialzie_context_encoding_variables()
        self.presence = True
        context = str(context_value) 
        if( context.__contains__('&quot;') or context.__contains__('%22') or
            context.__contains__('&#34;') or context.__contains__("\\" + "u0022") or 
            context.__contains__('%2522') or 
            (context_name != 'URL' and context_name != 'ATTR' and context.__contains__('\\'+'"')) ):
            self.double_quotes = True 
        else: 
            self.double_quotes = self.filtering_analyzer('double', context_name, context) 

        if( context.__contains__('%27') or context.__contains__('&#39;') or context.__contains__('&#039;') or
            context.__contains__("\\" + "u0027") or context.__contains__('%2527') or 
            context.__contains__('&apos;') or (context_name != 'URL' and context_name != 'ATTR' and context.__contains__('\\'+"'")) ):
            self.single_quotes = True  
        else: 
            self.single_quotes = self.filtering_analyzer('single', context_name,context)

        if( context.__contains__('&lt;') or context.__contains__('%3C') or 
            context.__contains__('%2'+'f') ):
            self.lessthan_sign = True 
        else: 
            self.lessthan_sign = self.filtering_analyzer('less_than', context_name,context)
        
        if( context.__contains__('%2'+'F') or context.__contains__("\\" + "/") or
            context.__contains__('&#47;')  ):
            self.forwardslash = True 
        else:
            self.forwardslash = self.filtering_analyzer('forwardslash', context_name, context)
        
        return self.presence, self.double_quotes, self.single_quotes, self.lessthan_sign, self.forwardslash


    def filtering_analyzer(self, special_char, name, context):
        if name == 'ATTR' and special_char == 'double' : 
            return self.double(context) or self.attr_single_quotes_outside(context,'xyz')
        if name == 'ATTR' and special_char == 'single' : 
            return self.single(context) or self.attr_double_quotes_outside(context,'yxz')
        if name == 'ATTR' and special_char == 'less_than' : 
            return self.less_than(context)
        
        if name == 'HTML' and special_char == 'double' : 
            return self.double(context)
        if name == 'HTML' and special_char == 'single' : 
            return self.single(context)
        if name == 'HTML' and special_char == 'less_than' :
            return self.less_than(context) 

        if name == 'SCRIPT' and special_char == 'double' : 
            return self.double(context) or self.script_single_quotes_outside(context,'xyz') 
        if name == 'SCRIPT' and special_char == 'single' : 
            return self.single(context) or self.script_double_quotes_outside(context,'yxz')
        if name == 'SCRIPT' and special_char == 'less_than': 
            return self.less_than(context)
        
        if name == 'URL' and special_char == 'double' : 
            return self.double(context)
        if name == 'URL' and special_char == 'single' : 
            return self.single(context)
        if name == 'URL' and special_char == 'less_than' : 
            return self.less_than(context)
        
        if special_char == 'forwardslash' :
            return self.check_forwardslash(context)
        
        return False
   

    def double(self,context): 
        pattern1 = re.compile(r'(?!=)(?!:)\s?"[\s]*xyz')
        falsepositive = re.compile(r'[=:]\s?"\s?xyz')
        value = pattern1.findall(context)
        impure = falsepositive.findall(context)
        if value and not impure:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        return True     # Filtering is PRESENT

    def single(self, context):
        pattern1 = re.compile(r"\'[\s]*yxz")
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        return True     # Filtering is PRESENT
    
    def less_than(self, context): 
        pattern1 = re.compile(r'\<[\s]*zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nhtml Filtering Value = ',value)
            return False    # No Filtering 
        return True     # Filtering is PRESENT
  
    def check_forwardslash(self, context):
        pattern1 = re.compile(r"\/\s*uvw")
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        return True     # Filtering is PRESENT

    def attr_single_quotes_outside(self,context,attack): #xyz
        pattern = re.compile(r'[=]\s?\'[@\*!~|$_,}+*\\#*\"{*\s^*\'?\[\]*(*)*\/*.*\w*:*&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            # self.Text.write_directly("\tAttr-Double\tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True
        return False

    def attr_double_quotes_outside(self,context,attack): #yxz
        pattern = re.compile(r'[=]\s?\"[@\*!~|$_,}+\"*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*:&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            # self.Text.write_directly("\tAttr-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        return False

    def script_single_quotes_outside(self,context,attack): #xyz
        pattern = re.compile(r'[=]\s?\'[@\*!~|$_,}+:\"*\\#\'*{*\s^*?\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*'+ re.escape(attack))
        pattern1 = re.compile(r'[,]\s?\'[@\*!~|$_}+:\"*\\#\'*{*\s^*?=\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*'+ re.escape(attack))
        pattern2 = re.compile(r'[:]\s?\'[@\*!~|$_,}+\"*\\#\'*{*\s^*?=\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*'+ re.escape(attack))
        pattern3 = re.compile(r'\w{1,10}[(]\s?\'[@\*!~|$_,}+*\\#\'*{*\s^*?=\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*"\s?' + re.escape(attack))
        
        value = pattern.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Double = \tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True

        value = pattern1.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Double , \tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True

        value = pattern2.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Double : \tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True

        value = pattern3.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Double ( \tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True
        
        # self.Text.write_directly('\n\n\t There is no mitigation for Double Quotes here \n')
        # self.Text.write_directly(str(context))
        return False

    def script_double_quotes_outside(self,context,attack):  #yxz
        pattern = re.compile(r'[=]\s?\{?\"[@\=*!~|$_,}+*\\#*{*\s^*?\[\]*(*)*\/*=.*\w*&*;*\-*%*\d*]*\"?\s?[xX][yY][zZ][@\*!~|$_,}+*\\#*\"{*\s^*?\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*\s?\'?\s?' + re.escape(attack))
        pattern1 = re.compile(r'[,]\s?\"[@\*!~|$_,}+*\\#*\"{*\s^*?\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*\s?\'\s?'+ re.escape(attack))
        pattern2 = re.compile(r'[:]\s?\"[@\*!~|$_,}+*\\#*\"{*\s^*?\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*\s?\'\s?'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        value = pattern1.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        value = pattern2.findall(str(context))
        if value:    
            # self.Text.write_directly("\tScript-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        # self.Text.write_directly('\n\n\t There is no mitigation for Single Quotes here \n')
        # self.Text.write_directly(str(context))
        return False

    def toString(self):
        return 'SourceCodeAnalysis'

if __name__ == "__main__":
    print( '{Context_Encoding}')
