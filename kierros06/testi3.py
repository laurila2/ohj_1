tulokset = [6, 10, 15, 15, 15, 12, 9, 2]
import numpy as np


def tulosta_pylvaat(tulokset):
    hash = '#'
    for res in np.unique(tulokset):
        print(f'{res} {tulokset.count(res) * hash}')


tulosta_pylvaat(tulokset)