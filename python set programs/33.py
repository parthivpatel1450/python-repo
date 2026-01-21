l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
s1=set(l1)
s2=set(l2)
commons = s1&s2 # or s1.intersection(s2)
commonlist = list(commons)
print (commonlist)