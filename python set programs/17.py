lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = {"SQL", "C#"}

a=lang1.union(lang2)
b=lang2 | lang3

print(a)
print(b)