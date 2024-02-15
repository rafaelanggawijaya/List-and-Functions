bid = 0
print("!!!!!!!!!!!!!!!!!!!!\n!!!!!!Auction!!!!!!!\n!!!!!!!!!!!!!!!!!!!!")
auction_item = input("What is the auction for?:")
reserve_price = float(input("What is the reserve price?:"))
print(f"The auction for {auction_item} has started!\n")
while True:
    print(f"The Highest bid right now is ${bid}")
    bidder = float(input("What is your bid (-1 to exit auction): "
                         "$")).__round__(2)
    if bid >= bidder:
        print("Please bid a higher number\n")
    elif bid < bidder:
        bid = bidder
    elif bidder == -1.0:
        break
if bid > reserve_price:
    print(f"The auction for {auction_item} has finished with a bid of ${bid}")
else:
    print("project")




