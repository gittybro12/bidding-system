
bid = {}
still_bidding = False
higher = 0
def greater_bid():
    global higher
    for x in bid:
        bid_value = bid[x]
        if bid_value > higher:
            higher = bid_value
    print(f"The winner of the bid is {x} with a bid of ${higher}")        
while not still_bidding:
    name = input("Please enter your name\n")
    bid_amount = int(input("Please enter bid amount\n$"))

    bid[name] = bid_amount

    bidding = input("Still bidding? 'yes' or 'no'")
    if bidding == 'no':
        greater_bid()
        still_bidding = True


        



