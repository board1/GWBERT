
from ctypes import *


libFile = '/data/zbh/NLPIR/NLPIR/NLPIRSDK/NLPIR-ICTCLAS/lib/linux64/libNLPIR.so'

dll = CDLL(libFile)


def loadFun(exportName, restype, argtypes):
    global dll
    f = getattr(dll, exportName)
    f.restype = restype
    f.argtypes = argtypes
    return f


class ENCODING:
    GBK_CODE = 0  # 默认支持GBK编码
    UTF8_CODE = GBK_CODE + 1  # UTF8编码
    BIG5_CODE = GBK_CODE + 2  # BIG5编码
    GBK_FANTI_CODE = GBK_CODE + 3  # GBK编码，里面包含繁体字


class POSMap:
    ICT_POS_MAP_SECOND = 0  # 计算所二级标注集
    ICT_POS_MAP_FIRST = 1  # 计算所一级标注集
    PKU_POS_MAP_SECOND = 2  # 北大二级标注集
    PKU_POS_MAP_FIRST = 3  # 北大一级标注集
Init = loadFun('NLPIR_Init', c_int, [c_char_p, c_int, c_char_p])
Exit = loadFun('NLPIR_Exit', c_bool, None)

ParagraphProcess = loadFun('NLPIR_ParagraphProcess', c_char_p, [c_char_p, c_int])
FileProcess = loadFun('NLPIR_FileProcess', c_double, [c_char_p, c_char_p, c_int])
ImportUserDict = loadFun('NLPIR_ImportUserDict', c_uint, [c_char_p])
AddUserWord = loadFun('NLPIR_AddUserWord', c_int, [c_char_p])
SaveTheUsrDic = loadFun('NLPIR_SaveTheUsrDic', c_int, None)
DelUsrWord = loadFun('NLPIR_DelUsrWord', c_int, [c_char_p])
GetUniProb = loadFun('NLPIR_GetUniProb', c_double, [c_char_p])
IsWord = loadFun('NLPIR_IsWord', c_bool, [c_char_p])



if not Init(b'/data/zbh/NLPIR/NLPIR/NLPIRSDK/NLPIR-ICTCLAS/',ENCODING.UTF8_CODE,b''):
    print("Initialization failed!")
    exit(-111111)



def word_seg(str1):
    import re
    pattern = re.compile('\(.*?\)')
    # strt = u'哈说的好稍稍好的(dhasiodhasodhaosho)十四哦对哈死哦大哈'
    # print(pattern.search(str))

    # print(re.sub(pattern,'',str))
    # print(str1)
    str1 = re.sub(pattern,'',str1)
    str1 = str1.replace('/','')

    result =  ParagraphProcess(str1.encode('utf8'),0)
    return result.decode('utf8')


def word_seg_pos(str1,number):
    # prcal(year, w=0, l=0, c=6, m=3)
    print(str1)
    result = ParagraphProcess(str1.encode('utf8'),number)
    result = result.decode('utf8')
    result = result.split(' ')
    # result.remove('')
    # print(result)
    list1 = []
    list2 = []
    # print(result.split(' '))
    for i in result:
        # print(i)
        if(i == ''):
            continue
        # print(i.split('/'))
        try:
            x1,x2 = i.split('/')[0],i.split('/')[1]
            list1.append(x1)
            list2.append(x2)
        except:
            continue
        
    # print(list1,list2)
    return list1,list2



def word_seg_pos_str(str1,number): #清洗并进行词性标注
    import re
    pattern = re.compile('\(.*?\)')
    # strt = u'哈说的好稍稍好的(dhasiodhasodhaosho)十四哦对哈死哦大哈'
    # print(pattern.search(str))

    # print(re.sub(pattern,'',str))
    # print(str1)
    str1 = re.sub(pattern,'',str1)
    str1 = str1.replace('/','')
    result = ParagraphProcess(str1.encode('utf8'),number)
    result = result.decode('utf8')
    return result


def replace_the_result(result1):
    list1 = result1.strip().split(' ')
    strnomal = ''
    strblock = ''
    if(list1 == ['']):
        strnomal = '\n'
        strblock = '\n'
    else:
        for i in list1:
            
            temp = i.split('/')
            if(len(temp)==1):
                continue
            strnomal += temp[0] +' '
            if(temp[1] == 'nr' or temp[1]=='nrf'):
                strblock += '[nr]'+' '
            elif(temp[1] == 'm'):
                strblock += '[m]'+' '
            elif(temp[1] == 'ns'):
                strblock += '[ns]'+' '
            elif(temp[1] == 'nz'):
                strblock += '[nz]'+' '
            elif(temp[1] == 't'):
                strblock += '[t]'+' '
            else:
                strblock += temp[0] +' '

        strnomal = strnomal[0:-1]+'\n'
        strblock = strblock[0:-1]+'\n'
    # print(strblock,strnomal)
    return strblock



def block_result_replace_list(str1):
    import re
    pattern = re.compile('\(.*?\)')
    # strt = u'哈说的好稍稍好的(dhasiodhasodhaosho)十四哦对哈死哦大哈'
    # print(pattern.search(str))

    # print(re.sub(pattern,'',str))
    # print(str1)
    str1 = re.sub(pattern,'',str1)
    str1 = str1.replace('/','')
    result = ParagraphProcess(str1.encode('utf8'),1)
    try:
        result = result.decode('utf8')
    except:
        result = ''
    list1 = result.strip().split(' ')
    # strnomal = ''
    # strblock = ''
    block_list = []
    if(list1 == ['']):
        # strnomal = '\n'
        # strblock = '\n'
        block_list.append('\n')
    else:
        for i in list1:
            
            temp = i.split('/')
            if(len(temp)==1):
                continue
            # strnomal += temp[0] +' '
            if(temp[1] == 'nr' or temp[1]=='nrf'):
                # strblock += '[nr]'+' '
                block_list.append('[nr]')
            elif(temp[1] == 'm'):
                # strblock += '[m]'+' '
                block_list.append('[m]')
            elif(temp[1] == 'ns'):
                # strblock += '[ns]'+' '
                block_list.append('[ns]')
            elif(temp[1] == 'nz'):
                # strblock += '[nz]'+' '
                block_list.append('[nz]')
            elif(temp[1] == 't'):
                # strblock += '[t]'+' '
                block_list.append('[t]')
            else:
                # strblock += temp[0] +' '
                block_list.append(temp[0])

        # strnomal = strnomal[0:-1]+'\n'
        # strblock = strblock[0:-1]+'\n'
    return block_list



def nomal_list(str1):
    import re
    pattern = re.compile('\(.*?\)')
    # strt = u'哈说的好稍稍好的(dhasiodhasodhaosho)十四哦对哈死哦大哈'
    # print(pattern.search(str))

    # print(re.sub(pattern,'',str))
    # print(str1)
    str1 = re.sub(pattern,'',str1)
    str1 = str1.replace('/','')

    result =  ParagraphProcess(str1.encode('utf8'),0)
    try:
        result = result.decode('utf8')
    except:
        result = ''
    result = result.split(' ')
    result = [i for i in result if len(i)>0]
    print(result)
    return result





if __name__ == "__main__":

    p = "Test Article: 中国科学院计算技术研究所在多年研究基础上，耗时一年研制出了基于多层隐码模型的汉语词法分析系统 ICTCLAS(Institute of Computing Technology, Chinese Lexical Analysis System)，该系统的功能有：中文分词；词性标注；未登录词识别。分词正确率高达97.58%(最近的973专家组评测结果)，基于角色标注的未登录词识别能取得高于90%召回率，其中中国人名的识别召回率接近98%，分词和词性标注处理速度为31.5KB/s。ICTCLAS 和计算所其他14项免费发布的成果被中外媒体广泛地报道，国内很多免费的中文分词模块都或多或少的参考过ICTCLAS的代码。"
    # result = ParagraphProcess(p.encode('utf8'),POSMap.PKU_POS_MAP_FIRST)

    # # print(word_seg_pos(p,0))
    # print(word_seg_pos(p,1))
    # print(word_seg_pos(p,2))
    # print(word_seg_pos(p,3))

    # prcal(year, w=0, l=0, c=6, m=3)
    # result1 = word_seg_pos_str(p,1)
    # print(word_seg_pos_str(p,1))
    # replace_the_result(result1)
    print(word_seg(p))