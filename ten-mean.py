import sys
# import pandas as pd
import csv
input = sys.argv[1]

ll=[]
ss=[]
sta=[]
fista=[]
fiend=[]
cc=[]
c1="chr1D"
f=open(input)
for x in f:
    x_split = x.strip().split('\t')
    n=x_split[3]
    chrom=x_split[0]
    start=x_split[1]
    end=x_split[2]
    if chrom==c1 :
        if len(ll)< 10 :
            ll.append(float(n))
            sta.append(start)
        else :
            ss.append(sum(ll)/len(ll))
            fista.append(sta[2])
            fiend.append(end)
            cc.append(chrom)
            del sta[0]
            del ll[0]
            ll.append(float(n))
            sta.append(start)
    else :
        if 0<len(ll) :
            ss.append(sum(ll)/len(ll))
            ll=[]
            fista.append(sta[2])
            sta=[]
            sta.append(start)
            fiend.append(end)
            cc.append(c1)
            ll.append(float(n))
            c1=chrom 
ss.append(sum(ll)/len(ll))
fiend.append(end)
fista.append(sta[2])
cc.append(chrom)
f.close()
#res=pd.DataFrame(cc, columns=['cc'])
#res = pd.concat([res, pd.DataFrame(fista,columns=['fista'])],axis=1)
#res = pd.concat([res, pd.DataFrame(fiend,columns=['fiend'])],axis=1)
#res = pd.concat([res, pd.DataFrame(ss,columns=['ss'])],axis=1)
data_list=[]
for a,b,c,d in zip(cc,fista,fiend,ss):
    x = {}
    x['Chrom']= a
    x['start']= b
    x['end'] = c
    x['ratio'] = d
    data_list.append(x)

with open(sys.argv[2],'w',newline='',encoding='UTF-8') as f_c_csv:
    writer = csv.writer(f_c_csv)
    writer.writerow(['Chrom', 'start','end','ratio'])
    for nl in data_list:
        writer.writerow(nl.values())

