
import re
import os 

# Local imports
import HarmlessTestString
import BaseURL

class write_text_file:
    payload = HarmlessTestString.harmless_test_string
    filename = ''
    path = ''
    url = ''

    def __init__(self, url):
        self.url = url
        base = BaseURL.base_url(url)
        self.filename = self.get_filename()
        self.createfile(self.filename)

    def core_url(self, link):
        exp = re.compile('\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(link)
        print('Core Url ', core)
        return core[0]

    def createfile(self, filename):
        self.path = filename + '.txt'
        textfile = open(self.path, "w")
        textfile.write(f'\tWebsite-URL: "{self.url}"\n\n')
        textfile.close()

    def get_filename(self):
        f = self.url
        f = f.replace("/", "_")
        f = f.replace("\\", "_")
        f = f.replace(":", "_")
        f = f.replace(" ", "")
        f = f.replace("\\n", "")
        f = f.replace('%', '_')
        
        f = f.replace("*", "_")
        f = f.replace("<", "_")
        f = f.replace(">", "_")
        f = f.replace("&", "_")
        
        f = f.replace("\"", "_")
        f = f.replace("|", "_")
        f = f.replace("?", "_")
        f = f.replace("+", "_")

        f = f.replace('\n','')
        f = f.replace('\r', '')
        f = f.replace('\t', '')
        
        f = f.rstrip("\t")
        f = f.rstrip("\n")
        f = f.rstrip("\r")
        f = f.rstrip("\r\n")

        if len(f) > 150: 
            f = f[:150]
        # print('File Name => ', f)
        return f

    def write_contexts(self, link, attrs, htmls, scripts, urls):
        breakline = "\n----------------------------------------------------------------------------------\n"
        # path = self.folder + filename + '.txt'
        textfile = open(self.path, "a", encoding='utf-8')

        print( "\nWriting Data in => ", self.filename + '.txt' , '\n' )
        textfile.write('_______________________________________________________________________________________________________\n')
        textfile.write(link + "\n")
        
        textfile.write(breakline + 'Attribute Context: [' + str( len(attrs) ) + ']\n')
        for a in attrs:
            textfile.write(str(a) + "\n")

        textfile.write(breakline + 'HTML Context: [' + str( len(htmls) ) + ']\n')
        for h in htmls:
            textfile.write(str(h) + "\n")

        textfile.write(breakline + 'Script Context: [' + str( len(scripts) ) + ']\n')
        for s in scripts:
            textfile.write(str(s) + "\n")

        textfile.write(breakline + 'URI Context: [' + str( len(urls) ) + ']\n')
        for u in urls:
            textfile.write(str(u) + "\n")

        textfile.write(breakline + '\n')
        textfile.close()
#    
    def write_postforms(self, posturl, r, presence):
        breakline = "\n__________________________________________________________________________________"
        print('\n Writing Post Form Data to TEXT_FILE\n')
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a")
        textfile.write(breakline )
        textfile.write('\nPost Forms' + breakline + '\n')
        for i in range( len(posturl) ):
            textfile.write( str(posturl[i]) + '\t' + str(r[i]) + '\t' + str(presence[i]) + '\n')    
        textfile.close()

    def write_directly(self,data):
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a")
        try:
            textfile.write( data )
        except:
            textfile.write( str(data.encode(encoding='UTF-8',errors='strict')) )
        textfile.close()
        
    def write_encoding(self, Context, presence, double_quotes, single_quotes, lessthan_sign, forward_slash):
        filename = self.get_filename()
        path = filename + '.txt'
        textfile = open(path, "a")
        textfile.write('______________________________________________\n')
        textfile.write('SpecialChars     "')
        textfile.write("\t\t'" + '\t\t<' + "\t\t/ \n")
        textfile.write(Context + ':\t\t\t')
        textfile.write(str(double_quotes) + '\t')
        textfile.write(str(single_quotes) + '\t')
        textfile.write(str(lessthan_sign) + '\t')
        textfile.write(str(forward_slash) + '\n')
        textfile.close()

    def write_attack_payloads(self, payloads):
        filename = self.get_filename()
        path = filename + '.txt'
        textfile = open(path, "a")
        textfile.write('Payloads:\n')
        count = 1
        for payload in payloads:
            textfile.write('\t' + str(count) + '. ' + str(payload) + '\n')
            count += 1
        textfile.close()
    
    def write_attack_url(self, url):
        filename = self.get_filename()
        path = filename + '.txt'
        textfile = open(path, "a")
        textfile.write('Attack URL: \n')
        textfile.write('\t' + str(url) + '\n')
        textfile.close()

    def write_status(self, status):
        filename = self.get_filename()
        path = filename + '.txt'
        textfile = open(path, "a")
        textfile.write('Status:\n')
        textfile.write('\t' + status)
        textfile.close()

    def write_detection(self, detection):
        filename = self.get_filename()
        path = filename + '.txt'
        textfile = open(path, "a")
        textfile.write('Payload Detection: \n')
        for d in detection:
            textfile.write('\t' + str(d) + '\n')
        textfile.close()


    def toString(self):
        return "WriteTextFile"


if __name__ == "__main__":
    print('{WriteTextFile}')

