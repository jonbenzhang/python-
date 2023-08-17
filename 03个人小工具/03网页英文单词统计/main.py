import nltk
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
import inflect
from nltk.stem import PorterStemmer
import nltk

# nltk.download("punkt")

# Initialize Python porter stemmer
ps = PorterStemmer()
p = inflect.engine()
lemmatizer = WordNetLemmatizer()


def get_wiki_word_list():
    url = "https://en.wikipedia.org/wiki/Internet_protocol_suite"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.get_text()
    words = re.split('\W+', text)
    return words


def lemmatization(word, tag=None):
    tag = get_wordnet_pos(word, tag)
    return lemmatizer.lemmatize(word, tag)


# 获取单词的词性
def get_wordnet_pos(word, tag=None):
    # if word in {"defines"}:
    #     return wordnet.VERB
    if not tag:
        tag = pos_tag([word])[0][1]
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def get_known_word_list():
    file_path = "/Users/zhangmeng/myproject/blog_my/english/known.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words += line.split()
        return words


# 过滤
def to_filter(word_list: list[str]):
    known_word_set = set(get_known_word_list())
    word_list = [word for word in word_list if not word.isdigit()]  # 过滤数字
    word_list = [lemmatization(word, tag) for word, tag in nltk.pos_tag(word_list) if tag != 'NNP']
    # word_list = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in word_list]
    word_list = [p.partition_word(word)[1] for word in word_list]

    # [print(word,ps.stem(word)) for word in word_list if ps.stem(word) != word]
    # word_list = [ps.stem(word) for word in word_list]
    word_list = [word for word in word_list if len(word) > 3]
    word_list = [word.lower() for word in word_list]
    word_list = [word for word in word_list if word not in known_word_set]
    return word_list


#
# if __name__ == '__main__':
#     print(p.partition_word("defines"))
#     # a = get_wordnet_pos("defines")
#     # print(lemmatizer.lemmatize("defines", "v"))
#     # print(a)
# import os
#
# os._exit(0)
# words = get_known_word_list()
words = get_wiki_word_list()
words = to_filter(words)
print(len(words))
# 去除单个字母


word_counts = Counter(words)

with open('wiki_word_counts.txt', 'w', encoding='utf-8') as f:
    for word, count in word_counts.most_common():
        # print(word, count)
        if count > 3:
            # f.write(f"{word}: {count}\n")
            f.write(f"{word}\n")
with open("r.txt", 'w', encoding='utf-8') as f:
    word_list = []
    for word, count in word_counts.most_common():
        if count > 3:
            word_list.append(word)
    print(len(word_list))

    f.write(",".join(word_list))
