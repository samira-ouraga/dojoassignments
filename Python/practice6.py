def FindChar(list_a):
    print "pick a character"
    char  = input()
    list_b = ''
    for i in list_a:
        if char in i:
            list_b += str(i)
    return list_b
print FindChar(['hello','world','my','name','is','Anna'])

