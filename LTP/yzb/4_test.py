import jieba
import jieba.posseg as psg
# 打开读取文件名为threekingdoms.txt的三国演义文档
txt = open('5.txt','r', encoding = 'utf-8').read()
# jieba.lcut() 精确模式切分中文
txt = psg.cut(txt)
for word in txt:
    print(word)
