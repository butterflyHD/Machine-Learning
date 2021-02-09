# 1) FizzBuzz. Print numbers from 1 to 100
#    If it’s a multiplier of 3, print “fizz”
#    If it’s a multiplier of 5, print “buzz”
#    If both 3 and 5 — “fizzbuzz"
#    Otherwise, print the number itself 

def FizzBuss(n):
    
    i = 1
    while(1):
        r3 = i%3
        r5 = i%5
        f = 0
        b = 0
        fb = 0

        if(i%3 == 0):
            f = 1
        if(i%5 == 0):
            b = 1
        if((f == 1) & (b == 1)):
            fb = 1
          
        if(fb == 1):
            print('fizzbuzz')
        elif(f == 1):
            print('fizz')
        elif(b == 1):
            print('buzz')
        else:
            print(i)
        i += 1
        if(i > n): break


# 2) Factorial. Calculate a factorial of a number

def Factorial(n):
   v = 1
   for i in range(2, n+1):
       v *= i
   print(v)

# 3) mean([4, 36, 45, 50, 75]) = 42

def meanInList(list):
    n = len(list)
    v = 0
    for i in range(0, n):
        v += list[i]/n
    return(v)

# 4) given a list, and a N, if there exist A+B = N, return True
def ABN(ll, N):
    llmax = max(list)
    llmin = min(list)
    vCand = 0
    #(1) llmax + llmax  < N, return false
    if(N > llmax * 2) return False
    #(2) llmin + llmin > N return false
    if(N < llmin * 2) return False

    while(1):
        i = 1
        j = 1
        vCand  = list[i] + list[j]
        vCandi = list[i+1] + list[j]
        if (vCand == N) 
            return True
        if (vCandi == N) 
            return True
        if (vCandi > N)
            







if __name__ == '__main__':
    #FizzBuss(10)
    #Factorial(5)
    ll = ([4,36,45,50,75])
    mm = meanInList(ll)
    print(mm)







