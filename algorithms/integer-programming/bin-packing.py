import random
import math

def first_fit(lst):
    bins = []
    for pack in lst:
        for i in range(len(bins)):
            if (bins[i] + pack <= 1.0):
                bins[i] += pack
                break
        else:
            bins.append(pack)
        print(bins)
    return len(bins)

    packs = [.3, .2, .6, .7, .1, .2, .3, .4]
print(packs)

opt = math.ceil(sum(packs)) 
ff = first_fit(packs)
#ffd = first_fit_d(packs)
#bf = best_fit(packs)

print(f"OPT: {opt}")
print(f" FF: {ff}")
#print(f"FFD: {ffd}")
#print(f" BF: {bf}")
