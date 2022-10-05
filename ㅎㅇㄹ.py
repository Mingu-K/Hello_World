
if __name__ == "__main__":
    spruce(3)
'''

def line(number, text):
    if text=="":
        print("*"*number)
    else:
        print(text[0]*number)

def shape (size1, character1, size2, character2):
    num=1
    while num<=size1:
        line(num, character1 )
        num+=1
    sum=1
    while sum<=size2:
        line(size1, character2)
        sum+=1
a = [1,2,3,4]
print('hi')


'''ef spruce(number):
    print("a spruce!")
    bo = 1
    while 0 < number:
        num = "*" * bo
        i = " " * (number - 1)
        print(i + num)
        bo += 2
        number -= 1


if __name__ == "__main__":
    spruce(3)
'''

def line(number, text):
    if text=="":
        print("*"*number)
    else:
        print(text[0]*number)

def shape (size1, character1, size2, character2):
    num=1
    while num<=size1:
        line(num, character1 )
        num+=1
    sum=1
    while sum<=size2:
        line(size1, character2)
        sum+=1


if __name__ == "__main__":
    shape(5, "x", 2, "o")