mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"
count=0

for x in mystr:
    if x.lower() in vowels:
        count+=1
print("number of vowels=",count)