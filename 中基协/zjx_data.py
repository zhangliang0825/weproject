
import csv
import datetime
import re
from pyquery import PyQuery as pq
import datetime

Today = datetime.datetime.now()
Today_str = Today.strftime('%Y%m%d')
print(Today_str)



word_str_3 = '坐享、安享、尽享、日回报、从业回报、欲购从速、' \
             '从业年限、安沁、今年以来、季度收益、排名、限额发售、限额配售、' \
             '限额销售、稳健、募集上限、比例配售、第一名、冠军、唯一'



word_3_list = word_str_3.split('、')



product_name_list = []
jijin_name_list = []
product_key_list = []
all_data_file = csv.reader(open('20200331新发基金.csv', 'r',encoding='utf8'))

all_data_ = [(product_name, product_key, jijin_name) for product_name, product_key, jijin_name in all_data_file
             if '新发基金' not in product_name and product_name!='']


def get_content_api(jj_id,cur3,conn3):

    sql = f'''select id,post_type,title,str_date,media,link from cx0308 where id >11814702
                 and str_date>=20210329'''
    cur3.execute(sql)
    data_list = cur3.fetchall()

    S_conut = ['%s'] * 9
    S_conut = ','.join(S_conut)
    key1_word = '中基协'

    for id_, post_type, title, str_date, media, link in data_list:  # id_cx0308
        print(id_, post_type, title, str_date, media, link)
        try:
            sql = 'select content from cx0308 where id = %s'
            cur3.execute(sql, id_)
            content = cur3.fetchone()[0]

            content_re = re.sub(r'\[.*?\]|<.*?>|\s+', '', content)
            content_spilt = re.split(r'。', content_re)
            if post_type==3 and media in ['中融基金','大成基金','大成基金','东方基金微助手','大成财经汇','汇安基金','万家基金微理财','浙商基金'
                                          ,'浙商基金微视界']:

                hisinfo_sql = f'''select key1,category,summary,media from hisinfo_cx where
                              del_flag = 0 and post_id ={id_} and (category LIKE "%@%" OR  category LIKE "%A%"  OR category LIKE "%a%" )'''  # 涉及到基金公司的sqland key1 in {name_list}

                cur3.execute(hisinfo_sql)
                all_data_fur = cur3.fetchall()

                if all_data_fur:
                    PROduct = [j[0] for j in all_data_ if j[1] in content]  # 产品名的匹配

                    if PROduct:  # 产品在文章
                        num = len((PROduct))
                        summary = [k for k in content_spilt for j in all_data_ if j[1] in k][:num]
                        summary_text = ''.join(summary) + '。'
                        product_tag = '|'.join(PROduct)
                        sql2 = '''insert into hisinfo_cx(post_id,summary,post_type,key1,str_date,
                                       tags,media,media_channel,zjx_p) values (%s)''' % (S_conut)
                        cur3.execute(sql2, (id_, summary_text, post_type, key1_word, str_date, '({})'.format(product_tag)
                                            , all_data_fur[0][-1], all_data_fur[0][-1], 1))
                        conn3.commit()
                        print(title, str_date, media, link, product_tag, summary_text, '微信')
                        return 1
                    else:
                        doc = pq(link)('div.rich_media_content')
                        if 'https://mmbiz.qpic.cn' in str(doc):
                            sql2 = '''insert into hisinfo_cx(post_id,summary,post_type,key1,str_date,
                                                   tags,media,media_channel,zjx_p) values (%s)''' % (S_conut)
                            cur3.execute(sql2, (id_, '', post_type, key1_word, str_date, '()'
                                                , all_data_fur[0][-1], all_data_fur[0][-1], 3))
                            conn3.commit()
                            return 3

            else:


                    hisinfo_sql = f'''select key1,category,summary,media from hisinfo_cx where
                       del_flag = 0 and post_id ={id_} and (category LIKE "%@%" OR  category LIKE "%A%"  OR category LIKE "%a%" )'''  # 涉及到基金公司的sqland key1 in {name_list}

                    cur3.execute(hisinfo_sql)
                    all_data_fur = cur3.fetchall()

                    if all_data_fur:
                        if '基金' in str(content) and '公告' not in title:
                            PROduct = [j[0] for j in all_data_ if j[1] in content]#产品名的匹配
                            if PROduct:  # 产品在文章
                                num = len((PROduct))
                                summary = [k for k in content_spilt for j in all_data_   if j[1] in k][:num]
                                summary_text = ''.join(summary)+'。'
                                product_tag = '|'.join(PROduct)
                                sql2 = '''insert into hisinfo_cx(post_id,summary,post_type,key1,str_date,
                                    tags,media,media_channel,zjx_p) values (%s)''' % (S_conut)
                                cur3.execute(sql2, (id_, summary_text, post_type, key1_word, str_date, '({})'.format(product_tag)
                                                    , all_data_fur[0][-1], all_data_fur[0][-1], 1))
                                conn3.commit()
                                print(title, str_date, media, link, product_tag,summary_text)
                                return 1
                            else:
                               #关键词的匹配

                                if '@' in ''.join([i[1] for i in all_data_fur]):
                                    T_IMPORT = [i for i in word_3_list if i in content]

                                    if T_IMPORT:
                                        print(T_IMPORT)
                                        all_at_company = [company[0] for company in all_data_fur]
                                        num = len((all_at_company))
                                        summary1 = [k for k in content_spilt for company in all_at_company if company in k][:num]
                                        summary_text1 = ''.join(summary1)+'。'
                                        company_tags = [i for i in all_at_company]
                                        if company_tags:
                                            all_tags = T_IMPORT
                                            all_tags_text = '|'.join(all_tags) + "({})".format('|'.join(list(set(company_tags))))
                                            sql3 = '''insert into hisinfo_cx(post_id,summary,post_type,key1,str_date,
                                                tags,media,media_channel,zjx_p) values (%s)''' % (S_conut)
                                            cur3.execute(sql3, (
                                            id_, summary_text1, post_type, key1_word, str_date, all_tags_text, all_data_fur[0][-1],
                                            all_data_fur[0][-1], 2))
                                            conn3.commit()
                                            print(T_IMPORT, company_tags,2222,summary_text1,all_tags)
                                            return 2

                    else:
                            hisinfo_sql2 = f'''select key1,category,summary,media from hisinfo_cx where
                                                       del_flag = 0 and post_id ={id_}'''  # 涉及到基金公司的sqland key1 in {name_list}
                            cur3.execute(hisinfo_sql2)
                            all_data_fur2 = cur3.fetchall()
                            if all_data_fur2:
                                summary_else = all_data_fur2[0][2]
                                media_else = all_data_fur2[0][-1]
                                sql = '''insert into hisinfo_cx(post_id,summary,post_type,key1,str_date,media,media_channel,add_report,zjx_p)
                                values (%s)''' % (S_conut)
                                cur3.execute(sql,( id_, summary_else, post_type, key1_word, str_date,media_else,media_else,Today_str,Today_str))
                                conn3.commit()
                                return Today_str
        except Exception as e:
            if e:
                return 0
        print(id_, '以输出', datetime.datetime.now())

# if __name__ == '__main__':
#     id_ = sys.argv[0]
#     get_content_api(id_)
#6939305
# 6924390

