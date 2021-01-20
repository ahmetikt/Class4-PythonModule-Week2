#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### 1 #####
# simdiye kadar yapilmis en hantal python kodu olabilir bu. En az 8 saat ugrastim. ilk once for dongusu ile yapayim dedim
#ilk satirda oldugu gibi ama out of range hatasindan kurtulamadim. Sonunda kese cikara sonuca ulastim


list1 = list(range(1,23))
for i in list1:
    list1.remove(i+1)
list2 = list1[2],list1[5],list1[8]
list3 = set(list1)- set(list2) 
list4 = list(list3)

list5= list4[3],list4[7]
list6 = set(list4)- set(list5)
list7 =list(list6)

list8 = list7[4]

list8_1 = []
list8_1.append(list8)

list9 = set(list7)- set(list8_1)

list10= list(list9)
list10


# In[ ]:





# In[ ]:


##2##


import collections
from collections import deque  

list4 = collections.deque([1,2,3,4,5])
#list4.rotate(2)
list4.rotate(-2)


# In[ ]:





# In[ ]:


###3###

#bos bir dict olustururuz
#replace ile bosluklari yer degistirme yontemi ile aliriz
#karakterleri ayristiririz
#karakter listemizde var mi yok mu kontrol edilir
#ekleme yapilir
#ve print ederiz




soz = dict()
tekst = input('noktalama isareti kullanmadan bir cumle giriniz; ')
tekst = tekst.replace(' ','')
for kelime in tekst:
    if kelime in soz:
        soz[kelime] = soz[kelime]+1
    else:
        soz[kelime] = 1
            
for j in soz:
    print(j, ":", soz[j], end=' ', sep=' ')
    


# In[ ]:


### 4 #### 


in1 = input().lower().strip()
in2 = input().lower().strip()
k1 = set(in1)
k2 = set(in2)
k3= k1|k2
a= list(k3)
a.sort()

kar=''.join(a)

cc = list(kar)

aa = ''.join(cc[0:2])

bb = ''.join(cc[2:3])

dd = ''.join(cc[3:])

son = [aa,bb,dd]
son



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




