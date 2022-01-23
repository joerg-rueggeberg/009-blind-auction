# REPLIT VERSION

from replit import clear
from art import logo

bidders = {}
max_bidder = ""
max_bid = 0.0
ended = False

while not ended:
    print(f"Blind Auction Software{logo}")
    bidder_name = str(input("\nWie heißt du? (Spitzname) "))
    bidder_bet = int(input("Wie viel möchtest du bieten? € "))
    bidders[bidder_name] = bidder_bet

    bidder_new = input("\nNehmen weitere Personen an der Auktion teil? 'ja'/ 'nein': ").lower()

    if bidder_new == "ja":
        clear()
    elif bidder_new == "nein":
        clear()
        print(f"Blind Auction Software{logo}")
        ended = True
print("\nWir haben einen Sieger!")

for bidder in bidders:
    if bidders[bidder] > max_bid:
        max_bid += bidders[bidder]
        max_bidder = bidder
print(f"\nHerzlichen Glückwunsch! {max_bidder} erhält den Zuschlag mit einem Gebot von: {max_bid}€")
