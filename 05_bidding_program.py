import os
bids = {}
n = int(input("How many people are participating in the auction? "))
for i in range(n):
    name = input(f"Enter your name: ")
    bid = float(input(f"Enter your bid amount: "))
    bids[name] = bid
    os.system('cls')
highest_bid = max(bids.values())
winner = max(bids, key=bids.get)
print(f"The winner of the auction is {winner} with a bid of ${highest_bid:.2f}")
