from __future__ import print_function
import random
def top_to_random(l, n, printing):
    for i in range(0, n):
            random_index = random.randint(0, (len(l) - 1))
            top = l[0]
            for j in range(0, random_index):
                l[j] = l[j + 1]
            l[random_index] = top
            if (printing):
                for k in range(0, len(l)):
                    print(l[k], end = " ")
                print("")
    return l
list1 = [1, 2, 3, 4, 5]
top_to_random(list1, 10, True)

def monte_carlo(l, n, k, r):
    n_at_top = 0.0
    for i in range(0, r):
        l = top_to_random(l, k, False)
        if (l[0] == n):
            n_at_top += 1
    return n_at_top / r

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(monte_carlo(list2, 10, 10, 200000))
print(monte_carlo(list2, 10, 25, 200000))
print(monte_carlo(list2, 10, 50, 200000))
print(monte_carlo(list2, 10, 75, 200000))
print(monte_carlo(list2, 10, 100, 200000))
