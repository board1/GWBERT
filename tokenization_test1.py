from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import random
from re import S, sub
import tokenization
import tensorflow as tf
import jieba

def seg_sentence_ch(sentence,wordlist,model,max_word_len=5):
    """
    model= 1 为正向，0为逆向
    """
    i = 0
    res = []
    while i < len(sentence):
        # if method == self.L or method == self.S:
        j_range = list(range(max_word_len, 0, -1)) if model == 0 else list(range(2, max_word_len + 1)) + [1]
        for j in j_range:
            if j == 1 or sentence[i:i + j] in wordlist:
                res.append(sentence[i:i + j])
                i += j
                break
    return res

# vocab_file='/data/zbh/bert_learn_token/learn_fenci/bert-master/vocab.txt'


# def mf_tokenizer(line,tokenizer):
#     vocab_new = '/data/zbh/wordsegment_allanguages/vocabulayr_forall/ri_word.txt'
#     word_list = []
#     f1 = open(vocab_new,'r',encoding='utf-8')
#     while True:
#         token = tokenization.convert_to_unicode(f1.readline())
#         if(not token):
#             break
#         token = token.strip()
#         word_list.append(token)

#     res = seg_sentence_ch(line,word_list,0)

#     subline_list = []
#     str1 = ''
#     for i in res:
        
#         if(i not in word_list):
#             str1 +=i
#         else:
#             if(str1!=''):
#                 subline_list.append(str1)
#             subline_list.append(i)
#             str1 = ''
#     if(str1!=''):
#         subline_list.append(str1)
#     tokens = []
#     for i in subline_list:
#         if(i not in word_list):
#             tokens.extend(tokenizer.tokenize(i))
#         else:
#             tokens.append(i)
#     return tokens


word_list_all = []
vocabulary_list = ['/data/zbh/wordsegment_allanguages/vocabulayr_forall/ri_word.txt',
'/data/zbh/wordsegment_allanguages/vocabulayr_forall/han_word.txt']
# vocab_new = '/data/zbh/wordsegment_allanguages/vocabulayr_forall/ri_word.txt'
for vocab_new in vocabulary_list:
    f1 = open(vocab_new,'r',encoding='utf-8')
    while True:
        token = tokenization.convert_to_unicode(f1.readline())
        if(not token):
            break
        token = token.strip()
        word_list_all.append(token)

word_list_all_dict = {}
for i in word_list_all:
    word_list_all_dict[i] = 1









def mf_tokenizer(line,tokenizer):
    res = seg_sentence_ch(line,word_list_all,0)

    subline_list = []
    str1 = ''
    for i in res:
        
        if(i not in word_list_all):
            str1 +=i
        else:
            if(str1!=''):
                subline_list.append(str1)
            subline_list.append(i)
            str1 = ''
    if(str1!=''):
        subline_list.append(str1)
    tokens = []
    for i in subline_list:
        if(i not in word_list_all):
            tokens.extend(tokenizer.tokenize(i))
        else:
            tokens.append(i)
    return tokens


def mf_tokenizer_dict(line,tokenizer):
    res = seg_sentence_ch(line,word_list_all,0)

    subline_list = []
    str1 = ''
    for i in res:

        try:
            xx1 = word_list_all_dict[i]
            if(str1!=''):
                subline_list.append(str1)
            subline_list.append(i)
            str1 = ''
        except:
            str1 +=i
            
    if(str1!=''):
        subline_list.append(str1)
    tokens = []
    for i in subline_list:
        try:
            xx1 = word_list_all_dict[i]
            tokens.append(i)
        except:
            tokens.extend(tokenizer.tokenize(i))
    return tokens




def mf_tokenizer_arch_zh(line,tokenizer): # 对中文的修改，采用dict的形式，减少list的检索时间
    
    res = jieba.lcut(line)
    tokens = res

    return tokens









vocab_ch = '/data/zbh/wordsegment_allanguages/vocabulayr_forall/zh_word.txt'
word_list_ch = {}
f1 = open(vocab_ch,'r',encoding='utf-8')
while True:
    token = tokenization.convert_to_unicode(f1.readline())
    if(not token):
        break
    token = token.strip()
    # word_list.append(token)
    word_list_ch[token] = 1

def mf_tokenizer_zh_mf1(line,tokenizer): # 对中文的修改，采用dict的形式，减少list的检索时间
    
    res = jieba.lcut(line)

    subline_list = []
    str1 = ''
    for i in res:
        try:
            x_temp = word_list_ch[i]
            str1 +=i
        except:
            if(str1!=''):
                subline_list.append(str1)
            subline_list.append(i)
            str1 = ''
    if(str1!=''):
        subline_list.append(str1)
    tokens = []
    for i in subline_list:

        try:
            x_temp = word_list_ch[i]
            tokens.append(i)
        except:
            tokens.extend(tokenizer.tokenize(i))

    return tokens




def mf_tokenizer_nblock(line,tokenizer):
    tokens1 = []
    line1 = line.split(' ')
    for i in line1:
        try:
            x1 = dict_vocab_block['i']
            tokens1.append(i)
        except:
            token_temp = tokenizer.tokenize(i)
            tokens1.extend(token_temp)
    if(tokens1 == ['']):
        tokens1 = []
    return tokens1
    

    # vocab_new = '/data/zbh/wordsegment_allanguages/vocabulayr_forall/zh_word.txt'
    # word_list = []
    # f1 = open(vocab_new,'r',encoding='utf-8')
    # while True:
    #     token = tokenization.convert_to_unicode(f1.readline())
    #     if(not token):
    #         break
    #     token = token.strip()
    #     word_list.append(token)
    # # res = seg_sentence_ch(line,word_list,0)
    # res = jieba.lcut(line)

    # subline_list = []
    # str1 = ''
    # for i in res:
        
    #     if(i not in word_list):
    #         str1 +=i
    #     else:
    #         if(str1!=''):
    #             subline_list.append(str1)
    #         subline_list.append(i)
    #         str1 = ''
    # if(str1!=''):
    #     subline_list.append(str1)
    # tokens = []
    # for i in subline_list:
    #     if(i not in word_list):
    #         tokens.extend(tokenizer.tokenize(i))
    #     else:
    #         tokens.append(i)
    # return tokens





def list2word(string_list,start,end):
    str1 = ''
    end = min(len(string_list),end)
    for i in range(start,end):
        str1 += string_list[i]+' '
    str1 = str1[0:-1]
    

    # print(str1)
    return str1

def seg_sentence_en(sentence,wordlist,model,max_word_len=5):
    """
    model= 1 为正向，0为逆向
    """
    i = 0
    res = []
    while i < len(sentence):
        # if method == self.L or method == self.S:
        j_range = list(range(max_word_len, 0, -1)) if model == 0 else list(range(2, max_word_len + 1)) + [1]
        for j in j_range:
            if j == 1 or list2word(sentence,i,i+j) in wordlist:
                res.append(list2word(sentence,i,i+j))
                i += j
                break
    return res

def mf_tokenizer_en(line,tokenizer):
    line=line.split(' ')
    vocab_new = '/data/zbh/bert_learn_token/learn_fenci/bert-master/word_dic_en.txt'
    word_list = []
    f1 = open(vocab_new,'r',encoding='utf-8')
    while True:
        token = tokenization.convert_to_unicode(f1.readline())
        if(not token):
            break
        token = token.strip()
        word_list.append(token)

    res = seg_sentence_en(line,word_list,0)
    subline_list = []
    str1 = ''
    for i in res:
        if(' 'not in i):
            str1 += i +' '
        else:
            if(str1!=''):
                str1 = str1[0:-1]
                subline_list.append(str1)
            subline_list.append(i)
            str1 = ''
    if(str1!=''):
        subline_list.append(str1)
    tokens = []
    for i in subline_list:
        if(i not in word_list):
            tokens.extend(tokenizer.tokenize(i))
        else:
            tokens.append(i)
    return tokens
        
    #     if(i not in word_list):
    #         str1 +=i
    #     else:
    #         subline_list.append(str1)
    #         subline_list.append(i)
    #         str1 = ''
    # tokens = []
    # for i in subline_list:
    #     if(i not in word_list):
    #         tokens.extend(tokenizer.tokenize(i))
    #     else:
    #         tokens.append(i)
    # return tokens
            


  
      

# line= '据悉，中国的三名航天员已经成功地完成了两次出舱任务。而保管好这个出舱航天服就是们需要进行的第一个准备。这个出舱航天服不同于一般的航天服，它们是用于出舱也就是不在空间站舱内会用的航天服，这个出舱航天服不是一次性的，可以多次使用，所以使用过后需要报管好。保管好之前需要对这个出舱航天服干燥，这样才能确保下一次上来的航天员能够更快地熟悉适应。'
# vocab_file = '/data/zbh/bert_learn_token/learn_fenci/bert-master/vocab.txt'




# tokenizer = tokenization.FullTokenizer(
#       vocab_file=vocab_file, do_lower_case=False)



# tokens = tokenizer.tokenize(line)


