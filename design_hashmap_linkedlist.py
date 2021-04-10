# LinkedList Implementation
class LinkedList:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.constant = 1000
        self.hashmap = [None] * self.constant

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.constant # Get the index we want to place the key into
        if self.hashmap[index] is None:
            self.hashmap[index] = LinkedList(key, value)
        else:
            current = self.hashmap[index]
            while True:
                # Update the current key and value if the key matches
                if current.pair[0] == key:
                    current.pair = (key, value) # Update
                    return
                
                # If you are at the end of the hashmap 
                # and the key has not been found
                # make the last entry the new key-value pair
                if current.next == None:
                    break
                current = current.next
            current.next = LinkedList(key, value)
                
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.constant # Get the index of the key in the hashmap
        current = self.hashmap[index]
        
        # Iterate through LinkedList to find node with specified key
        while current:
            # If you find entry with specified key then return it
            if current.pair[0] == key:
                return current.pair[1]
            else:
                # If key not found then go to next node
                current = current.next
        return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.constant
        current = self.hashmap[index]
        
        if current is None:
            return
        
        previous, current = current, current.next
        key_, value_ = previous.pair
        
        # Found key matching node to be removed
        if key_ == key:
            self.hashmap[index] = current
            return

        while current is not None:
            key_, value = current.pair
            
            if key_ == key:
                previous.next = current.next
                return
            previous, current = current, current.next

            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)