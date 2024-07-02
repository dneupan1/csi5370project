class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 4 * self.n  # Space allocation for segment tree
        self.buildTree(nums, 0, 0, self.n - 1)
    
    def buildTree(self, nums, treeIndex, lo, hi):
        """Build the tree with initial array values."""
        if lo == hi:
            self.tree[treeIndex] = nums[lo]
            return
        mid = (lo + hi) // 2
        self.buildTree(nums, 2 * treeIndex + 1, lo, mid)
        self.buildTree(nums, 2 * treeIndex + 2, mid + 1, hi)
        self.tree[treeIndex] = self.tree[2 * treeIndex + 1] + self.tree[2 * treeIndex + 2]

    def update(self, index: int, val: int) -> None:
        """Updates the value of nums[index] to be val."""
        def _update(index, val, treeIndex=0, lo=0, hi=None):
            if hi is None:
                hi = self.n - 1
            if lo == hi:
                self.tree[treeIndex] = val
                return
            mid = (lo + hi) // 2
            if index <= mid:
                _update(index, val, 2 * treeIndex + 1, lo, mid)
            else:
                _update(index, val, 2 * treeIndex + 2, mid + 1, hi)
            self.tree[treeIndex] = self.tree[2 * treeIndex + 1] + self.tree[2 * treeIndex + 2]
        _update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        """Returns the sum of the elements of nums between indices left and right inclusive."""
        def _sumRange(left, right, treeIndex=0, lo=0, hi=None):
            if hi is None:
                hi = self.n - 1
            if left > hi or right < lo:
                return 0
            if left <= lo and right >= hi:
                return self.tree[treeIndex]
            mid = (lo + hi) // 2
            return _sumRange(left, right, 2 * treeIndex + 1, lo, mid) + \
                   _sumRange(left, right, 2 * treeIndex + 2, mid + 1, hi)
        return _sumRange(left, right)

