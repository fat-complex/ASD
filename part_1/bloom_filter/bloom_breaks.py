import random

from part_1.bloom_filter.bloom_filter import BloomFilter

expected_keys = ["gg_wp", "gg_wp_123", "skill_smart", "nba_playoffs"]

bf = BloomFilter(32)

for key in expected_keys:
    bf.add(key)

some_keys = expected_keys + ["sdfsd", "jkghfg1234_", "sddfs45234sdf", "12343dfgd____"]
found_keys = []

for key in some_keys:
    if not bf.is_value(key):
        print("found: ", key)
        found_keys.append(key)

assert (set(some_keys) - set(found_keys) == set(expected_keys))