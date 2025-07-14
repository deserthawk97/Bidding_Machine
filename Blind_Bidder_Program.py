logo = r'''              ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ '''
print(logo)
bidding = {}
continue_bid = True

def find_highest_bidder(bidding):
    highestbid=0
    for bid in bidding:
        bid_amount=bidding[bid]
        if bid_amount > highestbid:
            highestbid = bid_amount
            winner = bid
    print(f"The winner is :{winner} ")

while continue_bid:
    print("Welcome to the secret auction Program:")
    name = input("What is your name? \n")
    bid = int(input("What is your Bid? \n"))
    bidding[name] = bid
    data = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if data == "no":
        print("\n" * 29)
        continue_bid = False
        find_highest_bidder(bidding)
    elif data == "yes":
        print("\n"*29)














