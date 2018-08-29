class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key not in self.dict:
            self.dict.update({key:0})
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.dict:
            self.dict.pop(key, None)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key not in self.dict:
            return False
        
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
