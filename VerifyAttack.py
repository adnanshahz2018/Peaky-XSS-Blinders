
# Python imports
import re

class verify_attack:

    def attr_single_quotes_outside(self, context, attack): #xyz
        pattern = re.compile(r'[=]\s?\'[@\*!~|$_,}+*\\#*\"{*\s^*\'?\[\]*(*)*\/*.*\w*:*&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            # self.Text.write_directly("\tAttr-Double\tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True
        return False

    def attr_double_quotes_outside(self, context, attack): #yxz
        pattern = re.compile(r'[=]\s?\"[@\*!~|$_,}+\"*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*:&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            # self.Text.write_directly("\tAttr-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        return False

    def script_single_quotes_outside(self, context, attack): #xyz
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

    def script_double_quotes_outside(self, context, attack):  #yxz
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
