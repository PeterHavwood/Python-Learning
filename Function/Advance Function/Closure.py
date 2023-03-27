def lazySum(*args):
    def sum():
        result = 0
        for n in args:
            result += n
        return result
    return sum

def mistakeExample():
    f = []
    for i in range(1,4):
        def fun():
            return i
        f.append(fun)
    return f

def rightExample():
    f = []
    # WTF....
    def fun(j):
        def g():
            return j
        return g
    for i in range(1,4):
        f.append(fun(i))
    return f

def countFun():
    count = 0
    def fun():
        nonlocal count
        count = count + 1
        return count
    return fun

def main():
    f1 = lazySum(1,2,3)
    f2 = lazySum(2,3,4)
    print("f1=============")
    print(f1)   # f1 refers to the function sum in lazySum
    print(f1())
    print("f2=============")
    print(f2)
    print(f2())

    print("Will there be 1, 2, 3?")
    # Answer is 'NO'
    fmList = mistakeExample()
    print(fmList[0]())   # fun in mistakeExample runs now, and i there now is 3
    print(fmList[1]())
    print(fmList[2]())

    # Now you get right result ^_^
    frList = rightExample()
    print(frList)
    print(frList[0]())
    print(frList[1]())
    print(frList[2]())

    count1 = countFun()
    print(count1(),count1(),count1())

if __name__ == '__main__':
    main()