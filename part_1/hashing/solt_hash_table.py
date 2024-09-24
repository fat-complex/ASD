import math
import statistics

from part_1.hashing.hash_table import HashTable
import random

char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPKRSTUVWXYZ123456789_"

class SoltHashTable(HashTable):
    def __init__(self, sz, stp):
        super().__init__(sz, stp)
        self.solt = ''.join(random.choice(char_set) for _ in range(6))

    def hash_fun(self, value):
        return super().hash_fun(value + self.solt)


def get_rainbow_for_source_table(table: HashTable, expected_collisions: int):
    collisions = 0
    rainbow: {} = {}
    while collisions < expected_collisions:
        key = ''.join(random.choice(char_set) for _ in range(random.randint(1, len(char_set))))
        h = table.hash_fun(key)
        if h in rainbow:
            rainbow[h].append(key)
            collisions += 1
        else:
            rainbow[h] = [key]
    return {key: val for (key, val) in rainbow.items() if len(val) > 1}

table1 = HashTable(3571, 1)

solt_table = SoltHashTable(3571, 1)

def number_of_matches(rainbow_table, table: SoltHashTable)-> int:
    cnt = 0
    for rainbow_hash_key, matches in rainbow_table.items():
        for val in matches:
            if table.hash_fun(val) == rainbow_hash_key:
                cnt += 1
    return cnt

results = []
for case in range(100):
    #Attack
    rainbow_table = get_rainbow_for_source_table(table1, 1000)
    #Defence
    results.append(number_of_matches(rainbow_table, solt_table))

print("Mean average for matches in rainbow for 1000 elements: ", math.ceil(statistics.mean(results)))
print("Max matches in rainbow for 1000 elements: ", max(results))
print("Probability breaking is ", math.ceil(statistics.mean(results)) / 1000 * 100)




