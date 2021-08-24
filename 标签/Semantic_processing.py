import re
import jieba
import time
# jieba.set_dictionary("dict.txt")
# jieba.initialize()
# jieba.load_userdict("all_jijin_words.txt")
import datetime

yesterday = datetime.date.today() + datetime.timedelta(-1)
yesterday = str(yesterday).replace('-','')
print(yesterday)

def rm_char(text):

    text_ = ''.join(re.findall(r'[\d+\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5]|\w+',text))

    return text_

def rm_token(words):
    words_list = list(words)
    stop_words = ['&','nbsp','《','》']
    words_list = [i for i in words_list if i not in stop_words]
    return words_list


def convert_text_to_wordlist(str_doc):
    text_ = ''.join(
        re.findall(r'[^x00-xff]',
            str_doc))

    word_list = rm_token(jieba.lcut(text_))
    return word_list

def multiple_replace(text, idict):
    if idict =={}:
        return  text
    else:
        rx = re.compile('|'.join(map(re.escape, idict)))

        def one_xlat(match):
            return idict[match.group(0)]

    return rx.sub(one_xlat, text)


def get_content(cur,tongyici,jijin_input):

    sql = f'''SELECT a.id, a.str_date, a.category, a.auto_scores, b.content,b.link, a.media_channel, b.title,a.key1,b.summary,a.media,a.post_type,a.reporter 
    FROM hisinfo_cx a INNER JOIN cx0308 b ON a.post_id = b.id
     WHERE   a.post_type <> 1 AND a.post_type<>15 AND a.post_type <> 5 and a.post_type <> 7 and a.post_type <> 20 and a.post_type <> 10 and a.del_flag = 0 
     AND a.key1 = '{jijin_input}' AND  a.str_date>=20210801 and a.id =	25511137 ORDER BY a.id DESC'''
    #a.category in ( '','[@]')
    cur.execute(sql)
    content_list = []
    for id, date, cate, score, content,link, media_channel, title, jijin, summary, media, post_type,reporter in cur.fetchall():

        content =re.sub(r'\s+|<.+?>|\[paper\]','',content)#对中文文本进行初步的清洗处理

        p = re.compile("\d+.\d+%|\d+%|排名第")
        tmp_text = p.sub("NUMBER%", content)#把涉及到%的数字进行替换
        s = re.compile("\d+年\d+月\d+日|\d+月\d+日")
        tmp_text = s.sub("NUMBER年NUMBER月NUMBER日", tmp_text)
        title =  s.sub("NUMBER年NUMBER月NUMBER日", title)

        # seg_list = convert_text_to_wordlist(tmp_text)
        # seg_list = tmp_text.split('。')

        #seg_list是对整个文本进行切词的结果，列表呈现出来.
        Tongyici_valve = tongyici[jijin]

        # final_sentence = [Tongyici_valve[word] if word in Tongyici_valve.keys() else word
        #                   for word in seg_list]
        # final_sentence = [ sentence.replace(key,word.replace("嘉实",'').strip())  for sentence in seg_list for  key,word in
        #                    Tongyici_valve.items() if key in sentence]

        word_replace_dict ={}
        for key,word in Tongyici_valve.items():
            if key == '':
                continue
            if key in tmp_text:

                word_replace_dict[key] = word.replace(jijin_input,'').strip()
        print(word_replace_dict,111111111234111111121)
        word_replace_dict.update({"风险提示":"。风险提示",'的洪流':"",})
        final_sentence = multiple_replace(tmp_text, word_replace_dict)
        print(final_sentence,1111111111111312)
        #自己微信去掉会打不上@
        textlist = final_sentence.replace(jijin_input,'[[GS]]').replace('[[GS]]自己微信','。[[GS]]自己微信')\
            .replace('[[GS]]分析师','[[GS]]').replace('[[GS]]ttvideo','。[[GS]]ttvideo')
        # if '。' in textlist :
        #     textlist = re.split(r'。', textlist)

        if any(i in textlist for i in ['?',"!",'？','！','；','！','。','；']):
            textlist = re.split("。|！|？|\?|！|!|；|；",textlist)
            print(textlist,11111111111111111111111666666666666666333333333333333)

        else:
            textlist = re.split(" ", textlist)

        print(textlist,2222222222221)
        #把基金以及嘉实基金词换成GS，同时把各个基金公司的产品换成CP
        text_ = [i for i in textlist if any(j in i for j in ['[[GS]]','[[CP]]','[[JL]]','[[GG]]'])]

        total_sentence = len(re.split(r'。', content))
        all_text_list = re.split(r'。', content)

        # text_ =  [textlist[index_-1:index_+1] if jijin in i and index_!=0
        #           else textlist[index_:index_+1] for index_,i in enumerate(textlist) if jijin in i]
        text_all = [i for i in all_text_list if jijin in i]
        # text_ = sum(text_,[])
        print(text_all,1111111111231,text_)
        content_list.append(
            [
                id,
                date,
                cate,
                score,
                text_,  # 涉及到基金公司的文本以句号分割
                media_channel,
                title,
                total_sentence,  # 总的句子数字
                jijin,
                textlist,  # 总共的句子文本
                text_all,
                summary,
                media,
                post_type,
                reporter
                # content
            ]
        )

    return content_list



