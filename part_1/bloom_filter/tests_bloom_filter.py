import unittest

from part_1.bloom_filter.bloom_filter import BloomFilter


class TestAddMethod(unittest.TestCase):
    def test_add(self):
        bloom = BloomFilter(32)

        str1 = "0123456789"
        str2 = "1234567890"
        str3 = "2345678901"
        str4 = "3456789012"
        str5 = "4567890123"
        str6 = "5678901234"
        str7 = "6789012345"
        str8 = "7890123456"
        str9 = "8901234567"
        str10 = "9012345678"

        bloom.add(str1)

        self.assertEqual(bloom.is_value(str1), True)
        self.assertEqual(bloom.is_value(str2), False)
        self.assertEqual(bloom.is_value(str3), True)
        self.assertEqual(bloom.is_value(str4), False)
        self.assertEqual(bloom.is_value(str5), True)
        self.assertEqual(bloom.is_value(str6), False)
        self.assertEqual(bloom.is_value(str7), True)
        self.assertEqual(bloom.is_value(str8), False)

        bloom.add(str2)
        self.assertEqual(bloom.is_value(str2), True)

        bloom.add(str9)
        self.assertEqual(bloom.is_value(str9), True)

        bloom.add(str10)
        self.assertEqual(bloom.is_value(str10), True)

        self.assertEqual(bloom.is_value("sdfsdfsdfsdfs"), False)


    def test_remove(self):
        bloom = BloomFilter(32)

        possible_keys = ["11111", "22222", "33333", "12345", "54321"]
        added_keys = []
        for key in possible_keys:
            bloom.add(key)
            if bloom.is_value(key):
                added_keys.append(key)
        self.assertEqual(possible_keys, added_keys)

        for key in added_keys:
            bloom.remove(key)
            self.assertFalse(bloom.is_value(key))
        self.assertEqual(bloom.bloom_filter, 0)


if __name__ == '__main__':
    unittest.main()
