class HashTable:
    def __init__(self,size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return 
        self.table[index].append([key, value])

    def get(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
        
    def remove(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return 
            
    def resize(self):
        print("🔄 Resizing from", self.size, "to", self.size * 2)
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        # Rehash all old values
        for slot in old_table:
            for key, value in slot:
                self.insert(key, value)

    def display(self):
        for i, slot in enumerate(self.table):
            print(i, ":", slot)
            
ht = HashTable()
ht.insert("name", "tanish")
ht.insert("age",20)
print(ht.get("name"))
print(ht.get("age"))
