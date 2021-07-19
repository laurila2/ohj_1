tulokset = [6, 10, 15, 15, 15, 12, 9, 2]

def tulosta_pylvaat(tulokset):
    # min, max, count

    korkein = max(tulokset)
    pienin = min(tulokset)
    hash = "#"

    print("")
    print("Information related to coffee drinkers:")
    i = 1
    for i in range(pienin, korkein + 1):
        print(f"{i} {hash * tulokset.count(i)}")
        i += 1

tulosta_pylvaat(tulokset)