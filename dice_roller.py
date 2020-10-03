import random
def main():
    dice_rolls=2
    roll_sum=0
    for i in range(0,dice_rolls):
        roll=random.randint(1,6)
        roll_sum += roll
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {roll_sum}')
if __name__== "__main__":
  main()