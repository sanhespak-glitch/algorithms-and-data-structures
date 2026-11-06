class HashTable:
    def __init__(self):
        self.a = [[] for i in range(8)]
        self.count = 0

    def hash_key(self, key):
        h = 0
        for c in key:
            h = (h * 131 + ord(c)) % 1000000007
        return h

    def put(self, key, value):
        j = self.hash_key(key) % len(self.a)

        for p in self.a[j]:
            if p[0] == key:
                p[1] = value
                return

        self.a[j].append([key, value])
        self.count += 1

        if self.count > len(self.a) * 2:
            old = self.a
            self.a = [[] for i in range(len(old) * 2)]

            for bucket in old:
                for k, v in bucket:
                    j = self.hash_key(k) % len(self.a)
                    self.a[j].append([k, v])

    def get(self, key):
        j = self.hash_key(key) % len(self.a)

        for k, v in self.a[j]:
            if k == key:
                return v

        return "Error"

    def delete(self, key):
        j = self.hash_key(key) % len(self.a)

        for i in range(len(self.a[j])):
            if self.a[j][i][0] == key:
                v = self.a[j][i][1]
                self.a[j].pop(i)
                self.count -= 1
                return v

        return "Error"


q = int(input())
d = HashTable()

for i in range(q):
    s = input().split()

    if s[0] == "put":
        d.put(s[1], int(s[2]))

    elif s[0] == "get":
        print(d.get(s[1]))

    elif s[0] == "del":
        print(d.delete(s[1]))

    elif s[0] == "size":
        print(d.count)