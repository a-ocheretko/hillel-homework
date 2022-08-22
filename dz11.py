class HashTable:

    def __init__(self, size):
        self.size = size
        self.slots = [None for i in range(self.size)]
        self.data = [None for i in range(self.size)]

    @staticmethod
    def hash_function(key, size):
        return key % size

    def put(self, key, data):

        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next = self.rehash(hash_value, self.size)
                while self.slots[next] is not None and self.slots[next] != key:
                    next = self.rehash(next, self.size)

                if self.slots[next] is None:
                    self.slots[next] = key
                    self.data[next] = data
                else:
                    self.data[next] = data

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        start = self.hash_function(key, self.size)

        data = None
        stop = False
        found = False
        position = start
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == start:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __str__(self):
        hash_table = {i: self[i] for i in self.slots if i is not None}
        return str(hash_table)


hshtbl = HashTable(10)
hshtbl[33] = 'Apple'
hshtbl[95] = 'Samsung'
hshtbl[51] = 'Xiaomi'
print(hshtbl)

hshtbl[20] = 'Lenovo'
hshtbl[33] = 'Huawei'
print(hshtbl)

