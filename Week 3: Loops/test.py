s = s.input()
s = s.lower()
new = ""
for ch in s:
    if s.isalnum() == False:
        new += ch
if new == "":
    print ("False")
else:
    print ("True ")