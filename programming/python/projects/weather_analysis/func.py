def chif(s):
    chifri='0123456789+-'
    itog=''
    for i in range(len(s)):
        if s[i] in chifri:
            itog+=s[i]
    return itog
