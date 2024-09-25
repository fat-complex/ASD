class FixedBitsDict:
    def __init__(self, key_size_in_bits):
        self.key_size = key_size_in_bits
        self.keys = 0
        self.values = [None] * self.key_size

    def put(self, key, value):
        self.keys |= (1 << key)
        self.values[key] = value


    def remove(self, key):
        if self.is_key(key):
            self.keys &= ~(1 << key)
            self.values[key] = None

    def is_key(self, key):
        return (1 << key) & self.keys != 0

    def get(self, key):
        if self.is_key(key):
            return self.values[key]
        return None

    def empty(self):
        return self.keys == 0