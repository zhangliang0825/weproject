import time
import requests
from pyquery import PyQuery as pq
import re
from newspaper import Article
import pymysql
import json
from readability import Document
from retrying import retry
import redis
import time

dbhost3 = '120.26.106.222'
dbuser3 = 'julai01'
passwd3 = 'Sh51785136@sh'
dbname3 = 'jijin'
today = time.strftime("%Y%m%d", time.localtime())
all_dataes = []
conn3 = pymysql.connect(dbhost3, dbuser3, passwd3, dbname3, charset='utf8')
cur3 = conn3.cursor()
sql = "SELECT DISTINCT reporter FROM hisinfo_cx WHERE reporter REGEXP '{' and str_date = %s"
cur3.execute(sql, (today,))
data_list = cur3.fetchall()
all_wuxiao_word = ['荷塘月色walorke', '金融界', '问表示', '南方号', '红周刊', '问实录',
                   '六里', '查阅日本央行的数据', '快快涨涨涨', 'CIS', '和讯网', '编辑', '问。', '树超', '杨德龙', '雄鹰',
                   '张先生', '基金君', '绝对值', '通讯员', '三思君', '见闻君', '求实', '东风', '亿欧', '金石', '时风', '小钱',
                   '小二', '安卓', '时超', '包干', '搜索', '里奥', '安宁'
    , '基长', '-1', '金日', '王悦', '慧玲', '市界', '智投']
for item in data_list:
    author_all = item[0].lstrip("{").rstrip("}").strip().split(" ")
    for i in author_all:
        if (len(i) > 3 or 1 >= len(i)) or i in all_wuxiao_word:
            continue
        all_dataes.append(i)

all_dataes.extend(['陈思扬', '家俊辉', '盘和林', '赵娜', '叶映橙', '陈志杰', '何小桃',
                   '陈健', '崔昊', '张鹤仪', '胡金华', '阮润生', '冯帆', '范蓉', '刘陈希婷',
                   '一石二鸟', '胡 兵', '刘元春', '王峰', '汤懿兰', '江文耀', '何蕴虹', '养基笔记', '冉学东', '刘佳', '余俊杰', '邵瑞'
                      , '戴安琪', '邱德坤', '张晓玲', '曹安浔', '谢丽婷', '刘美琳', '朱丽娜', '李致鸿', '谢中秀', '陈红兵', '胡静波', '石秀珍', '唐韶葵',
                   '姜诗蔷', '张尔妮'])
all_authors = list(set(all_dataes))
all_authors = sorted(all_authors, key=lambda x: len(x), reverse=True)


def index_author(sentence):
    global index_num

    if all(i not in sentence for i in ['表示', '咨询', '采访', '了解', '获悉', '2020', '“',
                                       '2019', '2018', '邮箱', 'com', '微信', '字数']):

        if '记者' in sentence:

            index_num = sentence.find('记者')

        elif '作者' in sentence:
            index_num = sentence.find('作者')

        try:
            right_word = sentence[index_num + 2]  # 超出索引

            if right_word != '，' and right_word != '。' and right_word != '，' and \
                    right_word != '“' \
                    and not right_word.isdigit():

                if not '\u4e00' <= right_word <= '\u9fff' or right_word == '丨' or \
                        right_word == '丨 ':  # 不等于中文

                    return True
                return False
        except:
            return False


def export_author(html):
    global author_split_text, index_num
    all_data = []
    author_split = html.split('</')

    author_texts = [re.sub(r'<.+?>', '', '</' + i) for i in author_split]

    author_text = [k for k in author_texts if k != '']

    for index_j, j in enumerate(author_text):

        if '作者' in str(j) or '记者' in str(j):

            #     continue

            if '记者' in str(j):
                index_num = str(j).find('记者')
            elif '作者' in str(j):
                index_num = str(j).find('作者')
            j = j[index_num:]

            if len(re.sub(r'\s+', '', j)) <= 3:

                j = j + author_text[index_j + 1]
                j = j.strip('&nbsp;')
                if len(j) <= 4:
                    j = j + author_text[index_j + 2]
            else:
                j = j

            all_data.append(j.strip())

    all_data = [i for i in all_data if '2019-' not in i and '2020-' not in i]

    # author_text = [j.strip()+author_text[index_j+1] if ('作者' in str(j) or '记者' in str(j) )
    # and len(author_text[index_j+1].strip().replace(' ',''))<=5#阀门
    # # else j.strip() for index_j,j in enumerate(author_text) if ('作者' in str(j) or '记者' in str(j))
    # ]

    # author_text = [i.replace('记者','记者:').replace('作者','作者:')for i in author_text if  len(i)<=12]

    author_list = list(filter(index_author, all_data))

    # author_list = [k for k in author_list if len(k.strip())>=4]#排序赛
    author_list = sorted(author_list, key=lambda x: len(x))

    author_list = [i for i in author_list if all(i != j for j in ['作者：', '作者', '记者', '记者：'])]

    try:
        if '作者' in author_list[0]:
            author_split_text = author_list[0].split('作者')[-1]
        elif '记者' in author_list[0]:
            author_split_text = author_list[0].split('记者')[-1]  # 后面是有符号

        fiale_text = re.findall(re.compile(r'[0-9A-Za-z\u4e00-\u9fa5]+'), str(author_split_text))
        all_author = ' '.join(fiale_text)

        author_real = ' '.join([i for i in re.sub(r'\s', '-', all_author).split('-')
                                if len(re.sub(r'[|]|\s+|:|;|丨|', '', i)) <= 3 and i.strip() != ''])
        # re.sub(r'')

        if author_real == '':

            a = strange_content(str(html))
            return a
        else:
            author_real = re.sub(r'字数| 文|通讯员|／文|新华社|[|]|图网|来源|摄|丨', '', author_real).strip()

            # 数字控制尾巴输出的

            return author_real.split("编辑")[0] if author_real else -1  # 作者后面是有符号的时候没有匹配上

    except:
        a = strange_content(html)

        if a:
            return a
        else:
            return ''


def square_author(html):
    try:
        all_html = str(html)

        if all(word in all_html for word in ['（', '）']):

            author_pattern1 = re.findall(re.compile(r'[（](.*?)[）]'), str(html))

        else:
            author_pattern1 = ['']

        if all(word in all_html for word in ['(', ')']):
            author_pattern2 = re.findall(re.compile(r'[(](.*?)[)]'), str(html))
        else:
            author_pattern2 = ['']

        author_pattern = author_pattern1 + author_pattern2

        author_real = [i for i in author_pattern if any(word in i for word in ['记者', '作者', '绝对值'])]  # 有记者的条件下在文中出现

        author_real = [i[i.find(j):] for j in ['记者', '作者', '绝对值'] for i in author_real if i.find(j) != -1]

        author_real = list(map(lambda x: re.sub(r'记者|作者|绝对值', '', x), author_real))  # 用map函数不用切片防止出现错误

        if len(author_real[0].strip().replace(' ', '')) <= 7:  # 有记者的前提条件下

            return author_real[0].strip().split("编辑")[0].replace('摄', '').replace('字数', '')
        else:
            return -2
    except:

        return -2


def strange_content(html):
    html = pq(html).html()  # 全部标签信息
    html_text = pq(html).text()

    html = Document(html).summary()  # 特殊处理的文本的便器

    all_content_text = ''.join(
        re.findall(r'[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5,]',
                   pq(html).text()))

    index_num = html_text.find(all_content_text[:10])

    text_1 = html_text[0:index_num + 10] + all_content_text[:150]  # 阀门文本数据量多少
    text_2 = all_content_text[-150:]
    text_all = text_1 + text_2
    all_data = ['']
    for authors in all_authors:

        author_re = re.findall(r'{}'.format(authors), str(text_all))

        if author_re:

            author_re = author_re[0]

            re_content = str(text_all)[str(text_all).find(author_re):str(text_all).find(author_re) + 5]

            if any(i in re_content for i in ['表示', '咨询', '采访', '了解', '获悉', '2020', '“',
                                             '2019', '2018', '邮箱', 'com', '微信', '得知', '认为', '告诉'
                , '注意', '就曾', '投签', '产投', '建议']): continue
            if author_re in all_data[-1]:
                continue
            all_data.append(author_re)

    return all_data

    # return author_re


def wx_content(url):  # 微信调用
    article = Article(url, language='zh')
    article.download()
    html = pq(article.html)

    result1 = square_author(html.text())

    if result1 != -2:
        return result1
    if result1 == -2:
        content_doc1 = str(html('div.rich_media_content'))
        content_doc = content_doc1.replace('记&nbsp;&nbsp;者', '记者').replace('作&nbsp;&nbsp;者', '作者') \
            .replace('记&nbsp;者', '记者').replace('作&nbsp;者', '作者') \
            .replace('记 者', '记者').replace('作 者', '作者').replace('记   者', '记者').replace('作   者', '作者')

        if '记者' in content_doc or '作者' in content_doc:

            wx_author = export_author(content_doc)

            if wx_author == ['']:  # 一旦得到-1说明记者和作者不存在

                wx_author = html("span.rich_media_meta.rich_media_meta_text").text()

            #     return wx_author,2
            # return wx_author,2
            return ''.join(wx_author)
        else:
            a = strange_content(html)
            if a != ['']:
                wx_author = ''.join(a)
            else:
                wx_author = html("span.rich_media_meta.rich_media_meta_text").text()

            return wx_author
    else:
        return ''


def judge_common_content(url, contents):
    if "epaper.cs.com.cn" in url:
        html1 = contents.replace('□', '记者:').replace('⊙', '记者:')

    elif 'paper.cnstock.com' in url:
        html1 = contents.replace('⊙', '记者:').replace('□', '记者:')
    elif 'www.toutiao.com' in url:
        html1 = re.sub(r'记者', '记者', contents)
    elif 'finance.sina.com.cn' in url:
        article = Article(url, language='zh')
        article.download()
        html1 = article.html
        html1 = pq(html1)("div.article").html()


    else:
        article = Article(url, language='zh', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'})
        article.download()
        html1 = article.html.replace('⊙', '记者:').replace('□', "记者:")

    content = pq(html1).text()
    result1 = square_author(content)

    if result1 != -2:
        return result1
    if result1 == -2:

        html = html1.replace('记&nbsp;&nbsp;者', '记者').replace('作&nbsp;&nbsp;者', '作者') \
            .replace('记&nbsp;者', '记者').replace('作&nbsp;者', '作者') \
            .replace('记 者', '记者').replace('作 者', '作者').replace('记&nbsp; &nbsp;者', '记者'). \
            replace('作&nbsp; &nbsp;者', '作者')
        if '记者' in str(html) or '作者' in str(html):

            author = export_author(html)
            print(author)
            if author != ['']:
                return ''.join(author)

        else:
            a = strange_content(content)
            if a == ['']:
                return ''
            else:
                return ''.join(a)
    return ''


def main(url, content):
    for i in range(1, 5):
        print('请求{}次'.format(i))
        try:
            if 'weixin.qq.com' in url:
                a = wx_content(url)
                return a
            elif 'http://xc.zhangyupai.net/' in url:
                url = 'https://mp.weixin.qq.com/s?' + url.split('/')[-1]
                a = wx_content(url)

                return a
            else:
                b = judge_common_content(url, content)
                return b
        except Exception as e:
            if not e:
                break



if __name__ == '__main__':

    dbhost3 = '120.26.106.222'
    dbuser3 = 'julai01'
    passwd3 = 'Sh51785136@sh'
    dbname3 = 'jijin'

    conn3 = pymysql.connect(dbhost3, dbuser3, passwd3, dbname3, charset='utf8')
    cur3 = conn3.cursor()

    pool = redis.ConnectionPool(host='tz6.zhangyupai.net', port=6379, db=2, password='Lz@12@12@julai')
    r = redis.Redis(connection_pool=pool)
    id_ = r.get(11).decode('utf8')

    sql = f'''SELECT DISTINCT a.id, a.link FROM cx0308 a INNER JOIN hisinfo_cx b ON a.id = b.post_id WHERE b.post_type IN (0,3,14,4,6) AND
    b.str_date >="20210412" AND b.`key1` IN ( "嘉实","新华","富国","鹏华","中欧","中邮","平安","国海富兰克林","长信","兴全","国泰","摩根士丹利华鑫","中信保诚","华宝","广发","大成","万家共赢",
    "南方","易方达","博时","天弘","华夏","交银","农银汇理","华安","海富通","工银瑞信","中银","建信","银华","华商","汇添富",
    "前海开源","华泰柏瑞","光大保德信","国泰元鑫","重阳投资","招商","富安达","民生加银")   and b.id =	24938497 ORDER BY a.`id` ASC'''

    cur3.execute(sql)
    data_list = cur3.fetchall()

    for id_, link in data_list:

        # if 'weixin' in link:
        #     # time.sleep(2.5)
        # else:
        #     time.sleep(0.5)
        if '.mp4' in link:
            continue

        try:
            if "epaper.cs.com.cn" in link or 'paper.cnstock.com' in link or \
                    'www.toutiao.com' in link:
                sql = 'select content from cx0308 where id =%s'
                cur3.execute(sql, id_)
                contents = cur3.fetchone()[0]
                print(contents)
                author = main(link, contents)
            else:
                author = main(link, '')
            author = '[%s]' % author
            print(author)
            sql = 'update hisinfo_cx set reporter = %s where post_id = %s'
            # cur3.execute(sql, (author, id_))
            # conn3.commit()
            # r.set(11, str(id_))

        except Exception as e:
            print(e)

