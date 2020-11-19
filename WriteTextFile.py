
import re
import os 

# Local imports
import HarmlessTestString
import BaseURL

class write_text_file:
    payload = HarmlessTestString.harmless_test_string
    url = ''
    path = ''
    filename = ''
    # folder = 'drive/My Drive/SQL_Vulnerable/'
    # folder = 'TuningData/'

    def __init__(self, url):
        self.url = url
        base = BaseURL.base_url(url)
        # self.folder = base + '/'
        # self.folder = self.core_url(self.url) + '/'
        self.filename = self.get_filename()
        self.createfile(self.filename)

    def core_url(self, link):
        exp = re.compile('\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(link)
        print('Core Url ', core)
        return core[0]

    def createfile(self, filename):
        # path = self.folder + filename + '.txt'
        self.path = filename + '.txt'
        textfile = open(self.path, "w")
        textfile.write(f'\tWebsite-URL =  "{self.url}"\n\n')
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
    def write_response(self, filename, data):
        path = '' +  filename + '.txt'
        textfile = open(path, "w+")
        # print(data)
        textfile.write(str(data))
        textfile.close()

    def write_links(self, filename, links):
        path = '' +  filename + '.txt'
        textfile = open(path, "w+")
        for data in links:  textfile.write(str(data) + '\n')
        textfile.close()
    
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
        return
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a")
        if Context is None: 
            textfile.write('\n\n\t\t \t\tENCODING SUMMARY \n\t   \t  Presence\t\t"' + "\t\t'" + '\t\t<' + "\t\t/ \n")
            return
        textfile.write('Mitigation        "' + "\t'" + '\t<' + "\t/ \n")
        textfile.write(Context +':\t\t' + str(double_quotes) +'\t')
        textfile.write( str(single_quotes) +'\t'+ str(lessthan_sign) +'\t'+ str(forward_slash) + '\n' )
        textfile.close()


if __name__ == "__main__":
    print('{WriteTextFile}')

