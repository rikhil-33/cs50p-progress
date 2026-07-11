name = input("Whats your name? ")

match name :
    case "Rikhil" | "Aditya" | "Sourish" | "Yashasvi" | "Ashrit":
        print("Hyd")
    case "Sreekar":
        print("AP")
    case _:
        print("who")
