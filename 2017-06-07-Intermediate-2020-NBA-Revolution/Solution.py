from itertools import product, chain, permutations
from operator import add, sub, mul, truediv

_OPS = {add: '+', sub: '-', mul: '*', truediv: '/'}

def opcycle(ops):
    it = iter(ops)
    return lambda a, b: next(it)(a, b)

def countdown(text):
    values = map(int, text.split())
    values, target = values[:-1], values[-1]
    for ops, perm in product(product(*[_OPS] * 5), permutations(values)):
        if reduce(opcycle(ops), perm) == target:
            return '{0} {6} {1} {7} {2} {8} {3} {9} {4} {10} {5} = {11}'.format(
                *chain(perm, (_OPS[op] for op in ops), (target,)))
    return None

print countdown('1 3 7 6 8 3 250')
print countdown('25 100 9 7 3 7 881')
print countdown('6 75 3 25 50 100 952')
