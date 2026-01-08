import array as ar
s1="WORD"
print ("original string:", s1)

# converting it to an array
sar=ar.array('u', s1)

# inserting an element
sar.insert(3,"L")

# getting back the modified string
s1=sar.tounicode()
print ("Modified string:", s1)