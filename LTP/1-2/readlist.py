import os
path ="./"
lis=os.listdir(path)
print(lis)
print(len(lis))
for i in range(len(lis)):
    filename=str(lis[i])
    fr=open(filename, 'r', encoding='utf-8')
    content = fr.readlines()
    fr.close()

#    listClines=''
#   fd=open(filename,'r', encoding='utf-8')
#   listC=fd.readlines()

#   for line in listC:
#     line=line.strip()
#     if len(line)==0:
#        continue
#     listClines=listClines+line
#     print(listClines)
#   fd.close()
    characers = []  # 存放不同字的总数
    rate = {}  # 存放每个字出现的频率

# 依次迭代所有行
    for line in content:
    # 去除空格
        line = line.strip()
    # 如果是空行，则跳过
        contentLines = ''
        if len(line) == 0:
           continue
        contentLines = contentLines + line
    # 统计每一字出现的个数
        for x in range(0, len(line)):
        # 如果字符第一次出现 加入到字符数组中
           if line[x] in contentLines:
              characers.append(line[x])
        # 如果是字符第一次出现 加入到字典中
    charac=[]
    for x in range(0,len(characers)):
       if not characers[x] in charac:
          charac.append(characers[x])
    print(len(charac))

#print(charac)

#print('---------------')
#charac2=[]
#for x in range(0,len(listClines)):
#   if not listClines[x] in charac and not listClines[x] in charac2:
#      charac2.append(listClines[x])
#print(len(charac2))
#print(charac2)

