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
# if __name__ == "__main__":
#     cookie = "lastCity=101020100; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=6be0f9e7-3e1a-4704-bff0-6df9b2946669; __c=1586059193; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1586059193; __l=l=%2Fwww.zhipin.com%2Fshanghai%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDdiHC088qh0KZEgsA1NC-X000007hOm-C00000LlxwwA.THdBULP1doZA8QMu1x60UWdBmy-bIy9EUyNxTAT0T1dBPjcsn1ubnH0snj7Bm1P-0ZRqnHPAPYfYwRcdPDN7nj0zfRc3Pjbdf1b3PH6zwRN7wjb0mHdL5iuVmv-b5Hn1PjnvP10knWDhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1Y1PW0znf%26tpl%3Dtpl_11534_21264_17382%26l%3D1516420953%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3343670121_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D140%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3138%26prefixsug%3Dboss%26rsp%3D0&g=%2Fwww.zhipin.com%2Fshanghai%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&friend_source=0; __a=71730166.1573305219.1573305219.1586059193.21.2.13.13; __zp_stoken__=8420yji3YHfhuVVwNgPwTbzY4wbwhxR2xxEaJdwNMzUiYH7lJ1tMKPIkQ10xBjRIh5E5sirR8V4SUvEBVMUBnNGmCwcOE2ngIn5i6K0xnykm3KamV38EFY4kC60nyZlFFCa4; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1586059983"
#     trans = BosstransCookie(cookie)
#     print(trans.stringToDict())