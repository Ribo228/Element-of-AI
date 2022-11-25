def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_pop = sum(populations)
    total_fishers = sum(fishers)
    cond_pop = []
    for j in range(len(countries)):
        #cond_pop.append(fishers[j] / total_fishers * 100)
        percentage = fishers[j] / total_fishers *100
        cond_pop.append(percentage)

    for country,cond_pop in zip(countries, cond_pop):
        print("%s %.2f%%" % (country, cond_pop)) # modify this to print correct results

main()
