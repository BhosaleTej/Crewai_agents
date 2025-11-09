
# for testing of webhook trigger
# for second testing of webhook trigger
# for third testing of webhook trigger after stash

#addition function
def divitionis(a,b,e):
    'divisionsn of ttr numbers'
    c = a / b 
    return c

def additionon(a,b):
    'addtions hof numbrs'
    c = a+b
    return c

def multiplicion(a,b):
    'multiply of numbers'
    c = a * b
    return c

def substracti(d,e):
    'substractions of number'
    f = d / e
    #substations
    return f

def factorial(n):
    return n+factorial(n-1)

def square(n):
    return n*2

def cub(n):
    #cube of number
    return n*3

def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count > 1 and nums[i] not in duplicates:
            duplicates.append(nums[i])
            #finds duplicates
    return duplicates

#first commit