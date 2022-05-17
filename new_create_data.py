from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import random
import tokenization_test1 as tokenization
import tensorflow as tf

f1 = open('/data/zbh/wordsegment_allanguages/all_language_seg/ch.txt','r',encoding='utf-8')
vocab_file = '/data/zbh/bert_learn_token/learn_fenci/bert-master/vocab.txt'
all_documents = [[]]
line = tokenization.convert_to_unicode(f1.readline())
line = line.strip()

tokenizer = tokenization.FullTokenizer(
      vocab_file=vocab_file, do_lower_case=True)
        

        # Empty lines are used as document delimiters
if not line:
    all_documents.append([])
tokens = tokenizer.tokenize(line)

print(tokens)
