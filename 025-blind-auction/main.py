from clear import clear
from art import logo

print(logo)
print("Welcome to the secret aution program.")
bid_list = {}
bidders = True
while bidders:
    bidder_name = input("What is your name?: ")
    bid_value = int(input("What is your bid: $"))
    bid_list[bidder_name]=bid_value
    # print(bid_list)

    other_bidders = input("Are there any ohter bidders? type 'yes' or 'no'")
    if other_bidders == "no":
        bidders = False
    else:
        clear()

max_bid = 0
max_bidder = ""
for bid in bid_list:
    # print(bid_list[bid])
    # print(type(bid_list[bid]))
    if bid_list[bid] > max_bid:
        max_bid = bid_list[bid]
        max_bidder = bid
print(f"The winner is {max_bidder} with a bid of ${max_bid}")