import time
st = time.process_time()

class Hash:
    def __init__(self, m, collision, function=1):
        self.size = m
        self.table = [None] * self.size
        self.type = collision
        self.func = function

    def hash(self, value):
        return value % self.size

    def insert(self, value):
        hashkey = self.hash(value)
        if self.type == 1:
            if self.table[hashkey] is None:
                self.table[hashkey] = list([value])
            else:
                self.table[hashkey] = [value] + self.table[hashkey]
        elif self.type == 2:
            while self.table[hashkey] is not None:
                hashkey = self.increment_key(hashkey)
            self.table[hashkey] = value
        elif self.type == 3:
            collision = 1
            original_hash = hashkey
            while self.table[hashkey] is not None:
                hashkey = self.quadric_key(original_hash, collision)
                collision += 1
            self.table[hashkey] = value
        else:
            collision = 1
            original_hash = hashkey
            h2 = (value % (self.size - 1)) + 1
            while self.table[hashkey] is not None:
                hashkey = self.double_key(original_hash, collision, h2)
                collision += 1
            self.table[hashkey] = value

    def double_key(self, key, collision, h2):
        return (key + collision * h2) % self.size

    def quadric_key(self, key, collision):
        return (key + collision+ collision * collision) % self.size

    def increment_key(self, key):
        return (key + 1) % self.size

    def delete(self, value):
        if self.type == 1:
            hashkey = self.hash(value)
            for val in self.table[hashkey]:
                if val == value:
                    self.table[hashkey].remove(val)

        else:
            for i in range(self.size):
                if self.table[i] == value:
                    self.table[i] = 'Deleted'

    def search(self, value):
        if self.type == 1:
            hashkey = self.hash(value)
            return hashkey
        for i in range(self.size):
            if self.table[i] == value:
                return i

    def size(self):
        return self.size

    def print_table(self):
        newtab = []
        for item in self.table:
            newtab.append(item)
        n = len(newtab)
        if self.type == 1:
            for a in range(n):
                if newtab[a] is not None and len(newtab[a]) == 1:
                    x = iter(newtab[a])
                    newtab[a] = next(x)
        print(newtab)


a = [int(x) for x in input().split()]
m = a[0]
c = a[1]
Table = Hash(m, c)
for i in range(2, len(a)):
    Table.insert(a[i])
Table.print_table()
et = time.process_time()

res = et - st
print('CPU Execution time:', res, 'seconds')
while True:
    try:
        b = [int(x) for x in input().split()]
        if b[0] == -1:
            break
        elif b[0] == 0:
            Table.insert(b[1])
            Table.print_table()
        elif b[0] == 1:
            print(Table.search(b[1]))
        else:
            Table.delete(b[1])
            Table.print_table()
    except EOFError:
        break
