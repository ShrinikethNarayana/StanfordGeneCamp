import anydbm

dict1 = anydbm.open('lncH', 'r')

dict2 = anydbm.open('notlncH', 'c')

count = 0

for key in dict1:
    dict2[key] = dict1[key]
    if count == 10000:
        break
    count += 1
