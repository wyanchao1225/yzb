from ltp import LTP
from ltp import StnSplit
ltp = LTP()
phrase_list=[]
# 打开读取文件名为threekingdoms.txt的三国演义文档
txt = open('1.txt','r', encoding = 'utf-8').read()
#print(txt)
sents = StnSplit().split(txt)
print(len(sents))
for word in sents:
  phrase_list.append(word)

print(phrase_list)

output = ltp.pipeline(phrase_list,tasks=["cws", "pos", "ner", "srl", "dep", "sdp"])
  #print(output.cws)

#counts = {}
#new = {}
# string.format() 格式化
#for word in txt:
	# 去标点符号
#	if len(word) == 1:
#		continue
#	else:
#		rword = word
#	counts[rword] = counts.get(rword,0) + 1
#li = list(counts.items())
# 由大到小排序
#li.sort(key=lambda x:x[1], reverse=True)
#for i in range(1,len(li)):
#	key,value = li[i]
#	print('{:<3}{:<6}{:>5}'.format(i,key,value))

#ltp = LTP("LTP/small")  # 默认加载 Small 模型
#fr = open('5.txt', 'r', encoding='utf-8')
# 读取文件所有行
#content = fr.readlines()
#sents = StnSplit().split(content)
#print(sents)
#contentLines = ''
#for line in content:
    # 去除空格
 #   line = line.strip()
    # 如果是空行，则跳过
  #  if len(line) == 0:
   #     continue
   # contentLines = contentLines + line
#str1=''.join(contentLines)
#print(str1)
#print(contentLines)
#sents = StnSplit().split(contentLines)

#sents = StnSplit().batch_split([contentLines])
#for i in sents:
#  print(i)
#tmp="他叫汤姆去拿外衣。"
#for i in range(0,len(sents)):
#    output = ltp.pipeline(sents[i], tasks=["cws", "pos", "ner", "srl", "dep", "sdp"])
# 使用字典格式作为返回结果
#    print(output.cws)  # print(output[0]) / print(output['cws']) # 也可以使用下标访问
 #   print(output.pos)
  #  print(output.sdp)

# 使用感知机算法实现的分词、词性和命名实体识别，速度比较快，但是精度略低
#ltp = LTP("LTP/legacy")
# cws, pos, ner = ltp.pipeline(["他叫汤姆去拿外衣。"], tasks=["cws", "ner"]).to_tuple() # error: NER 需要 词性标注任务的结果
#cws, pos, ner = ltp.pipeline(sents[0], tasks=["cws", "pos", "ner"]).to_tuple()  # to tuple 可以自动转换为元组格式
# 使用元组格式作为返回结果
#print(cws, pos, ner)
