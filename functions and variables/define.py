def main():
    name = input("Whats your name? ").strip().capitalize()
    hello(name)



def hello(to = "World"):
    print("Hello,", to)


main()