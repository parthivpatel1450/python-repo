"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""

text = "hello world!hello world!hello world!hello world!"

def compress(s):
    result = ""
    count = 1

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    return result

def decompress(s):
    result = ""
    char = ""
    num = ""

    for ch in s:
        if ch.isalpha() or ch in [' ', '!']:
            if char:
                result += char * int(num)
            char = ch
            num = ""
        else:
            num += ch

    result += char * int(num)
    return result

compressed = compress(text)
decompressed = decompress(compressed)

print("Compressed:", compressed)
print("Decompressed:", decompressed)