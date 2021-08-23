from datetime import datetime,timedelta


class ProxyModel(object):
    def __init__(self,data):#初始化变量
        self.ip = data['IP']
        self.port = data['Port']
        self.expire_str = data['ExpireTime']
        self.proxy = 'http://' + '%s:%s' % (self.ip, self.port)
        self.start_num = 0
        self.expire_time = self.detail_time
        self.blacked = False

    @property
    def detail_time(self):#类的每个属性值
        date_str, time_str = self.expire_str.split(" ")
        year, month, day = date_str.split("-")
        hour, minute, second = time_str.split(":")
        expire_time = datetime(
            year=int(year),
            month=int(month),
            day=int(day),
            hour=int(hour),
            minute=int(minute),
            second=int(second),
        )

        return expire_time

    @property
    def is_expiring(self):
        now = datetime.now()
        # proxies = {
        #  'http': 'http://%s:%s'% (self.ip, self.port),
        #   'https': 'https://%s:%s'% (self.ip, self.port)}
        # import requests
        #
        # try:
        #     response = requests.get('http://httpbin.org/get', proxies=proxies,timeout = 6.5)
        #     if response.status_code ==200:
        #         return True
        #     else:
        #         return False
        # except Exception as e:
        #     if e:
        #         print(e,'报错...')
        #         return False
        print(self.expire_time,7777777)
        print(self.expire_time - now)
        print(timedelta(seconds=30))
        if self.expire_time - now < timedelta(seconds=30):
            return True
        else:
            return False
