fiz=0
math=0
rus=0
c=0
with open ('D:\Python\programms\dataset_3363_4.txt') as f:
    with open ('D:\Python\programms\out.txt','w') as out:
        for line in f:
            s=(line.strip().split(';'))
            #print ((int(s[1])+int(s[2])+int(s[3]))/3)
            out.write (str((int(s[1])+int(s[2])+int(s[3]))/3)+'\n')
            fiz+=int(s[1])
            math+=int(s[2])
            rus+=int(s[3])
            c+=1
        out.write (str(fiz/c))
        out.write (' ')
        out.write (str(math/c))
        out.write (' ')
        out.write (str(rus/c))
#print(str(fiz/c),str(math/c),str(rus/c))
#print (fiz,math,rus)
