def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    for i in range(n):
        odds = 1*(2**(i+1))
        pass           # edit here to update the odds
    print(odds)

n = 7
flip(n)
