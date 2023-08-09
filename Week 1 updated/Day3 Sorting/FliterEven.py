def is_even(L):
    evenList = []
    for num in L:
        if num%2 == 0: #even
            evenList.append(num)
    return evenList
numbers =[10,2,3,14,17,29,19,18,22,26]
evens = is_even(numbers)#calling the function
print("Numbers: ", numbers)
#selecting evening numbers then put it in a new list
print("Even numbers: ", evens)

#Using Fliter
evenUsingFliter = list(filter(lambda n: n%2==0,numbers))
print("Filtered Evens: ", evenUsingFliter)