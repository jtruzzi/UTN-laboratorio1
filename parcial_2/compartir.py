clubs = [("Spikes", "black"), ("Diamonds", "red"), ("Hearts", "red"), ("Trebor", "black")]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Ace"]

stack = list()
for club, colour in clubs:
    for numero in numbers:
        stack.append((numero, club, colour))

def sort_func(card):
    return card[2]

stack_sorted = sorted(stack, key=sort_func)
print(stack_sorted)
