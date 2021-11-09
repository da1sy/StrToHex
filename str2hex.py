#!/usr/bin/env python2
import sys
def strTohex(strr,bit=4):
    print "\n         Str To Hex   "
    print "-"*29
    strr = list(strr)
    while 1 :
        if len(strr)%4 == 0 or len(strr)%8 == 0 : break
        strr.append(' ')

    hex_str = []
    for i in strr:
        hex_str.insert(0,hex(ord(i)))
    intt = 1
    for i in hex_str:
        print i[2:]+"",
        if (intt % bit) == 0:
            print "    |    ",
            strrr = hex_str[intt-bit:intt]
            for s in strrr:
                print chr(int(s,16)),
            print ''
        intt += 1
    print '-'*29
    return hex_str
if __name__ =="__main__":
    try:
        strTohex(sys.argv[1],int(sys.argv[2]))
    except:
        strTohex(sys.argv[1])
