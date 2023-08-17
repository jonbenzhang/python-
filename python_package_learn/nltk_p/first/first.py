# import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# a = nltk.pos_tag(["July"])
#
# if __name__ == '__main__':
#     print(a)
#     a = lemmatizer.lemmatize("went")
#     print(a)
# from nltk.stem import WordNetLemmatizer
#
# lemmatizer = WordNetLemmatizer()
#
# print(lemmatizer.lemmatize("needed"))
# print(lemmatizer.lemmatize("went"))
# print(lemmatizer.lemmatize("better", pos="a"))
# import inflect
#
# p = inflect.engine()
# print(p.present_participle('needed')) # need
"""
__author__:shuangrui Guo
__description__:
"""
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

wnl = WordNetLemmatizer()


# # 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
#
#
# # 分别定义需要进行还原的单词与相对应的词性
# words = ['cars', 'men', 'running', 'ate', 'saddest', 'fancier', "needed"]
# for i in range(len(words)):
#     print(words[i] + '--' + get_wordnet_pos(pos_tag([words[i]])[0][1]) + '-->' + wnl.lemmatize(words[i],
#                                                                                                get_wordnet_pos(
#                                                                                                    pos_tag([words[i]])[
#                                                                                                        0][1])))
# print(pos_tag(["needed"]))

import nltk
nltk.download('punkt')
a = "The link layer defines the networking methods within the scope of the local network link on which hosts communicate without intervening routers."
a = "This layer includes the protocols used to describe the local network topology and the interfaces needed to affect the transmission of Internet layer datagrams to next-neighbor hosts"
b = nltk.word_tokenize(a)
print(b)
# words = a.split()
# t = pos_tag(words)
# for i in t:
#     print(i)
