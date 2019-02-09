#import settings
import math

#set up variables
platinumCoin = 0;
goldCoin = 0;
electrumCoin = 0;
silverCoin = 0;
copperCoin = 0;
teamSize = 0;
total_coin_copper = 0;

input('Press Enter to divide currency between your party...')
teamSize = int(input('Please enter your Party size... '))

#convert the coin to copper and divide by team size covert back
#using highest denomination first

platinumCoin = int(input('Enter Platinum Coin  '))
goldCoin = int(input('Enter Gold Coin  '))
electrumCoin = int(input('Enter Electrum Coin  '))
silverCoin = int(input('Enter Silver Coin  '))
copperCoin = int(input('Enter Copper Coin  '))

#calculate total copper
total_coin_copper = (platinumCoin * 1000) + (goldCoin * 100)+ (electrumCoin * 50) + (silverCoin * 10) + copperCoin

#Use electrum coins for output?
electrum_ignore = input('Output with Electrum Coin? y/n ')

#divide total by party size
#check remainder if the amount cannot be divided by party size and take from total coin
coin_remainder = total_coin_copper % teamSize
total_coin_copper = total_coin_copper - coin_remainder

#divide the total amount minus the remainder by team size
player_coin_copper = total_coin_copper / teamSize

#while total_coin_copper >0:
#    platinumCoin = player_coin_copper / 1000

#print the remainder to be added manually
print('coin remainders Copper Pieces ', coin_remainder)

print(total_coin_copper in range (0):

