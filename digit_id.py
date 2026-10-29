#A digital ID scanner is malfunctioning and can read only one digit at a time.
#Given a number, break it into its individual digits (in the original order) 
#so the scanner can process each digit separately.

def split_number_to_list(number):
    lst=[]
    arr=[] 
    n=number
    while True:
        a = n%10
        b = n//10
        n=b
        lst.append(a)
        if n==0:
            break

    for i in range(len(lst)-1,-1,-1):
        arr.append(lst[i])
    print(arr)

split_number_to_list(6)