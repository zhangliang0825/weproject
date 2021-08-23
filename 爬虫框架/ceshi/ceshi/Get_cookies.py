# -*- coding: utf-8 -*-

class BosstransCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict
#
if __name__ == "__main__":
    cookie = "ttcid=5383c7cd65124c279ea8627231ba07ce20; tt_webid=6932748630370256391; csrftoken=03eed9c57e1c13ede8ff0655484a0648; csrftoken=03eed9c57e1c13ede8ff0655484a0648; passport_csrf_token=4729b295111b1fc9c128e4f47179c0a5; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; PIXIEL_RATIO=1.5; __utma=24953151.1786946199.1615880696.1615880696.1617849239.2; WIN_WH=391_578; ttwid=1%7CKsJtLsS-oK5WbTn-fv37N6TkXnFSTSPYxsiGdINBDio%7C1618188472%7C5386f584537fd9ff3ee5558cd9371fd4926453b8e4ac8ed7e6699fa02c161c79; tt_webid=6940875644386870798; __ac_signature=_02B4Z6wo00f01M9M3AQAAIDDf70wz.HsrqzPaNiAAFOw8t7Nwh-E2G7LF6abgYJXWG9OuvYxwq6CCJ4Zw6WzycO0JXwrFT5DAfLlsaWoSXPsp6u4JZXz1kNHq.sIGJGiwOt9UAm4o52FwvQy70; s_v_web_id=verify_kniwvr4g_HArrJ2D2_B3TB_4qrh_8cdL_CM6aIZ1AiACx; __tasessionId=maakb6ws81618492903576; MONITOR_WEB_ID=0de62af0-9498-4a8c-90c9-7d7f058883f0; tt_scid=VzV9UC.IIaeP6HZV8X-HwlBlrC-DyvTplkCRBlkQzLjCOeexNEP8smv5MC.HnEa8005f"
    trans = BosstransCookie(cookie)
    print(trans.stringToDict())