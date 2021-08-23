#!/usr/bin/env python
# coding=utf-8
import csv
import re
import demjson
from loguru import logger
import pymysql
from Semantic_processing import get_content

logger.add('runtime.log', format="{time} {level} {message}", filter="my_tags", level="INFO")


dbuser = 'julai01'
dbpass = 'Sh51785136@sh'
dbhost = '120.26.106.222'
dbname = 'jijin'

db = pymysql.connect(dbhost, dbuser, dbpass, dbname, charset='utf8')
cur = db.cursor()
simu_dict = {}
with open('data.txt','r',encoding='utf8') as f:
    read_data = eval(f.read())

    for item in read_data:


        for key,value in item.items():
            if '自有媒体' in value:
                del value['自有媒体']
            else:
                value = value
            if type(value) == dict:
                value_data = list(value.values())
                value_data = [i.split(',') for i in value_data]
                value_data = sum(value_data,[])

            else:
                value_data = value
            if any(i==key for i in ['行业标签关键词','持股标签关键词']):
                continue

            simu_dict[key] = value_data+ read_data[-2]['行业标签关键词']+ read_data[-1]["持股标签关键词"]


dbhost2 = '120.26.211.213'
dbuser2 = 'julai01'
passwd2 = 'Zycj@2020688'
dbname2 = 'wemedia'
conn2 = pymysql.connect(dbhost2, dbuser2, passwd2, dbname2, charset='utf8')
cur2 = conn2.cursor()


def text_mark(commnet_text):#百度api的情感正负面
    from aip import AipNlp
    APP_ID = '11688814'
    API_KEY = '67rU3I4pXY9ch1k2mB1FMzfB'
    SECRET_KEY = 'IP4givnVwb3yyS7L2S66OXEmX3hC8E2b'
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    commnet_text = commnet_text
    sentiment_text = client.sentimentClassify(commnet_text)
    positive_prob = sentiment_text.get("items")[0].get("positive_prob")  # 正面打分
    negative_prob = sentiment_text.get("items")[0].get("negative_prob")  # 负面打分
    sentiment = sentiment_text.get("items")[0].get("sentiment")  # 判断正负面情感

    print(commnet_text,positive_prob,negative_prob,sentiment)



def get_sysparam_info(category_input):
    get_key_sql = "select variable,info from sysparam where variable = %s"

    cur2.execute(get_key_sql,f'{category_input}_keywords')
    for line in cur2.fetchall():
        vari,keyword = line

        keys = [i for i in keyword.split(' ') if i
                !='']
        return keys

def get_fund_synonym(jijin):#得到基金相关的同义词
    sql = 'select variable,info from sysparam where variable = %s'
    cur2.execute(sql,f'tongyici{jijin}')
    line  = cur2.fetchone()
    variable, all_words = line
    combine_dict = {line.replace('==', '=').strip().split("=")[1]: line.replace('==', '=').strip().split("=")[0] for
                    line in all_words.split("/")
                    if len(line.replace('==', '=').strip().split("=")) == 2}
    return combine_dict

#优先判断负面文本
def check_neg_pos(content,score_info_dict,jj_name):

    negtive_count = ['']
    positive_count = ['']
    word_h = {'总经理认为',}#去除投研观点里面文本
    all_jijin_content = ''.join([i for i in content if jj_name in i and all(j not in i for j in  word_h)])
    score_2 = ['自己微信','ttanswer','财富号']

    if any(i in all_jijin_content for i in score_2):
        print(12345678981234)
        score = 2
        return score,negtive_count,positive_count

    else:
        # jl = [i for i in list(get_fund_synonym(jj_name).keys()) if '嘉实' not in i]

        for key,value in score_info_dict.items():

           #过滤出来同义词的两个
            if key == 'negative1':

                word_info = [re.sub(r'\[\[JJ\]\]|\[\[CP\]\]|\[\[GP\]\]|\[\[GS\]\]|\[\[JL\]\]|\*|\+|\[JJ\]\]', '', i) for
                             i in value]

                # content是涉及到相关基金公司的句子，用列表进行分隔
                confirm_sentence = sorted(set([info for info in word_info if len(info) >= 2]), key=len, reverse=True)
                title_score_ = [i for i in confirm_sentence if i in title and jj_name in title]
                if title_score_:
                    return -2,negtive_count,positive_count
                else:
                    if key == 'positive1':
                    # 区分一下标题和全文的
                        value = value
                        word_info = [re.sub(r'\[\[JJ\]\]|\[\[CP\]\]|\[\[GP\]\]|\[\[GS\]\]|\[\[JL\]\]|\*|\+|\[JJ\]\]', '', i)
                                     for
                                     i in value]

                        # content是涉及到相关基金公司的句子，用列表进行分隔
                        confirm_sentence = sorted(set([info for info in word_info if len(info) >= 2]), key=len,
                            reverse=True)

                        # 过滤出来同义词的两个

                        title_score_ = [i for i in confirm_sentence if i in title and jj_name in title]

                        if title_score_:
                            return 2,negtive_count,positive_count

                    negtive_counts = [i for i in confirm_sentence if i in all_jijin_content]
                    negtive_count.extend(negtive_counts)

            elif key == 'positive1':
                #区分一下标题和全文的
                value = value
                word_info = [re.sub(r'\[\[JJ\]\]|\[\[CP\]\]|\[\[GP\]\]|\[\[GS\]\]|\[\[JL\]\]|\*|\+|\[JJ\]\]', '', i) for
                                 i in value]
              #
              #       # content是涉及到相关基金公司的句子，用列表进行分隔
                confirm_sentence = sorted(set([info for info in word_info if len(info) >= 2]), key=len, reverse=True)


                positive_counts = [i for i in confirm_sentence if i in all_jijin_content]
                    #相同的词进行重复统计

                positive_count.extend(positive_counts)

        if len(negtive_count) > len(positive_count) and len(negtive_count)>=5:

            score = -2
        elif len(negtive_count) > len(positive_count) and 2<len(negtive_count)<5:

            score = -1
        elif len(negtive_count) < len(positive_count) and len(positive_count)>=5:
            score = 2
            # copy_end_tags.add('[@]')
        elif len(negtive_count) < len(positive_count) and 2 < len(positive_count) <5:
            score = 1
        else:
            score = 0
        return score,negtive_count,positive_count


def is_number(s):#判断字符串是否为数字
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

tags_key = ['M','H', 'J', 'T', 'A', 'S', 'B', 'Y', 'U', 'V', 'P', 'F', 'Z',
            'D', 'at', '*', '$', 'R', 'N', 'O', 'E', 'G','W','C','#']

dict_scores ={'negative1': '-1',
               'positive1': '1'}
#目前的postive和posttive3还没有用上



category_info_dict = {}#每个标签对应关键词
score_info_dict = {}#每个分数对应的关键词


for category in tags_key:
    category_info_dict[category] = get_sysparam_info(category)

for score_key,score_value  in dict_scores.items():
    score_info_dict[score_key] = get_sysparam_info(score_key)



def title_tags_(jijin,title):

    all_tags_ = set()
    category_words = category_info_dict
    for key,values in category_words.items():
        if values == None:
            continue
        value_list = [re.sub(r'\[\[.*?\]\]|\*|\+|\s+', '', i) for i in values if
                                           re.sub(r'\[\[.*?\]\]|\*|\+|\s+', '', i) not in  ['','规模']]

        tags = [j for j in value_list if j in title and '基金' in title]
        if key in ['$','E',]:
            if tags:
                print(tags,f'标题的{key}')
                all_tags_.add(f"[{key}]")
    word_title = ['发行','成立以来',]
    if jijin in title and any(i in title for i in word_title):
        all_tags_.add('[@]')
        all_tags_.add("[A]")
    word_title_w = ['直播',]
    if jijin in title and any(i in title for i in word_title_w):
        all_tags_.add('[@]')
        all_tags_.add("[W]")
    word_title2 = ['基金收评','超额收益','涨幅',]
    if any(i in title for i in word_title2) and jijin in title:
        all_tags_.add('[J]')
        all_tags_.add('[@]')
    word_title3 = ['一封信：', '：']
    #标题理出现：的语义顺序
    if any(i in title for i in word_title3) and jijin in title and all( i not in title for i in  ['重磅消息：','前董事长']):
        all_tags_.add('[H]')
        all_tags_.add('[@]')
    return all_tags_


def title_score(jijin,title,negtive_word):
    negtive_word_list = negtive_word.get('negative1')

    word_info = [re.sub(r'\[\[JJ\]\]|\[\[CP\]\]|\[\[GP\]\]|\[\[GS\]\]|\[\[JL\]\]|\*|\+|\[JJ\]\]', '', i) for i in negtive_word_list]
    word_info.extend(['离任','离职'])
    # content是涉及到相关基金公司的句子，用列表进行分隔
    confirm_sentence = sorted(set([info for info in word_info if len(info) >= 2]), key=len, reverse=True)
    print(confirm_sentence,11234567)
    # for i in confirm_sentence:
    #     if i in title:
    #         print(i,2222222222222211111111111111)
    if any(i in title and jijin in title for i in confirm_sentence):
        score = '-2bt'
        print(score,12653412)
        return score
    positive_word_list = negtive_word.get('positive1')
    word_info = [re.sub(r'\[\[JJ\]\]|\[\[CP\]\]|\[\[GP\]\]|\[\[GS\]\]|\[\[JL\]\]|\*|\+|\[JJ\]\]', '', i) for i in
                 positive_word_list]

    # content是涉及到相关基金公司的句子，用列表进行分隔
    confirm_sentence = sorted(set([info for info in word_info if len(info) >= 2]), key=len, reverse=True)
    print(confirm_sentence,123456781)
    if any(i in title and jijin in title for i in confirm_sentence):
        print(12345678912)
        score = '2bt'
        return score
    else:
        return None


def tags_write(jijin,title,content,all_content,text_all):

    jijin_num = ''.join(text_all).count(jijin)

    copy_end_tags = set()
    exclude_h_sentence_list = []
    M_exclude_sentence = []
    all_h_sentence = []
    category_words = category_info_dict

    title_tag = title_tags_(jijin,title)
    copy_end_tags.update(title_tag)

    for sentence in content:
        h_sentence = ['投资中最简单的事']
        if any(i in sentence for i in h_sentence):
            copy_end_tags.add('[H]')

        exclude_sentence = ['风险提示：','财富产品','免责声明']
        if any(i in sentence for i in exclude_sentence):
            continue
        deflaut_tag = ['调研']
        not_deflaut_tag = ["调研体系"]
        if any(i in sentence for i in deflaut_tag) and not any(i in sentence for i in not_deflaut_tag):

            copy_end_tags.add('[T]')
            continue
        m_author = ['LZ']
        if any(i in sentence for i in m_author):
            print(sentence,'MMMMMMMMMMMMMMMMMMM人名')
            copy_end_tags.add('[M]')
            continue
        # if jijin in sentence:

        for key,values in category_words.items():

            #key对应的标签的字母
            if values ==None:
                continue
            value_list = [re.sub(r'\[\[.*?\]\]|\*|\+|\s+', '', i) for i in values if
                     re.sub(r'\[\[.*?\]\]|\*|\+|\s+', '', i) != '']
            value_single = set(value_list)#把关键词进行去重
            if  key == 'M':

                GS_words = ['[[GS]]+' + i for i in value_single]
                # M_word = ['曾','先后','公奔私','去职','原基金经理']
                M_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                              j.split('+')[1] in sentence]

                if M_sentence:# and jijin_num ==1
                    print(M_sentence, 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
                    key = 'M'
                    copy_end_tags.add(f'[{key}]')
                    M_exclude_sentence.append(sentence)

            if  sentence in M_exclude_sentence:
                continue

            if key == 'Z':
                if '[[GG]]' in sentence:
                    key = 'Z'
                    copy_end_tags.add(f'[{key}]')
            if key == 'H':#优先去判断H,排除h里面的词的干扰
                value_single = value_single.union({'圆桌论坛'})
                exclude_word = ['可以说','分析师','资料介绍']
                #H的判断进行主谓宾的判断13622965
                if any (i in sentence for i in exclude_word):#把这些字应该扣掉而不是直接去跳过
                    continue
                #公司说去掉
                GS_JL_words = ['[[JL]]+[[GS]]+[[GG]]+'+i for i in value_single]

                sentence_split = sentence.split("，")#对每句话进行切分编程列表形式


                # exclude_h_sentence = [index_ for index_,i in enumerate(sentence_split) for value_info in
                #                       GS_JL_words if (value_info.split('+')[0] in i or value_info.split('+')[1] in i )
                #                       and value_info.split('+')[2] in i]
                #+''.join(sentence_split[index_:index_+1])
                exclude_jg_sentence = [single_sen for index_,single_sen in enumerate(sentence_split)
                                       if '[[GS]]' in single_sen or '[[JL]]' in single_sen or '[[GG]]'in single_sen]##
                exclude_jg_sentence= [i[i.find(j):i.find(j)+38] for i in exclude_jg_sentence for j in ['[[GG]]','[[JL]]','[[GS]]'] if i.find(j)!=-1]
                print(exclude_jg_sentence,123123123111)
                ###exclude_jg_sentence对句子进行筛选把符合有[[]]标志的分段式

                exclude_h_sentence = [(sentence.find(value_info.split('+')[3]),value_info) for index_, i in enumerate(exclude_jg_sentence) for value_info in
                                                            GS_JL_words if (value_info.split('+')[0] in i or value_info.split('+')[1] in i or value_info.split('+')[2] in i)
                                                            and value_info.split('+')[3] in i]#12


                if exclude_h_sentence:
                    print(exclude_h_sentence,'HHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
                    exclude_h_sentence_list.append(sentence)
                    exclude_h_num = min([i[0] for i in exclude_h_sentence])#取得每句话投研当中最小的位置
                    remaining_sentence = sentence[:exclude_h_num]#获取投研观点的前面句子

                    all_h_sentence.append(remaining_sentence)

                    real_tags = f'[H]'
                    copy_end_tags.add(real_tags)
                    copy_end_tags.add('[@]')

                    if '[[GG]]' in sentence:
                        copy_end_tags.add('[Z]')
                jl_gg_h = ['[[JL]]：', '[[GG]]：','[[GS]]：']
                exclude_gg_h = ["[[GS]]：[[JL]]"]
                if any(i in sentence for i in jl_gg_h) and \
                        not any(i in sentence for i in exclude_gg_h):

                    real_tags = f'[H]'
                    copy_end_tags.add(real_tags)
                    copy_end_tags.add('[@]')
                    if '[[GG]]' in sentence:
                        copy_end_tags.add('[Z]')
                    exclude_h_sentence_list.append(sentence)
            if sentence in exclude_h_sentence_list:

                continue

            # sentence = sentence.replace(remaining_sentence,"")
            # print(sentence,1234567890)

            # print(all_h_sentence,'所有的h的句子')
            # sentence = sentence+''.join(all_h_sentence)
            # print(sentence,'剩余的句子....')
            if key == 'W':
                w_exclude_word = ['营销市场','营销服务']
                if any(i in sentence for i in w_exclude_word):
                    continue
                GS_words = ['[[GS]]+[[JL]]+' + i for i in value_single]
                W_sentence = [(sentence,j) for j in GS_words if (j.split('+')[0] in sentence or
                                                             j.split('+')[1] in sentence) and j.split('+')[
                                  2] in sentence]
                print(W_sentence,'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
                if W_sentence:
                    key = 'W'

                    copy_end_tags.add(f'[{key}]')


            if key == 'E':
                E_exclude_sentence = ["含定投"]
                if any(i in sentence for i in E_exclude_sentence):
                    continue
                GS_words = ['[[GS]]+[[CP]]+' + i for i in value_single]
                W_sentence = [(sentence,j) for j in GS_words if (j.split('+')[0] in sentence or
                                                             j.split('+')[1] in sentence) and j.split('+')[
                                  2] in sentence]
                print(W_sentence,'EEEEEEEEEEEEEEEEEEEEEEEEEEE')
                if W_sentence:
                    key = 'E'

                    copy_end_tags.add(f'[{key}]')
                if '、' in sentence:
                    nums = re.search(r'(.*?)、', sentence).group(1)

                    if nums:

                        is_num = is_number(nums.strip())
                        for i in value_single:

                            if i in all_content and is_num:
                                key = 'E'

                                copy_end_tags.add(f'[{key}]')


            if key == 'R':

                GS_words = ['[[GS]]+[[JL]]+' + i for i in value_single]
                R_sentence = [(sentence,j) for j in GS_words if (j.split('+')[0] in sentence or
                                                                 j.split('+')[1] in sentence) and j.split('+')[
                                   2] in sentence]
                print(R_sentence,'RRRRRRRRRRRRRRRRRRRRRRRR')
                if R_sentence:
                    key = 'R'
                    copy_end_tags.add(f'[{key}]')
            if key == '*':

                GS_words = ['[[GS]]+[[CP]]+' + i for i in value_single]
                R_sentence = [(sentence, j) for j in GS_words if (j.split('+')[0] in sentence or
                                                                  j.split('+')[1] in sentence) and j.split('+')[
                                  2] in sentence]
                print(R_sentence, '***********************')
                if R_sentence:
                    key = '*'
                    copy_end_tags.add(f'[{key}]')
            if key =='V':
                GS_words = ['[[GS]]+' + i for i in value_single]
                GS_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                               j.split('+')[1] in sentence]
                print('VVVVVVVVVVV',GS_sentence)
                if GS_sentence:
                    key = '[V]'
                    copy_end_tags.add(key)
            if key =='G':
                GS_words = ['[[GS]]+[[CP]]+' + i for i in value_single]
                print(GS_words,2222222222222222222222)
                G_sentence = [(sentence, j) for j in GS_words if (j.split('+')[0] in sentence or
                                                                  j.split('+')[1] in sentence) and j.split('+')[
                                  2] in sentence]
                print(G_sentence,'ggggggggggggggggggggggggggggggggggggggggggggggg')
                if G_sentence:
                    key = '[G]'
                    copy_end_tags.add(key)


            if key=='B':

                GS_words = ['[[GS]]+' + i for i in value_single]
                find_cp_num = sentence.find("[[CP]]")
                exclude_word = ['基金净值']

                exclude_cp_sentence = sentence[:find_cp_num]
                if '[[GS]]' in exclude_cp_sentence and any(i in sentence for i in exclude_word):
                    continue
                GS_sentence =  [(sentence,j) for j in GS_words if j.split('+')[0] in sentence and
                                j.split('+')[1] in sentence]
                print(GS_sentence,'BBBBBBBBBBBBBBBBBBBBBBBB')
                if GS_sentence:
                    key = 'B'
                    copy_end_tags.add(f'[{key}]')
                else:
                    GS_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                                   j.split('+')[1] in sentence]
                    if GS_sentence:
                        key = 'B'
                        copy_end_tags.add(f'[{key}]')
            if  key == 'F':
                value_single = value_single.union({'首家百亿私募','老牌私募','股票类百亿私募'})
                GS_words = ['[[GS]]+[[CP]]+' + i for i in value_single]

                F_sentence = [(sentence, j) for j in GS_words if (j.split('+')[0] in sentence or
                                                                  j.split('+')[1] in sentence) and j.split('+')[
                                  2] in sentence]

                if F_sentence:
                    key = 'F'
                    copy_end_tags.add(f'[{key}]')
            if key == 'at':
                value_single = value_single.union({'圆桌论坛','澄清'})
                GS_JL_words = ['[[JL]]+[[GS]]+' + i for i in value_single]
                AT_sentence = [(sentence,j) for j in GS_JL_words if (j.split('+')[0] in sentence or
                               j.split('+')[1] in sentence) and j.split('+')[2] in sentence]
                print(AT_sentence,'@@@@@@@@@@@@@@@@@@@@@@')
                if AT_sentence :
                    key = '@'

                    copy_end_tags.add(f'[{key}]')


            if key == 'O':
                pass

            if key == 'U':

                u_exclude_word = ["募集规模", '发行规模','募集规模上限','[[GS]]：[[JL]]']
                # if any(i in sentence for i in a_exclude_word):
                #     continue
                sentence_u_split = [i for i in sentence.split("，") if not any(j in i for j in u_exclude_word)]
                sentence_u_split_text = ''.join(sentence_u_split)
                GS_words = ['[[GS]]+' + i for i in value_single]

                GS_sentence = [(sentence_u_split_text,j) for j in GS_words if j.split('+')[0] in sentence_u_split_text and
                               j.split('+')[1] in sentence_u_split_text]
                print(GS_sentence,'UUUUUUUUUUUUUUUUUUUUUU')
                if GS_sentence:
                    key = 'U'
                    copy_end_tags.add(f'[{key}]')
            if key == 'J':

                exclude_word = ['任职以来','占比']
                if any(i in sentence for i in exclude_word):
                    continue
                CP_words = ['[[CP]]+' + i for i in value_single]
                if 'NUMBER%' in sentence:


                    CP_sentence = [(sentence,j) for j in CP_words if j.split('+')[0] in sentence and
                                   j.split('+')[1] in sentence[sentence.find(j.split('+')[0]):]]
                    print(CP_sentence,'jjjjjjjjjjjjjjjj')
                    include_word = ["基金净值",'产品']

                    CP_sentence2 = [(sentence,i) for i in value_single if i in sentence[sentence.find('[[GS]]'):] and '[[GS]]' in sentence and
                                    any(i in sentence[sentence.find('[[GS]]'):] for i in include_word)]
                    print(CP_sentence,CP_sentence2,'JJJJJJJJJJJJJJJJJJJJJJJJJ')
                else:
                    CP_sentence = [(sentence, j) for j in CP_words if j.split('+')[0] in sentence and
                                   j.split('+')[1] in sentence]
                    print(CP_sentence, 'jjjjjjjjjjjjjjjj')
                    include_word = ["基金净值", '产品']

                    CP_sentence2 = [(sentence, i) for i in value_single if
                                    i in sentence and '[[GS]]' in sentence and
                                    any(i in sentence for i in include_word)]

                if CP_sentence:
                    key = 'J'
                    copy_end_tags.add(f'[{key}]')
                elif CP_sentence2:
                    print(CP_sentence2,'j2')
                    key = 'J'
                    copy_end_tags.add(f'[{key}]')
            if key == 'S':

                CP_words = ['[[CP]]+' + i for i in value_single]

                CP_sentence = [(sentence,j) for j in CP_words if j.split('+')[0] in sentence and
                               j.split('+')[1] in sentence]
                CP_sentence2 = [(sentence,i) for i in value_single if
                                i in sentence and '[[GS]]' in sentence and '产品' in sentence]

                if CP_sentence:
                    key = 'S'
                    copy_end_tags.add(f'[{key}]')
                elif CP_sentence2:
                    key = 'S'
                    copy_end_tags.add(f'[{key}]')
                S_word = '产品数量 净申购 净赎回 申购资金 一日售罄 日光 流动性 持有人户数 流通份额 募集多少亿 卖了多少亿 发行规模 募资 认购总规模 大卖超过 募集告罄 爆款 吸金达 限售额 大卖超 认购超 申购金额 申购总额 募集接近 这只规模 规模新基金'.split(" ")
                if '[[GS]]' in sentence and any(i in sentence for i in S_word):
                    key = 'S'
                    copy_end_tags.add(f'[{key}]')

            if key == 'A':

                exclude_a = '成立来|成立以来'
                sentences = re.sub(exclude_a,'',sentence)
                a = value_single
                a.add('备案')
                'NUMBER年NUMBER月NUMBER日 NUMBER月NUMBER日'
                sence_list = [i for i in a if i in sentences ]
                if sence_list:
                    print(sence_list,12345678909)
                    num_sen = [sentences.find(i,0) for i in ['[[CP]]','[[GS]]','[[JL]]']]
                    print(num_sen,1234)
                    if -1 in num_sen:
                        num_sen = set(num_sen)
                        num_sen.discard(-1)
                        if not num_sen:
                            continue
                    else:
                        num_sen = num_sen

                    print(num_sen,1234412,sentence[min(num_sen):])
                    shengxia_sen = [i for i in a if i in sentences[min(num_sen):]]
                    print(shengxia_sen,123455342)
                    if shengxia_sen:
                        key = 'A'
                        copy_end_tags.add(f'[{key}]')
                    #
                    # else:
                    #     a_exclude_word = ["成立以来",'新基金经理','NUMBER年NUMBER月NUMBER日','NUMBER月NUMBER日']
                    #     sentence_a_split = [i for i in sentences.split("，") if not all(j in i for j in a_exclude_word)]
                    #     sentence_a_split_text = ''.join(sentence_a_split)
                    #
                    #
                    #     GS_JL_words = ['[[CP]]+[[GS]]+' + i for i in value_single]
                    #     print('基金发行的A文本判断')
                    #     A_sentence = [(sentence_a_split_text,j) for j in GS_JL_words if (j.split('+')[0] in sentence_a_split_text or
                    #                                                      j.split('+')[1] in sentence_a_split_text) and j.split('+')[
                    #                        2] in sentence_a_split_text]
                    #
                    #     print('AAAAAAAAAAAAAAAA',A_sentence)
                    #
                    #     if A_sentence:
                    #         key = 'A'
                    #         copy_end_tags.add(f'[{key}]')
                        # else:
                        #     print(111111111111111111111122222222222222333333333333333311111111111111)
                        #     a_sentence = [i[i.find(j):]
                        #     for i in exclude_jg_sentence for j in['[[GG]]', '[[JL]]', '[[GS]]'] if i.find(j) != -1]
                        #     A_sentence = [i for i in a_sentence if any(j in i  for j in ['NUMBER年NUMBER月NUMBER日','NUMBER月NUMBER日','发行','募集'] )
                        #                   ]
                        #     if A_sentence:
                        #         copy_end_tags.add(f'[{key}]')

            if  key == 'C':
                GS_words = ['[[CP]]+' + i for i in value_single]

                Y_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                              j.split('+')[1] in sentence]
                print(Y_sentence, 'CCCCCCCCCCCCCCCCCCCC')
                if Y_sentence:
                    key = 'C'
                    copy_end_tags.add(f'[{key}]')
            if key == '#':
                value_single = value_single.union({'持仓','风口浪尖','辟谣', '谣言',
                                    '此地无银', '隐情','腰斩','赌博', '损失惨重', '违规减持', '联合坐庄', '蹊跷' ,'风暴眼' ,'澄清'})

                if any(i in sentence for i in  ['自己微信', 'ttanswer', '财富号']):
                    continue
                GS_words = ['[[CP]]+[[GS]]+[[JL]]+' + i for i in value_single]

                Y_sentence = [(sentence, j) for j in GS_words if (j.split('+')[0] in sentence or
                                                                  j.split('+')[1] in sentence or j.split('+')[2]) and j.split('+')[
                                  3] in sentence ]
                print(Y_sentence, '#################')
                if Y_sentence:
                    key = '#'
                    copy_end_tags.add(f'[{key}]')

            if key == 'T':
                value_single.union({'调研','吸引','持仓','打新','减持','调仓换股','定增'})

                GS_JL_words = ['[[GS]]+' + i for i in value_single]

                T_sentence = [(sentence,j) for j in GS_JL_words if j.split('+')[0] in sentence and
                                                                 j.split('+')[1] in sentence ]
                print(T_sentence,'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
                if T_sentence:
                    key = 'T'
                    copy_end_tags.add(f'[{key}]')
                t_sentence = [i for i in ['[[CP]]',] if i in sentence and '万股' in sentence and any(i in sentence for i in ('持股','持有'))]
                if t_sentence:
                    key = 'T'
                    copy_end_tags.add(f'[{key}]')

                T_word = ['持仓基金','持仓','重仓股']
                if any(i in sentence and '[[CP]]' in sentence for i in T_word):
                    key = 'T'
                    copy_end_tags.add(f'[{key}]')

            if key == 'Y':
                value_single.add('合作机构')
                GS_words = ['[[GS]]+' + i for i in value_single]

                Y_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                               j.split('+')[1] in sentence]
                print(Y_sentence,'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
                if Y_sentence:
                    key = 'Y'
                    copy_end_tags.add(f'[{key}]')
            if key == 'D':

                GS_words = ['[[GS]]+' + i for i in value_single]

                Y_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                              j.split('+')[1] in sentence]
                print(Y_sentence, 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
                if Y_sentence:
                    key = 'D'
                    copy_end_tags.add(f'[{key}]')

            if key == 'P':

                print(sentence, 3451123)
                GS_words = ['[[JL]]+' + i for i in value_single]

                P_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                              j.split('+')[1] in sentence]
                print(P_sentence, 'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
                if P_sentence:
                    key = 'P'
                    copy_end_tags.add(f'[{key}]')


            if key == 'D':

                GS_words = ['[[JL]]+' + i for i in value_single]

                P_sentence = [(sentence, j) for j in GS_words if j.split('+')[0] in sentence and
                              j.split('+')[1] in sentence]
                if P_sentence:
                    key = 'R'
                    copy_end_tags.add(f'[{key}]')
            if key == 'N':
                N_exclude_word = ["养老首席"]
                if any(i in sentence for i in N_exclude_word):
                    continue
                GS_words = ['[[GS]]+[[CP]]+' + i for i in value_single]

                N_sentence = [(sentence, j) for j in GS_words if (j.split('+')[0] in sentence or
                                                                  j.split('+')[1] in sentence) and j.split('+')[
                                  2] in sentence]
                if N_sentence:
                    key = 'N'
                    copy_end_tags.add(f'[{key}]')
            if key == '$':

                GS_words = ['[[CP]]+[[GS]]+' + i for i in value_single]#加上公司的标志
                layer_sentence = all_content.index(sentence)
                print(layer_sentence,12345678)
                if layer_sentence == 0:
                    start_ = layer_sentence
                else:
                    start_ = layer_sentence-1
                print(all_content[start_:layer_sentence+1],start_)
                all_tuijian_content = ''.join(all_content[start_:layer_sentence+2])
                print(all_tuijian_content,111111111111111111111222222222222333333333)
                S_sentence =  [(all_tuijian_content,j) for j in GS_words if (j.split('+')[0] in all_tuijian_content or j.split('+')[
                                   1] in all_tuijian_content) and j.split('+')[2] in all_tuijian_content]
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$',S_sentence)
                if S_sentence:
                    key = '$'
                    copy_end_tags.add(f'[{key}]')
                if '、' in sentence:
                    nums = re.search(r'(.*?)、', sentence).group(1)

                    if nums:

                        is_num = is_number(nums.strip())
                        for i in value_single:

                            if i in all_content and is_num:
                                print(nums, sentence, '$$$$$$$$$$$$$$111!1')
                                key = '$'

                                copy_end_tags.add(f'[{key}]')


    return copy_end_tags


jijin_list = ('景顺长城',)
# jijin_list =('国海富兰克林','嘉实','中银','中邮','长信','富安达','富国','汇添富','华夏','南方','国寿安保','天弘','博时','易方达','鹏华','新华','银华', '交银' ,'大成' ,'汇丰晋信','中信保诚' ,'博时' ,'建信' ,'华宝', '招商' ,'广发', '上投摩根', '中融', '工银瑞信' ,'华泰柏瑞', '中欧' ,'前海开源', '汇添富', '东证资管', '兴全' ,'华商', '国泰' ,'华安' ,'平安','农银汇理'  ,'海富通' ,'光大保德信', '摩根士丹利华鑫', '华商','民生加银')
#jingshun8920332,兴业12740731
for jj_name in jijin_list:#获取同义词
    jijin_synonym_dict = {}
    jijin_synonym_dict[jj_name] = get_fund_synonym(jj_name)

    content_item = get_content(cur,jijin_synonym_dict,jj_name)

    for con_info in content_item:
        try:
            id_,date,cate,score,content,media_channel,title,link,\
            total_sentence,jijin,textlist,text_all,summary,media,post_type,contentes=con_info
            jj_count = content.count("[[GS]]")

            if '公告' in title :
                continue

            if media == '金融界'  and ( '请保持关注' in title or '最新净值' in title):

                continue
            title_score_result = title_score(jijin,title,score_info_dict)

            check_neg_pos_score,negtive_count,postive_count = check_neg_pos(text_all, score_info_dict, jj_name)

            tags_reslut = tags_write(jijin, title, content,textlist,text_all)

            jijin_count = ''.join(text_all).count(jijin)

            tags_reslut = ''.join(tags_reslut)

            if title_score_result == '-2bt' or check_neg_pos_score in (-2,-1):

                if title_score_result == '-2bt':
                    check_neg_pos_score =-2
                else:
                    check_neg_pos_score = check_neg_pos_score
                tags_reslut = re.sub(r'\[H\]|\[@\]|\[\$\]|\[E\]','',tags_reslut)

            elif  title_score_result =='2bt':

                if '@' not in tags_reslut:
                    tags_reslut = tags_reslut+'[@]'

            # elif check_neg_pos_score == 2:
            #     tags_reslut = tags_reslut + '[@]'
            else:
                tags_reslut = tags_reslut
            count_tags = len(tags_reslut.split(']'))

            if  all(i in tags_reslut for i in ['[A]', '[S]']) and count_tags ==3\
                    or all(i in tags_reslut for i in ['[A]', '[S]','[$]']) and count_tags ==4:

                check_neg_pos_score = 1
            if ('[$]' in tags_reslut and count_tags==3) or tags_reslut == '[$]':

                check_neg_pos_score =1

            if  all(i in tags_reslut for i in ['[@]', '[H]']) and count_tags ==3:

                check_neg_pos_score = 1
            if all(i in tags_reslut for i in ['[A]', '[S]']) and all(i not in tags_reslut for i in ['[@]', '[H]','[$]',]) and \
                check_neg_pos_score !=-2 and title_score_result != '-2bt':

                check_neg_pos_score = 1
            else:
                if jijin_count > 2 and all(i in tags_reslut for i in ['[A]', '[S]', '[@]']) and count_tags >= 4:

                    check_neg_pos_score =2
                if  all(i ==tags_reslut for i in ['[A]','[@]']) and jijin in title and \
                check_neg_pos_score !=-2 and title_score_result != '-2bt':

                    check_neg_pos_score = 2

                if ('@' in tags_reslut or 'H' in tags_reslut) and (jijin in title or count_tags > 5):

                    check_neg_pos_score = 2

                else:
                    if   jijin in title and any (i in title for i in '发行 获准 注册 成立 募集 成立 NUMBER年NUMBER月NUMBER日 NUMBER月NUMBER日'.split(" ")) and \
                check_neg_pos_score !=-2 and title_score_result != '-2bt':

                        check_neg_pos_score = 2
                    elif ('$' in tags_reslut and 'E' in tags_reslut and 'A' in tags_reslut) and  check_neg_pos_score in (0,-1,-2):
                        print(12344444444444444441111111111)
                        check_neg_pos_score = 1
                    elif ('@' in tags_reslut or 'H' in tags_reslut) and  check_neg_pos_score in (0,-1,-2):
                        print(2345123)
                        check_neg_pos_score = 1
                    elif tags_reslut == '[A]' and check_neg_pos_score!=-2 :
                        print(1111111111111111222231231)
                        check_neg_pos_score = 1
                    #统计全部的公司的次数超过5次
                    elif jijin in media:
                        print(1111111111122222222211111111)
                        check_neg_pos_score = 2
                        tags_reslut = tags_reslut.replace('[@]','')+'[@]'
                # elif ('@' in tags_reslut or 'H' in tags_reslut) and jijin in title:
                #     check_neg_pos_score = 2
                # #分数的函数调用
                # #
                if jijin_count ==1 and all(i not in tags_reslut for i in ['[@]','[H]','[$]']) and title_score_result != '-2bt':

                    check_neg_pos_score = 0
                if jijin_count >4 and any(i  in tags_reslut for i in ['[@]','[H]','[$]']) and count_tags >=4 :

                    print(11111111111122222222111)
                    check_neg_pos_score = 2
            if  tags_reslut == '[#]' and title_score_result != '-2bt':
                check_neg_pos_score = 0
            if  '[#]' in tags_reslut and 1<len(negtive_count)<=3:
                tags_reslut = re.sub(r'\[H\]|\[@\]|\[\$\]|\[E\]', '', tags_reslut)
                check_neg_pos_score =-1
            if '[#]' in tags_reslut and len(negtive_count) > 3:
                tags_reslut = re.sub(r'\[H\]|\[@\]|\[\$\]|\[E\]', '', tags_reslut)
                check_neg_pos_score = -2
            if '[#]' in tags_reslut and len(negtive_count) ==1 :
                tags_reslut = re.sub(r'\[H\]|\[@\]|\[\$\]|\[E\]', '', tags_reslut)
                check_neg_pos_score = 0
            if '[M]' in tags_reslut and '[@]' in tags_reslut:
                tags_reslut = re.sub(r'\[M\]', '', tags_reslut)
            # if any(i in title for i in ['的基金经理','新增基金经理']):
            #     check_neg_pos_score = 0
            #     tags_reslut = '[#][R]'

            content =     contentes

            tags_word_simu = simu_dict.get(jijin)
            tags_word_simu.append("韩海峰")



            all_tags = [tags_info for tags_info in tags_word_simu if tags_info in content]
            tags_text = '|'.join(all_tags)
            text_gy = '''GY、GY被查、冯柳被查、冯柳谣言被查、冯柳传言被查、冯柳传闻被查、冯柳谣言被调查、冯柳传言被调查、冯柳传闻被调查、冯柳百亿重仓股暴跌、高毅虚假消息、被查谣言、高毅被调查、高毅传言被查、高毅资产被查、高毅资产被调查、高毅资产传言被调查、高毅传闻被查、千亿私募被调查、违规、网传被查、高毅谣言被查、高毅资产谣言被查、世纪华通、同仁堂、抄作业、冯柳罕见发微博、公司也急了、被查、千亿资管公司被查、回应被查传闻、辟谣、回应、澄清、谣言'''
            text_gy_list = text_gy.split('、')
            all_tags_gy = [tags_info for tags_info in text_gy_list if tags_info in content]
            if all_tags_gy:
                tags_text = tags_text+'|GY'

            # if  cate != '':
            #     if cate[-1] in ['.',']']:
            #         tags_reslut = tags_reslut
            # if  cate == '':
            #     tags_reslut = tags_reslut
            # else:
            #     tags_reslut = cate
            if tags_reslut =='':
                tags_reslut = '[]'
            else:
                tags_reslut = tags_reslut
            sql = '''update hisinfo_cx set tags = '{0}' where id = {1}'''.format(tags_text,id_)
            print(sql)
            cur.execute(sql)
            db.commit()
        except Exception as e:
            print(e)

    #
    # def check_neg_pos_baidu(commnet_text, meida, jj_name):
    #     neg_pos_dict = {}
    #     from aip import AipNlp
    #     APP_ID = '22516417'
    #     API_KEY = 'nElswzUEh191WRuMLSCBn6rc'
    #     SECRET_KEY = 'vfspaXFbEcwvSygw74ErZ83MkWzq1yD4'
    #     client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    #     all_text = ''.join(commnet_text)
    #     print(meida, jj_name, 1111111111111111111111112222222222222222222222222555555555555555)
    #     if any(i in all_text for i in ["自己微信", 'ttvideo']) or any(i in meida for i in ['理财嘉', jj_name]):
    #         return 21
    #     else:
    #         for item in commnet_text:
    #             item = item.encode("gbk", 'ignore').decode("gbk", "ignore")[:800]
    #             sentiment_text = client.sentimentClassify(item)
    #
    #             positive_prob = sentiment_text.get("items")[0].get("positive_prob")  # 正面打分
    #             negative_prob = sentiment_text.get("items")[0].get("negative_prob")  # 负面打分
    #             sentiment = sentiment_text.get("items")[0].get("sentiment")  # 判断正负面情感
    #
    #             if positive_prob > negative_prob:
    #                 neg_pos_dict.setdefault('positive', []).append(1)
    #             elif negative_prob > positive_prob:
    #                 neg_pos_dict.setdefault('negative', []).append(1)
    #         if neg_pos_dict.get('negative') != None and neg_pos_dict.get("positive") != None:
    #             if len(neg_pos_dict.get('negative')) > len(neg_pos_dict.get("positive")):
    #                 return -1
    #             elif len(neg_pos_dict.get('negative')) < len(neg_pos_dict.get("positive")):
    #                 return 1
    #             else:
    #                 return 0
    #         if neg_pos_dict.get("positive") != None and neg_pos_dict.get('negative') == None:
    #             return 1
    #         else:
    #             return -1
