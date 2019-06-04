def basic():
    for i in range(251):
        print(i)

#basic()


def mult_5():
    for i in range(5,1001,5):
        print(i)

# mult_5()


def dojo_count():
    for i in range (1,101):
        if(i%10 == 0):
            print("Coding Dojo")
        elif(i%5 == 0):
            print("Coding")
        else:
            print(i)

# dojo_count()

def huge():
    sum = 0
    for i in range(0,500001):
        sum+=i
    print(sum)

# huge()

def countdown_4():
    for i in range(2018,0,-4):
        print(i)

# countdown_4()

def flex_counter(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if (i%mult == 0):
            print(i)
    
# flex_counter(2,9,3)
