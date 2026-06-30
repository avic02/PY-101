logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def find_the_winner (bid_logs):
  winner = ""
  highest_bid = 0
  for bidder in bid_logs:
    bid_amt = bid_logs[bidder]
    if bid_amt > highest_bid :
      highest_bid = bid_amt
      winner = bidder
  
  print(f"The winner of the silent auction is {winner} with a bid amt of {highest_bid} $ \n CONGRATULATIONS !!")

bid_logs = {}

Bidding_countinues = True

while Bidding_countinues : 
    
  user_name = input("What is the name of the Bidder ? : \n").lower()

  user_bid = int(input("what is the amt of bid : $ "))

  bid_logs[user_name] = user_bid

  bid_loop = input("are there new bidder present : yes / no ? \n").lower()

  if bid_loop == "no":
    bidding_countinues = False 
    print("The bind has ended since there is no other bidder.")
    find_the_winner(bid_logs)
    break
  
  elif bid_loop == "yes":
    print("\n" * 15)
    continue

  else:
    continue

 



  
