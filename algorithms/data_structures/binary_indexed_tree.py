
class BinaryIndexedTree(object):
    """
    Implementation of Binary Indexed Tree
    for range sum queries and single index updates.
    """

    def __init__(self, max_index=10):
        """
        max_index = N where N is the number of elements to be stored.
        """
        self.max_index = max_index
        self.tree = []
        self.element_list = []
        for i in range(self.max_index+1):
            self.tree.append(0)
            if(i is not 0):
                self.element_list.append(0)

    def create_from_list(self,element_list):
        """
        An element at index i in element_list is stored at index i+1 in tree.

        Index 0 in the tree is not used and can contain any garbage value.

        Time Complexity: O(N*lg N)
        """
        self.element_list = element_list
        self.max_index = len(element_list)
        self.tree = []

        for i in range(self.max_index+1):
            self.tree.append(0)

        for index in range(1,self.max_index+1):
            self.tree_update(index,self.element_list[index-1])

    def is_valid(self, index):
        """
        Returns true if the index is valid for a prefix sum query on the tree
        """
        return index >= 0 and index <= self.max_index

    def prefix_sum(self, index):
        """
        Time Complexity: O(lg N)
        """
        if(self.is_valid(index)):
            pre_sum = 0
            while(index > 0):
                pre_sum += self.tree[index]
                index -= (index&(-index))
            return pre_sum
        return -1

    def update(self, index, elem):
        """
        Updates the element list at index

        Corresponding binary indexed tree is updated at index+1

        Time Complexity: O(lg N)
        """
        if(index is not 0 and self.is_valid(index)):
            temp = self.element_list[index]
            self.element_list[index] = elem
            self.tree_update(index+1,elem-temp)

    def tree_update(self, index, diff):
        """
        Updates the Binary Indexed Tree at index

        Time Complexity: O(lg N)
        """
        while(index <= self.max_index):
            self.tree[index] += diff
            index += (index &(-index))

    def range_query(self, left_index, right_index):
        """
        left_index and right_index are indices in element_list (both inclusive)

        Returns sum(element_list[left_index:right_index+1])

        Time Complexity: O(lg N)
        """
        if(self.is_valid(left_index) and self.is_valid(right_index+1)):
            return self.prefix_sum(right_index+1)-self.prefix_sum(left_index)
        return -1
