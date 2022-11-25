countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # write your solution here
    total_population = sum(populations)
    total_fishers = sum(fishers)

    guess = None
    biggest = 0.0
    para = (populations[0]/total_population) * (fishers[0] / populations[0])
    for i in range(len(populations)):
        start = (populations[i]/total_population) * (fishers[i]/populations[i])
        if start > para:
            para = (populations[i]/total_population) * (fishers[i]/populations[i])
            guess = countries[i]
            biggest = fishers[i] / total_fishers * 100
    return (guess, biggest)

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
