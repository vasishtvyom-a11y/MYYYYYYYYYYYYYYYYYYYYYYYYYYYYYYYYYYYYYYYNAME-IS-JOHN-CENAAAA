print("Hello! I am AI Bot. What's your name?:")
name=input()
print(f"Nice to meet you,{name}!")
print("How are you feeling today?(good or bad):")
mood=input().lower()
if mood=="good":
    print ('I am glad to hear that')
if mood=="bad":
    print("I am, sorry to hear that.Hope" 
    "Eveyrthing gets better soon.")
else:
    print("I see.Its hard to put feeling to words")
print(f"It was nice chatting with you {name}.Good Bye!")

