import jieba
import jieba.posseg as psg
# 打开读取文件名为threekingdoms.txt的三国演义文档
txt = open('5.txt','r', encoding = 'utf-8').read()
# jieba.lcut() 精确模式切分中文
txt = psg.lcut(txt)
counts = {}
new = {}
# string.format() 格式化
for word in txt:
	# 去标点符号
	if word.flag == 'x':
		continue
	else:
		rword = word
	counts[rword] = counts.get(rword,0) + 1
li = list(counts.items())
# 由大到小排序
li.sort(key=lambda x:x[1], reverse=True)
for i in range(1,len(li)):
	key,value = li[i]
	print('{:<3}{:<4}{:>5}'.format(i,key,value))
