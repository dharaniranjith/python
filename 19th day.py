# individual list la two list print aganum
'''a=[1,2,3,4,5,6,7,8]
a[0]=[1,2]
a[1]=[3,4]
a[2]=[5,6]
a[3]=[7,8]
a.pop()
a.pop()
a.pop()
a.pop()
print(a)'''
#alternate 
'''a=[1,2,3,4,5,6,7,8]
b=[]
for i in range(0,len(a),2):
    b.append([a[i],a[i]+1])
print(b)'''
#a,b la pair ah varanum
'''a=[1,2,3,4,5,6,7,8]
b=[0,0,0,0,0,0,0,0]
c=[]
for i in range(len(a)):
    c.append([a[i],b[i]])
print(c)'''

# multiple same string highest key of ascii value in string print one value
a="abjabcaiyb"
b={}
d=[]
for i in a:
    c=a.count(i)
    b[i]=c
e=max(b.values())
for i in a:
    if a.count(i)==e:
        d.append(i)
print(d)
for i in range(65,92):
    if chr(i) in d:
        print(chr(i))
        break

    
