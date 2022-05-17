# 这里是针对 GWBERT 的程序
整体程序基于BERT 发布的源码
由于GWBERT 在词表上进行了优化，这里需要对 tokenization 的部分进行修改
并在其他程序中稍加改动。
这里的tokenization_test1.py是在原始tokenization 的基础上修改得到代码，可以加载之前 生成的词汇表，并对所支持的语言根据词汇表的内容进行分词
其他程序加载了 tokenization_test1.py 
其中 run_classifier_archrihan.py 是针对四个语言的分类finetune 程序