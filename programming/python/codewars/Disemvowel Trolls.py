def disemvowel(string):
    k='qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM!?,'
    string1=''
    for i in range(len(string)):
        if string[i] in k:
            string1+=string[i]
        if string[i]==' ':
            string1+=' '
    string=string1
    return string
print(disemvowel('N ffns bt,r wrtng s mng th wrst v vr rd'))