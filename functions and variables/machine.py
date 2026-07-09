emoticon = ":("

def main():
    global emoticon
    say("is anyone there ?")
    emoticon = ":D"
    say("HII, ")

def say(phrase):
    print(phrase + " " + emoticon)

main()