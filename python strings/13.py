mystr = '10101'

def strtoint(mystr):
    for x in mystr:
        if x is not '01':
            return "Error. String with non-binary characters"
    num=int(mystr,2)
    return num

print ("binary:{} integer: {}".format(mystr,strtoint(mystr)))