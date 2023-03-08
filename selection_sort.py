import random

MAX_VAL = 65536

class Sort:
    def __init__(self):
        self.reset_stats()

    # construct a random list of size n
    def random_list(n):
        lst = []
        for i in range(n):
           lst.append(random.randint(0, MAX_VAL))
        return lst

    def is_sorted(lst):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True

    def reset_stats(self):
        self.comps = 0
        self.moves = 0

    def get_comps(self):
        return self.comps

    def get_moves(self):
        return self.moves

    def compare(self, comparison):
        self.comps += 1
        return comparison

    def swap(self, lst, i, j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        self.moves += 3

    # Original version of selection sort.
    # You should *NOT* modify this version.
    def selection_sort(self, lst):
        for i in range(len(lst) - 1):
            index_min = i
            for j in range(i + 1, len(lst)):
                if self.compare(lst[j] < lst[index_min]):
                    index_min = j
            self.swap(lst, i, index_min)

    # Modified version of selection sort.
    def selection_sort_mod(self, lst):
        for i in range(len(lst) - 1):
            index_min = i
            for j in range(i + 1, len(lst)):
                if self.compare(lst[j] < lst[index_min]):
                    index_min = j
            self.swap(lst, i, index_min)


if __name__ == "__main__":
    sort = Sort()
    lst = Sort.random_list(100)
    sort.selection_sort(lst)
    print("comparisons: " + str(sort.get_comps()))
    print("moves: " + str(sort.get_moves()))
    assert(Sort.is_sorted(lst))
