def main():

    Difficulty = input("Hard or casual").strip().capitalize()
    players = input("Multiplayer or Single").strip().capitalize()

    if Difficulty == "Hard":
        if players == "Multiplayer":
            recommend("Poker")
        elif Difficulty == "Casual":
            recommend("Klondike")
        else:
            print("Enter a valid num of players")
   
    elif Difficulty == "Medium":
        if players == "Multiplayer":
            recommend("Hearts")
        elif Difficulty == "Casual":
            recommend("Clock")
        else:
            print("Enter a valid num of players")

    else: 
        print("Enter a valid difficulty")

def recommend(game):
    print("you might like ", game)

main()