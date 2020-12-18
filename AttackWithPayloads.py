
# Local imports
import HarmlessTestString
from Factory import Factory
from WebRequest import web_request
from VerifyAttack import verify_attack
from RegularExpression import regular_expression

class attack_with_payloads:
    harmless_string = HarmlessTestString.harmless_test_string
    factory = Factory.get_instance()

    def attack(self, attack_flag, attack_payloads, url, context_name, presence, 
                double_quotes, single_quotes, lessthan_sign, forwardslash):

        Text = self.factory.get_specific_item('WriteTextFile').get_object()
        if not attack_flag:
            return 
        if attack_payloads:
            print('\nAttack Paloads for ', context_name, ':\n', attack_payloads)
        for attack in attack_payloads:
            url = url.replace(self.harmless_string, attack)
            pay = attack
            print(context_name, 'Attack Url: ', url)
            # ------------- Writing To Text File --------------
            Text.write_attack_url(url)
            # -------------------------------------------------
            Web = web_request()
            Web.initialize(url,'GET')
            data = Web.get_source()
            if( data.__contains__(attack)):
                print('\nDetection  Successful with Payload: ', str(attack))
                # ------------- Writing To Text File --------------
                Text.write_status('Detection Successful with Payload: ' + str(attack) + '\n')
                # -------------------------------------------------
                RegExp = regular_expression(data)
                RegExp.set_payload(attack)
                value = RegExp.context_attack(context_name)

                VA = verify_attack()
                detection = []
                print('FINAL OUTPUT:')
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
                    
                print(detection)
                # ------------- Writing To Text File --------------
                Text.write_detection(detection)
                # -------------------------------------------------
            else:
                print('\n* Detection  UnSuccessful with payload: ', attack, ' *')
                # ------------- Writing To Text File --------------
                Text.write_status('* Detection UnSuccessful with Payload: ' + str(attack) + ' * \n\n')
                # -------------------------------------------------

    def toString(self):
        return 'AttackWithPayloads'