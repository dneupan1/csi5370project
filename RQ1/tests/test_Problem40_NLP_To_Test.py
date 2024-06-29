class NumArray:
    def __init__(self, nums):
        """
        Initializes the object with the integer array nums.
        """
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)  # Segment tree array
        self.build_tree(nums)
    
    def build_tree(self, nums):
        """
        Builds the segment tree based on the input array nums.
        """
        # Initialize leaves in the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, index, val):
        """
        Updates the value of nums[index] to be val.
        """
        # Update the leaf node
        pos = self.n + index
        self.tree[pos] = val
        
        # Update the internal nodes
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def sumRange(self, left, right):
        """
        Returns the sum of the elements of nums between indices left and right inclusive.
        """
        # Convert to segment tree indices
        l = self.n + left
        r = self.n + right
        sum_ = 0
        
        while l <= r:
            if l % 2 == 1:
                sum_ += self.tree[l]
                l += 1
            if r % 2 == 0:
                sum_ += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        
        return sum_