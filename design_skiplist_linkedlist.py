from random import randrange

class HeaderNode:
    def __init__(self):        
        # The columns of data nodes are known as towers. 
        # Towers are linked together by the down reference 
        # in the data node.
        self.down = None 
        
        # Each Horizontal Group of Data Nodes Is a Level
        # If you look closely, you will notice that each 
        # level is actually an ordered linked list of data 
        # nodes where the order is maintained by the key.
        self.next = None

class DataNode:
    def __init__(self, val):
        self.val = val
        self.down = None
        self.next = None
    
class Skiplist:

    def __init__(self):
        self.head = None        

    def search(self, target: int) -> bool:
        current = self.head
        
        # Traverse skiplist
        while current:
            if current.next == None:
                current = current.down
            else:
                if current.next.val == target:
                    return current.next.val
                else:
                    #  If the key we are looking for is 
                    # less than the key contained in the data 
                    # node, we know that no other data node on 
                    # that level can contain our key since everything 
                    # to the right has to be greater. In that case, we 
                    # drop down one level in that tower. 
                    if target < current.next.val:
                        current = current.down
                    
                    # On the other hand, as long as there are 
                    # data nodes on the current level with key 
                    # values less than the key we are looking for, 
                    # we continue moving to the next node
                    else:
                        current = current.next
                        
        # If no such level exists (we drop to None), 
        # we have discovered that the key is not present 
        # in our skip list. We break out of the loop 
        # and return None. 
        return None

    def flip(self):
        return randrange(2)
    
    def add(self, num: int) -> None:
        # Check to see if this is first node being added to skiplist
        if self.head == None:
            self.head = HeaderNode()
            tmp = DataNode(num)
            self.head.next = tmp
            top = tmp
            # If we are adding to the head of the list, 
            # a new header node as well as data node must 
            # be created. The iteration in lines continues 
            # as long as the flip method returns a 1 (the 
            # coin toss returns heads). Each time a new 
            # level is added to the tower, a new data node 
            # and a new header node are created.
            while self.flip() == 1:
                newhead = HeaderNode()
                tmp = DataNode(num)
                tmp.down = top
                newhead.next = tmp
                newhead.down = self.head
                self.head = newhead
                top = tmp
        # In the case of a non-empty skip list 
        # we need to search for the insert position 
        # as described above. Since we have no way of 
        # knowing how many data nodes will be added 
        # to the tower, we need to save the insert points 
        # for every level that we enter as part of the 
        # search process.  
        else:
            tower = [] # Stack to hold tentative insert points  
            current = self.head
            
            while current:
                if current.next is None:
                    tower.append(current)
                    current = current.down
                else:
                    if current.next.val > num:
                        tower.append(current)
                        current = current.down
                    else:
                        current = current.next
            lowest_level = tower.pop()
            tmp = DataNode(num)
            tmp.next = lowest_level.next
            lowest_level.next = tmp
            top = tmp
        
            while self.flip() == 1:
                if not tower: # Check if stack is empty
                    newhead = HeaderNode()
                    tmp = DataNode(num)
                    tmp.down = top
                    newhead.next = tmp
                    newhead.down = self.head
                    self.head = newhead
                    top = tmp
                else:
                    next_level = tower.pop()
                    tmp = DataNode(num)
                    tmp.down = top
                    tmp.next = next_level.next
                    next_level.next = tmp
                    top = tmp
                
                    
    def erase(self, num: int) -> bool:
        current = self.head
        erased = False
        
        # Traverse skiplist
        while current:
            if current.next == None:
                current = current.down
            else:
                if current.next.val == num:
                    # del current.next
                    erased = True
                    # delete node
                    return erased
                else:
                    if num < current.next.val:
                        current = current.down
                    else:
                        current = current.next
        return erased
# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)