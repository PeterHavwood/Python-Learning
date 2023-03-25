def escapeChar():
    print('\'Hello World!\'')
    # a strange thing here: print(r'\') https://www.jianshu.com/p/b9a5876ebe4e
    print('if u dont like escape char \n \\')
    print('\n \\Bye~\\')  

def operatorChar(str1, str2):
    #string is immutable type, so we can pass it here
    print('str1 * 3 + str2 * 2: ', str1 * 3 + str2 * 2)
    str1 += str2
    print('str1 += str2: ', str1)
    print('Is \'wo\' now in str1? ', 'wo' in str1)
    # slicing
    print('str1[2]: ', str1[2])
    print('str1[2:5]: ', str1[2:5])
    print('str1[2::2]: ', str1[2::2])

def methodChar(str1, str2):
    print(len(str1))
    print(str1.find('el'))

    print(str1.center(10,'*'))
    print(str2.rjust(15,' '))

    strWithSpace = '   abdc  efe   '
    print(strWithSpace.strip())

def formatPrint():
    a1 = 1
    a2 = 1.3
    b = True
    c = [1, 2, 3]
    d = 'bye!'

    print('a1: %d  a2(d): %d  a2(f): %f a2(.3f): %.3f' % (a1, a2, a2, a2))
    print('a1: {0}, a2: {1}, b: {2}'.format(a1, a2, b))
    print(f'a1: {a1}, a2: {a2}, c:{c}, {d}')

str1 = 'hello'
str2 = 'world'
#escapeChar()
#operatorChar(str1,str2)
#methodChar(str1,str2)
#formatPrint()