bid = 0
print("!!!!!!!!!!!!!!!!!!!!\n!!!!!!Auction!!!!!!!\n!!!!!!!!!!!!!!!!!!!!")
auction_item = input("What is the auction for?:")
reserve_price = float(input("What is the reserve price?:"))
print(f"The auction for {auction_item} has started!\n")
while True:
    print(f"The Highest bid right now is ${bid}\n")
    bidder = round(float(input("What is your bid (-1 to exit auction): "
                         "$\n")), 2)
    if bidder < 0:
        break
    elif bid < bidder:
        bid = bidder
    elif bid >= bidder:
        print("Please bid a higher number\n")
if bid > reserve_price:
    print(f"The auction for {auction_item} has finished with a bid of $"
          f"{round(bid, 2)}")
else:
    print(f"The {auction_item} did not sell")
