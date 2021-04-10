'''Design Skiplist

    William Ikenna-Nwosu (wiknwo)

    Design a Skiplist without using any built-in libraries.

    A Skiplist is a data structure that takes O(log(n)) 
    time to add, erase and search. Comparing with treap and 
    red-black tree which has the same function and 
    performance, the code length of Skiplist can be 
    comparatively short and the idea behind Skiplists are 
    just simple linked lists.

    You can see there are many layers in the Skiplist. Each 
    layer is a sorted linked list. With the help of the top 
    layers, add , erase and search can be faster than O(n). 
    It can be proven that the average time complexity for 
    each operation is O(log(n)) and space complexity is 
    O(n).

    To be specific, your design should include these functions:

    - bool search(int target) : Return whether the target 
    exists in the Skiplist or not.

    - void add(int num): Insert a value into the SkipList. 

    - bool erase(int num): Remove a value in the Skiplist. 
    If num does not exist in the Skiplist, do nothing and 
    return false. If there exists multiple num values, 
    removing any one of them is fine.

    - Note that duplicates may exist in the Skiplist, your 
    code needs to handle this situation.

    See more about Skiplist : https://en.wikipedia.org/wiki/Skip_list
'''
class Skiplist:

    def __init__(self):
        self.skiplist = {}        

    def search(self, target: int) -> bool:
        return target in self.skiplist
    
    def add(self, num: int) -> None:
        self.skiplist[num] = self.skiplist.get(num, 0) + 1
                    
    def erase(self, num: int) -> bool:
        if num not in self.skiplist: 
            return False 
        
        self.skiplist[num] -= 1
        
        if self.skiplist[num] == 0:
            del self.skiplist[num]
        return True 
        
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)