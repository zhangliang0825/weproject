import requests
from furl import furl
from PDF import format_web
import os
from xpinyin import Pinyin
from shutil import move
import pymysql
from loguru import logger
import base64
import datetime

date_ = datetime.datetime.now()
today_now = date_.strftime('%Y%m%d')

logger.add('上传数据报告.log',rotation='1 days')

@logger.catch
def get_content(id_,cur3,pdf_url_code):
    fuben_pinyin = {
        'cytz':'重阳投资',
        'fullgoal':'富国',
        'gtyx':'国泰元鑫',
        'guohai':'国海富兰克林',
        'nongyin':'农银汇理',
        'zxbc':'中信保诚',
        'xinquan':'兴全',
        'mingshengjiayin':'民生加银',
        'zhaoshan':'招商',
        'dzzg':'东方红资产管理',
        'jiaoyin':'交银',
        'boshi':'博时',
        'tianhong':'天弘',
        'htzg':'海通资管',
        'zjh':'证监会',
        'gyzc':'高毅资产'
    }
    all_name_chioce = {'国泰元鑫': '国泰元鑫资产',
                       '兴全': '兴证全球基金',
                       '重阳投资': '重阳投资'
                       ,'高毅资产':'高毅资产'}

    if ('index' in pdf_url_code or 'compliancerisknew' in pdf_url_code) and 'zjx' not in pdf_url_code and \
            'weekindex' not in pdf_url_code and 'quarterindex' not in pdf_url_code :

        sql = 'select key1,str_date from hisrisk_cx where id = {}'.format(id_)
        cur3.execute(sql)
        key1,str_date = cur3.fetchone()

        p = Pinyin()
        pdf_url = 'http://www.zhangyupai.net/mobile/'+pdf_url_code+'?key1={}&print=1'.format(key1)
        f = furl(pdf_url)
        if key1=='东证资管':
            key1 = '东方红资产管理'
        key_name = all_name_chioce.get(key1,f'{key1}基金')
        # if '东证资管' in key_name :
        if any(i == key_name for i in ['东方红资产管理基金','海通资管','高毅资产']):
            print(pdf_url_code)
            if 'indexv3_gyzc' in pdf_url_code:
                Shh_jiji_name = '{}{}舆情日报'.format(str_date, key_name)
            else:
                key_name = key_name.replace('基金','')
                Shh_jiji_name = '{}{}每日报告'.format(str_date, key_name)
        elif '天弘' in key_name and 'compliancerisknew' in pdf_url_code:
            Shh_jiji_name = '{}{}合规风险动态简报'.format(str_date, key_name)
        else:
            Shh_jiji_name = '{}{}每日报告'.format(str_date, key_name)
    elif  'quarterindex' in pdf_url_code:

        sql = 'select key1,str_date from hisrisk_week where id = {}'.format(id_)
        cur3.execute(sql)
        key1, str_date = cur3.fetchone()

        p = Pinyin()
        pdf_url = 'http://www.zhangyupai.net/mobile/' + pdf_url_code + '?key1={}&print=1'.format(key1)
        print(pdf_url)
        f = furl(pdf_url)

        if key1 == '东证资管':
            key1 = '东方红资产管理'
        key_name = all_name_chioce.get(key1, f'{key1}基金')
        if '东方红资产管理' in key_name:
            key_name = key_name.replace('基金', '')
            Shh_jiji_name = '{}{}媒体传播效果季度报告'.format(str_date, key_name)
        elif any(i in key_name for i in ['中信保诚','交银','华安']):
            print(123456)
            Shh_jiji_name = '{}{}媒体正面传播效果分析季报'.format(str_date, key_name)
        else:
            Shh_jiji_name = '{}{}媒体传播效果季度报告'.format(str_date, key_name)
    elif 'zjx' in pdf_url_code and 'weekindex' not in pdf_url_code:

        sql = 'select key1,str_date from hisrisk_cx where id = {}'.format(id_)
        cur3.execute(sql)
        key1, str_date = cur3.fetchone()

        p = Pinyin()
        pdf_url = 'http://www.zhangyupai.net/mobile/' + pdf_url_code + '?key1={}&print=1'.format(key1)
        f = furl(pdf_url)
        Shh_jiji_name = '{}基金规范营销每日报告'.format(str_date)
    else:
        sql = 'select key1,str_date from hisrisk_week where id = {}'.format(id_)
        cur3.execute(sql)
        key1, str_date = cur3.fetchone()

        p = Pinyin()
        pdf_url = 'http://www.zhangyupai.net/mobile/'+pdf_url_code+'?key1={}&print=1'.format(key1)

        f = furl(pdf_url)

        if key1=='东证资管':
            key1 = '东方红资产管理'
        if '国泰元鑫' in key1:
            Shh_jiji_name = '{}{}资产舆情周报'.format( str_date,key1)
        elif '东方红资产管理' in key1:
            Shh_jiji_name = '{}{}每周报告'.format(str_date, key1)
        elif '证监会' in key1:
            Shh_jiji_name = '{}证监会基金行业舆情监测周报'.format(str_date)
        else:
            Shh_jiji_name = '{}{}基金每周报告'.format(str_date, key1)

    if key1 in list(fuben_pinyin.values()):

        pingyin = list(fuben_pinyin.keys())[list(fuben_pinyin.values()).index(key1)]
    else:
        pingyin = p.get_pinyin(u"{0}".format(key1), '')
    if key1 == '东方红资产管理':
        key1 = '东证资管'

    f.args['key1'] = key1
    f.args['str_date'] = str_date

    #实例化一个url
    if 'week' in f.url:
        save_name = str_date+'zhoubao'+pingyin

        result = format_web(f.url,save_name)
    elif 'quarterindex' in f.url:
        save_name = str_date + 'jibao' + pingyin
        result = format_web(f.url, save_name)
    else:
        save_name = str_date + 'ribao' + pingyin

        result = format_web(f.url,save_name)
    if result:
        files = {

            'file': open(r'{}.pdf'.format(save_name), 'rb'),

        }
        data = {
            "token": '{"path":"/var/www/html/jijin/upload/%s/","name":"%s"}'%(pingyin,Shh_jiji_name)
        }

        response = requests.post('http://www.zhangyupai.net:8181/uploadfile/',
                                 files=files, data=data).text
        logger.debug(response)

        return 1
    else:
        return -1
#     pingyin_list.append(pingyin)
# jijin_dict = dict(zip(pingyin_list,jijin_list))
#
#     #/var/www/html/jijin/upload#服务器路径
#
#     for root,dirs,files in os.walk('D:\代码脚本\项目程序\文件上传'):
#
#         for dir in dirs:
#             print(jijin_dict)
#             if dir in list(jijin_dict):
#
#                 jijin_path = r'''D:\代码脚本\项目程序\文件上传\{}'''.format(dir)
#                 jijinname = jijin_dict.get(dir)
#
#                 f.args['key1'] = jijinname
#                 f.args['str_date'] = str_date
#                 Shh_jiji_name = '{}{}基金每日报告'.format(str_date,jijinname)
#                 #实例化一个url
#                 print(Shh_jiji_name)
#                 result = format_web(f.url,Shh_jiji_name)
#                 print(Shh_jiji_name+'.pdf', jijin_path)
#                 if result:
#                     move(Shh_jiji_name+'.pdf', jijin_path)
#                     return 1

