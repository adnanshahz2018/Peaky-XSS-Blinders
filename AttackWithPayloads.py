
# Local imports
import HarmlessTestString
from VerifyAttack import verify_attack
from RegularExpression import regular_expression
from WebRequest import web_request

class attack_with_payloads:
    harmless_string = HarmlessTestString.harmless_test_string

    def attack(self,
        attack_flag, attack_payloads, url, 
        context_name, presence, double_quotes, 
        single_quotes, lessthan_sign, forwardslash 
        ):
        if attack_flag:
            if attack_payloads:
                # self.Text.write_directly('\nAttack Payloads for ' + str(context_name) + '\n' + str(attack_payloads) + '\n')
                print('\nAttack Paloads for ', context_name, '\n', attack_payloads , '\n')
            for attack in attack_payloads:
                url = url.replace(self.harmless_string, attack)
                pay = attack
                # links = self.read_excel()
                print('\n', context_name, 'Attack Url: ', url)
                # self.Text.write_directly('\n'+ context_name + ' Attack Url: ' + url)
                Web = web_request(url,'GET')
                data = Web.get_source()
                if( data.__contains__(attack)):
                    print('\n\n=>Detection  Successful with Payload: ', str(attack), '\n')
                    # self.Text.write_directly('\n\n=>Detection  Successful with Payload: ' + str(attack) + '\n')
                    # print('=>The Automated Tool Assumes that there is a potential XSS Present in the Website\n')
                    RegExp = regular_expression(data)
                    RegExp.set_payload(attack)
                    value = RegExp.context_attack(context_name)

                    VA = verify_attack()
                    detection = []
                    print('FINAL OUTPUT:\n')
                    for val in value:
                        if  context_name == 'ATTR':
                            if not single_quotes and not VA.attr_double_quotes_outside(val, attack): 
                                detection.append(str(val))
                            if not double_quotes and not VA.attr_single_quotes_outside(val, attack): 
                                detection.append(str(val))
                        elif  context_name == 'SCRIPT':
                            if not single_quotes and not VA.script_double_quotes_outside(val, attack): 
                                detection.append(str(val))
                            if not double_quotes and not VA.script_single_quotes_outside(val, attack): 
                                detection.append(str(val))
                        else:
                            detection.append(str(val))
                     
                    # self.write_excel_attack_description(url, context_name, 'TRUE', detection)
                    # self.Text.write_directly('\nFINAL OUTPUT: ' + '\n')
                    print( detection  , '\n\n')
                    for d in detection: 
                        # self.Text.write_directly(str(d) + "\n")
                        pass
                else:
                    print('\n\n ***** Detection  UnSuccessful with payload: ', attack, '\n\n')
                    # self.write_excel_attack_description(url, context_name, 'FALSE', 'None')
                    # self.Text.write_directly('\n\n ______Detection  UnSuccessful with payload: ' + str(attack) + '\n\n')
     