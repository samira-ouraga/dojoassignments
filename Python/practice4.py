def Mixedlist():
    print "enter a list with any value"
    response = input()
    sum = 0 
    sentence = ''
    for i in response:
        if isinstance(i, int):
            sum += int(i)
            print  'The list you entered is of integer type, the sum is ' + str(sum) + ''
        
        elif isinstance(i, str):
            sentence+=str(i)
            print 'The list you entered is of string type, it is ' + sentence + ''
        
        elif isinstance(i, str) and isinstance(i, int):
            sum += int(i)
            sentence+=str(i)
            print 'The list you entered is of mixed type, the sum is ' + str(sum) + 'the words are ' + sentence + ''
    
print Mixedlist()

