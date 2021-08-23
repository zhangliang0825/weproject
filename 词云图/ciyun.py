import pymysql
import csv
import jieba.analyse
import numpy as np
from PIL import Image
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import re
import pandas as pd
import datetime

today = datetime.date.today()
last_week = str(today - datetime.timedelta(days=5))
last_week_f = str(today - datetime.timedelta(days=20))


def main(keyword):
    dbuser = 'julai01'
    dbpass = 'Sh51785136@sh'
    dbhost = '120.26.106.222'
    dbname = 'jijin'

    db = pymysql.connect(dbhost, dbuser, dbpass, dbname, charset='utf8')
    cur = db.cursor(pymysql.cursors.SSCursor)

    dbhost2 = '120.26.211.213'
    dbuser2 = 'julai01'
    passwd2 = 'Zycj@2020688'
    dbname2 = 'test1'
    conn2 = pymysql.connect(dbhost2, dbuser2, passwd2, dbname2, charset='utf8')
    cur2 = conn2.cursor()

    sql = 'select words,weight  from `Clwords` where del_flag = %s and name = %s'

    cur2.execute(sql,(1,keyword))
    exclude_word = [i[0] for i in cur2.fetchall()]
    cur2.execute(sql, (0, keyword))
    include_word = {i[0]:i[1] for i in cur2.fetchall()}
    try:
        if keyword in ['富安达', '国泰元鑫']:
            sqlToday = "SELECT a.id, a.key1, a.str_date, cx0308.content FROM hisinfo_cx a INNER JOIN cx0308 ON a.post_id = cx0308.id AND a.grp_id =0 AND a.post_type <>1 AND a.del_flag =0 AND a.key1 ='{name}' " \
                       "WHERE a.str_date >='{weekly}' AND a.str_date <='{today}'".format(name=keyword,
                weekly=last_week_f.replace('-', ''), today=str(today).replace('-', ''))
            cur.execute(sqlToday)

        else:
            sqlToday = "SELECT a.id, a.key1, a.str_date, cx0308.content FROM hisinfo_cx a INNER JOIN cx0308 ON a.post_id = cx0308.id AND a.grp_id =0 AND a.post_type <>1 AND a.del_flag =0 AND a.key1 ='{name}' " \
                       "WHERE a.str_date >='{weekly}' AND a.str_date <='{today}'".format(name=keyword,
                weekly=last_week.replace('-', ''), today=str(today).replace('-', ''))
            cur.execute(sqlToday)
        print('{}词云图生成中.....'.format(keyword) + '日期从{}到{}'.format(last_week, today))
        num = []
        dates = []
        contents = []
        for line in cur:
            id, key1, date, content = line

            for i in content.split('。'):
                for j in re.split(r'\s+', i):
                    if keyword[:3] in j:
                        num.append(id)
                        contents.append(j)
                        dates.append(date)
        df = pd.DataFrame({'content': contents, 'id': num, 'date': dates})
        df.to_csv('result.csv', encoding='utf8')

        with open('result.csv', 'r', newline='', encoding='utf8') as f:
            reader = csv.reader(_.replace('\x00', '') for _ in f)
            rows = ''
            for row in reader:

                rows += ''.join(row[1])

        jieba.load_userdict('all_jijin_words.txt')
        jieba.analyse.set_stop_words("stop_ciyun.txt")
        result = jieba.analyse.textrank(''.join(contents), topK=150, withWeight=True)
        out = open('Keyword_probability.csv', 'w', newline='')
        csv_writer = csv.writer(out, dialect='excel')
        for j in result:
            line = list(j)
            csv_writer.writerow(line)
        keywords = include_word

        for i in result:
            if i[0] in  exclude_word:
                continue
            keywords[i[0]] = i[1]

        image = Image.open('28e.jpg')
        graph = np.array(image)
        wc = WordCloud(font_path="msyh.ttc", width=100, height=100,background_color='white', \
            random_state=100, max_words=250, \
            mask=graph, ).generate_from_frequencies(keywords)
        image_color = ImageColorGenerator(graph)
        plt.imshow(wc)
        plt.imshow(wc.recolor(color_func=image_color))
        plt.axis('off')
        plt.show()
        if plt.savefig('{}_{}_weeklyciyun1'.format(keyword, str(today).replace('-', '')),
            dpi=300):
            return 1
        else:
            return 0
    except Exception:
        return 0


if __name__ == '__main__':
    keyword_list = ['富国',]
    for keyword in keyword_list:
        main(keyword=keyword)
