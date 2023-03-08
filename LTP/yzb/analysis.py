# -*- coding: utf-8 -*-
# @Time : 2019/8/25 10:31
# @Author : Administrator 
# @File : zitongji.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
#用来统计TXT文本，并统计字频
# 打开文件
fr = open('1.txt', 'r', encoding='utf-8')
# 读取文件所有行
content = fr.readlines()
contentLines = ''

listClines=''
fd=open('2.txt','r', encoding='utf-8')
listC=fd.readlines()

for line in listC:
    line=line.strip()
    if len(line)==0:
       continue
    listClines=listClines+line
#print(listClines)
characers = []  # 存放不同字的总数
rate = {}  # 存放每个字出现的频率

# 依次迭代所有行
for line in content:
    # 去除空格
    line = line.strip()
    # 如果是空行，则跳过
    if len(line) == 0:
        continue
    contentLines = contentLines + line
    # 统计每一字出现的个数
    for x in range(0, len(line)):
        # 如果字符第一次出现 加入到字符数组中
        if line[x] in listClines:
            characers.append(line[x])
        # 如果是字符第一次出现 加入到字典中
charac=[]
for x in range(0,len(characers)):
    if not characers[x] in charac:
       charac.append(characers[x])
print(len(charac))

print(charac)

print('---------------')
charac2=[]
for x in range(0,len(listClines)):
    if not listClines[x] in charac and not listClines[x] in charac2:
       charac2.append(listClines[x])
print(len(charac2))
print(charac2)

fr.close()
fd.close()


