b=[i+10 for i in range(9)]
b=[i*10 for i in range(9) if i%2==0]
d=[i*2 if i%2==1 else i*3 for i in range(9)]
#只要有免費的列表不用range
b=[i+10 for i in a]
b=[i*10 for i in a if i%2==0]
d=[i*2 if i%2==1 else i*3 for i in a]

n=["Bob","Tom","Alice","Jerry","Wendy","Smith"]
a=[i.upper()+"3"if len(i)<4 else i.upper()+"5" for i in n ]
#集合的推導式
s={1,1,2,3,3,4,5,6,6}
a={i for  i in s if i%2==0}
a={i*i for i in s if i%2==0}
a={i*i if i%2==0 else i*i*i for i in s}
a={i**2 if i%2==0 else i**3 for i in s}
#字典的推導式
a={i:i+10 for  i in s if i%2==0}
a={i:i*i+10 for i in s if i%2==0}
a={i:i*i if i%2==0 else i*i*i for i in s}
a={1:i**2 if i%2==0 else i**3 for i in s}
#元組
a=(i for i in range (9))
tuple(a)

