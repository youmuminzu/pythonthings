import re
import jieba.posseg as psg
import collections


def readfile(file_url):
    file = open(file=file_url, mode='r', encoding='utf-8')
    content = file.read()
    return content


def stoplist():
    stoplist1 = [
        line.rstrip()
        for line in open(file='百度停用词表.txt', mode='r', encoding='utf-8')
    ]
    stoplist2 = [
        line.rstrip()
        for line in open(file='哈工大停用词表.txt', mode='r', encoding='utf-8')
    ]
    stoplist3 = [
        line.rstrip()
        for line in open(file='四川大学停用词库.txt', mode='r', encoding='utf-8')
    ]
    stopwords = stoplist1 + stoplist2 + stoplist3
    return stopwords


stoplist = stoplist()
text = readfile('tophub_out.txt')
filter = re.compile('[^\u4E00-\u9FD5]+')
text = filter.sub('', text)
seg = psg.cut(sentence=text, use_paddle=True)
meaninfulword = []
for word, flag in seg:
    word = word.strip()
    if word not in stoplist:
        meaninfulword.append(word)
print(meaninfulword)
count = collections.Counter(meaninfulword)
# print(count)
print(count.most_common(200))