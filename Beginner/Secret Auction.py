# Secret Auction

# LOGO
logo = '''
    █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
   ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
   ███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
   ██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
   ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

              ██████╗  █████╗ ███╗   ███╗███████╗
             ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
             ██║  ███╗███████║██╔████╔██║█████╗  
             ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
             ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
              ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

                 💰 PLACE YOUR BID 💰
'''
# User Input
name = input("What is your name? ")
bid = int(input("What is your bid? $"))

# Storing Bids
bids = {}
bids[name] = bid 
while input("Are there any other bidders? Type 'yes' or 'no'. ").lower() == "yes":
    print("\n" * 100) # Clear the console by printing new lines
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid


# Comparing Bids and Finding the Winner
max_bid = 0
max_bidder = ""
for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        max_bidder = key
print(f"The winner is '{max_bidder}' with a bid of ${max_bid}.")