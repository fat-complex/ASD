class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bloom_filter: int = 0


    def hash1(self, str1):
        h = 0
        for c in str1:
            code = ord(c)
            h = (h * 17 + code) % self.filter_len
        return 1 << h

    def hash2(self, str1):
        h = 0
        for c in str1:
            code = ord(c)
            h = (h * 223 + code) % self.filter_len
        return 1 << h

    def add(self, str1):
        self.__set(self.hash1(str1))
        self.__set(self.hash2(str1))

    def remove(self, str1: str):
        if self.is_value(str1):
            self.__unset(self.hash1(str1))
            self.__unset(self.hash2(str1))

    def is_value(self, str1):
        return self.__is_set(self.hash1(str1)) and self.__is_set(self.hash2(str1))

    def __set(self, bit_mask):
        self.bloom_filter |= bit_mask

    def __unset(self, bit_mask):
        self.bloom_filter &= bit_mask

    def __is_set(self, bit_mask) -> bool:
        return bit_mask & self.bloom_filter != 0