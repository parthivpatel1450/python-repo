s1={1,2,3,4,5}
s2={4,5,6,7,8}

joined_set={x for s in [s1,s2] for x in s}
print(joined_set)