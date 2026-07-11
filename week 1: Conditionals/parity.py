def main():
    x = int(input("enter the value of x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return n % 2 == 0
#    if n % 2 == 0:
#        return True
#    else:
#        return False
    
main()