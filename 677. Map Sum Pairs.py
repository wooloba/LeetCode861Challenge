####################
#   Yaozhi Lu      #
#   Nov 14 2018    #
####################

#Origin:https://leetcode.com/problems/map-sum-pairs/

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.data[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        theSum = 0
        for key,val in self.data:
            if key[0:len(prefix)] == prefix:
                theSum += val

        return theSum


def if __name__ == "__main__":
    
    # Your MapSum object will be instantiated and called as such:
    obj = MapSum()
    obj.insert("apple", 3)
    print(obj.sum('app'))

main()