import requests
import json

class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        #需要传递的参数
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【姚鹏】正在进行登录操作，您的验证码是{code}".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        print(re_dict)
        return re_dict

if __name__ == "__main__":
    #例如：9b11127a9701975c734b8aee81ee3526
    yun_pian = YunPian("c779794c70d86d505f1c4e67652f9589")
    yun_pian.send_sms("2018", "13546367788")