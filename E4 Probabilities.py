import random

def main():
    prob = random.random()
    if prob < 0.1:
        faverite = "bats"
    if prob <0.2 and prob >0.1:
        faverite = "cats"
    if prob > 0.2:
        faverite = "dogs"
    print("I love " + faverite)

main()
