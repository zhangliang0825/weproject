from django.shortcuts import render,HttpResponseRedirect
from weixintest.models import Data,Hisinfo_cx
import requests,time
import pymysql
import datetime
import re
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = str(today-oneday).replace("-",'')
# Create your views here.
def Index(request):
    data_list = Data.objects.all()    # 获取data表所有数据
    ids = []     # 存储所有id
    for data in data_list:
        ids.append(data.id)
    return render(request, 'index.html',{'ids':ids})


def Button(request,id):
    global medias, keyword, warn_data, i, ides, type_num
    print(id)
    
    is_rk = request.GET.get("rk")
    name = request.GET.get("name")

    biz = Data.objects.get(pk=id).biz
    title = Data.objects.get(pk=id).title
    link = Data.objects.get(pk=id).link
    content = Data.objects.get(pk=id).text

    content = re.sub(r'<.*?>|\s+','',content)

    medias = Data.objects.get(pk=id).media
    author_ = Data.objects.get(pk=id).author
    top_ = Data.objects.get(pk=id).is_top
    ori = Data.objects.get(pk=id).is_ori
    datetime = Data.objects.get(pk=id).datetime
    
    type_ = Data.objects.get(pk=id).type
    if type_ == '搜狗':
        type_num = 3
        link = f'http://xc.zhangyupai.net:8181/weixintest/weixin_id/{id}/'+link.replace("http://mp.weixin.qq.com/s?",'')+f'&{medias}'
    elif type_ == '搜狐':
        type_num = 14
    elif type_ == '微博':
        type_num = 7
    elif type_ == '头条' and 'com/w/' not in link:
        type_num = 6
    elif  'com/w/' in link:
        type_num = 17
    if name:
        print(name)

        if name in content:
            summary = eval(content)

            summary_key = [i for i in summary if name in i]

            data = {
                'title': title,
                'content': str(content),
                'post_type': type_num,
                'summary': '',
                'media_orig': medias,
                'reporter': medias,
                'content_url': link,
                'str_date': datetime.split(' ')[0].replace('-', ''),
                'username': medias,
                'media_channel': medias,
                'is_orig': '1',
                'spider': type_
            }

        insert_url = 'http://tz4.zhangyupai.net:81/mobile/import_mynews1.php'
        resp = requests.post(insert_url, data=data, timeout=7).text
        print(resp)

        # print(name,type_num)

        datetimes = datetime.split(' ')[0].replace('-', '')


        sql = '''select id,key1 from hisinfo_cx where key1='{}' and media='{}' and str_date = '{}' and post_type = '{}'  and id >20204356 and del_flag =0'''
#         sql = f'''SELECT a.id FROM hisinfo_cx a INNER JOIN cx0308 b ON a.`post_id` = b.`id` WHERE a.`post_id` >17512570 AND a.`post_type` in (6,7,14,17) AND a.`str_date` >= {yesterday}
# AND b.`link` = '{link}' AND a.`key1` = "{name}"'''

        ids = Hisinfo_cx.objects.using('custom').raw(sql.format(name,medias,datetimes,type_num))

        if ids:

            for i in ids:
                ides = i.id

                return render(request, 'button.html', {'id': id, 'biz': biz, 'title': title, 'link': link, 'media': medias, "datetime": datetime,
                                                       'author': author_, 'top': top_, 'ori': ori, 'htmls':','.join(summary_key), 'type':type_,
                                                           'ruku': is_rk, 'risk_id': ides, 'name': name})
        else:
            return render(request, 'button.html', {'htmls':'该条新闻入库时已经被删除了....'})
    return render(request,'button.html',{'id':id,'biz':biz,'title': title, 'link': link, 'media':medias,"datetime":datetime,
                                         'author':author_,'top':top_,'ori':ori,'htmls':'','type':type_,
                                         'ruku':is_rk})

def Warehousing(request,id):


    content = Data.objects.get(pk=id)
    wtitle = content.title
    wcontent = content.text
    wurl = content.link
    wmedia = content.media
    wtime = content.datetime
    w_time = time.strptime(wtime, '%Y%m%d %H:%M:%S')
    post_time = int(time.mktime(w_time))
    data = {
        'title':wtitle,
        'content_url':wurl,
        'content': str(wcontent),
        'bizname':wmedia,
        'media_orig':wmedia,
        'datetime':post_time,
        'spider':'微信'
    }
    insert_url = 'http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
    response = requests.post(insert_url, data=data, timeout=20).text
    print(response)
    # return HttpResponse('入库成功')
    return render(request,'warehousing.html',{'id':id})

def Warn(request,id):

        return HttpResponseRedirect('11111')
