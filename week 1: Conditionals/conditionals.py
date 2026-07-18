def main():

    Difficulty = input("Hard or casual").strip().capitalize()
    if not (Difficulty == "Hard" or Difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    players = input("Multiplayer or Single").strip().capitalize()
    if not (players == "Multiplayer" or players == "Single"):
        print("Enter a valid num of players")
        return

    if Difficulty == "Hard" and players == "Multiplayer":
        recommend("Poker")
    elif Difficulty == "Hard" and players == "Single":
        recommend("Klondike")
    elif Difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("you might like ", game)

main()