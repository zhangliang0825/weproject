from bs4 import BeautifulSoup
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Jianxiangdata,Hisinfo_cx
import requests,time
import pymysql

# Create your views here.
def Index(request):
    data_list = Data.objects.all()    # 获取data表所有数据
    ids = []     # 存储所有id
    for data in data_list:
        ids.append(data.id)
    return render(request, 'index.html',{'ids':ids})


def Button(request,id):


    jjhost1 = '112.124.8.191'
    jjuser1 = 'root'
    jjsswd1 = 'Zycj@2020688'
    jjname1 = 'tuisong'
    jjconn2 = pymysql.connect(jjhost1, jjuser1, jjsswd1, jjname1, charset='utf8')
    jjcur2 = jjconn2.cursor()
    try:
        # sql = '''select md5link,str_date,media,spider from cx0308 where id = %s'''
        # jjcur.execute(sql,id)
        # md5link, str_date,media, spider = jjcur.fetchone()
        # id_dev3 = spider.strip('搜狗 ')

        try:
            if jjcur2:
                print(id)
                # sql = '''select html from data where  id =%s and biz = %s and media =%s
                #  and datetime = %s and type = "搜狗" '''
                sql = '''select html from data where  id =%s and type = "搜狗"'''
                jjcur2.execute(sql, (id))
                html = jjcur2.fetchone()[0]
                html = '<meta name="viewport" content="target-densitydpi=device-dpi, width=device-width " />'+html

                content = str(html).replace('data-src="',
                                                                               'src="https://m.wbiao.cn/mallapi/wechat/picReverseUrl?url=')
                #http://read.html5.qq.com/image?src=forum&q=5&r=0&imgflag=7&imageUrl=
                #http://tz6.zhangyupai.net:8181/weixintest/spider-api/?img=
                #https://m.wbiao.cn/mallapi/wechat/picReverseUrl?url=
                print(1111111111111111)
                return render(request,'jinxiang.html',{'htmls':content})
            else:
                return HttpResponse("<h1>404出错了...</h1>")
        except Exception as e:
            print(e)
            return HttpResponse("<h1>404出错了...</h1>")
    except Exception as e:
        if e:
            return HttpResponse("<h1>404出错了...</h1>")




def image_proxy(request):
    print(2222222222221111)
    img = request.GET.get('img')
    print(img,11111,request)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    }
    status = 0
    try:
        r = requests.get(
            img,
            headers=headers)
    except :
        status = 1
    if status == 1:
        return ''
    response = HttpResponse(r.content, content_type='image/jpeg')
    return response
    # global medias, keyword, warn_data, i, ides
    # num = request.GET.get("num")
    # firstname = request.GET.get("firstname")
    # biz = request.GET.get("biz")
    #
    # is_rk = request.GET.get("rk")
    # name = request.GET.get("name")
    # print(name)
    # print(id)
    # if id:
    #     # conn = pymysql.connect(host='120.26.211.213', user='huanghai', password='huanghai_password', database='news_caiji', charset='utf8mb4')
    #     # with conn.cursor() as cur:
    #     #     sql = '''insert into weixin(biz,name,collect,wxcat) values (%s,%s,%s,%s)'''
    #     #     cur.execute(sql,(biz,firstname,1,num))
    #     #     conn.commit()
    #     # try:
    #     #     post_id = Jianxiangdata.objects.get(post_id=id).post_id
    #     #     content = Jianxiangdata.objects.get(post_id = id).content
    #     #     if content:
    #     #
    #     #         return render(request,'jinxiang.html',{'htmls':content})
    #     # except Exception as e:
    #         return HttpResponse("<h1>微信数据维持三天时间...</h1>")

    #     title = Data.objects.get(pk=id).title
    #     link = Data.objects.get(pk=id).link
    #     content = Data.objects.get(pk=id).text
    #     htmls = Data.objects.get(pk=id).html
    #     medias = Data.objects.get(pk=id).media
    #     author_ = Data.objects.get(pk=id).author
    #     top_ = Data.objects.get(pk=id).is_top
    #     ori = Data.objects.get(pk=id).is_ori
    #     datetime_ = Data.objects.get(pk=id).datetime
    #     keyword = Data.objects.get(pk=id).type
    #     w_time = time.strptime(datetime_, '%Y%m%d %H:%M:%S')
    #     post_time = int(time.mktime(w_time))
    #     datetime = time.strftime('%Y%m%d', time.localtime(time.time()))
    # if is_rk == '是':
    #     data = {
    #         'title': title,
    #         'content_url': link,
    #         'content': str(content),
    #         'bizname': medias,
    #         'media_orig': medias,
    #         'datetime': post_time,
    #         'spider': '微信'
    #     }
    #     insert_url = 'http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
    #     response = requests.post(insert_url, data=data, timeout=20).text
    #     print(response)
    # if name:
    #     sql = '''select id,key1 from hisinfo_cx where key1='{}' and media='{}' and str_date = {}'''
    #     ids = Hisinfo_cx.objects.using('custom').raw(sql.format(name,medias,datetime))
    #     for i in ids:
    #         ides = i.id
    #         return render(request, 'button.html', {'id': id, 'biz': biz, 'title': title, 'link': link, 'media': medias, "datetime": datetime_,
    #                                                'author': author_, 'top': top_, 'ori': ori, 'htmls': htmls, 'type': keyword, 'firstname': firstname,
    #                                                'ruku': is_rk, 'risk_id': ides, 'name': name})
    # return render(request,'button.html',{'id':id,'biz':biz,'title': title, 'link': link, 'media':medias,"datetime":datetime_,
    #                                      'author':author_,'top':top_,'ori':ori,'htmls':htmls,'type':keyword,'firstname':firstname,
    #                                      'ruku':is_rk})

def Warehousing(request,id):
    name = request.GET.get("name")
    print(name)
    # 入库SQL语句
    # 标题，url，媒体，时间
    # date_time = time.strftime('%Y%m%d 00:00:00', time.localtime(time.time()))
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
#     # 获取当天日期
#     datetime = time.strftime('%Y%m%d',time.localtime(time.time()))
#     # key1、media需动态传入
#     sql = '''select id,key1 from hisinfo_cx where key1='{}' and media='{}' and str_date={} limit 1'''
#     ids = Hisinfo_cx.objects.using('custom').raw(sql.format(keyword,medias,datetime))
#     print(ids)
#     for i in ids:
#         url = 'http://www.zhangyupai.net/index.php?r=hisinfo/wxnotify&id=' + str(i.id)
        return HttpResponseRedirect('11111')
