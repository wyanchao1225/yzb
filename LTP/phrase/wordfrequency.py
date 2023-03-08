import json
fr =open('1-2.txt','r',encoding='utf-8')
characers=[]
stat={}
for line in fr:
    line=line.strip()
    if len(line)==0:
        continue
    for x in range(0,len(line)):
        if line[x] in [' ','。',' 。','“',"”","{","}","(",")","[","]","<<",">>","?","，",":","：","！","？"]:
         continue
        if  line[x] not in characers:
            characers.append(line[x])
        if  line[x] not  in stat.keys():
            stat[line[x]]=0
        stat[line[x]]+=1
fw1=open('result.json','w')
fw1.write(json.dumps(stat))
fw1.close()
stat=sorted(stat.items(),key=lambda d:d[1],reverse=True )  #d[1]为计数的值
print(type(stat),len(stat))

fw=open('result.txt','w',encoding="utf8")
for item11 in stat:
    fw.write(item11[0]+","+str(item11[1])+"\n")
fr.close()
fw.close()
