class SegmentTree:
    def __init__(self, indices):
        self.n = len(indices)
        self.tree = [float('inf')] * (4 * self.n)
        self.build(1, 0, self.n - 1, indices)

    def build(self, node, l, r, indices):
        if l == r:
            self.tree[node] = indices[l]
        else:
            mid = (l + r) // 2
            self.build(2 * node, l, mid, indices)
            self.build(2 * node + 1, mid + 1, r, indices)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return float('inf')
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return min(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def update(self, node, l, r, idx, value):
        if l == r:
            self.tree[node] = value
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node, l, mid, idx, value)
            else:
                self.update(2 * node + 1, mid + 1, r, idx, value)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])


class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        sorted_baskets = sorted((baskets[i], i) for i in range(n))
        capacities = [b[0] for b in sorted_baskets]
        original_indices = [b[1] for b in sorted_baskets]
        index_to_position = {index: pos for pos, (_, index) in enumerate(sorted_baskets)}
        tree = SegmentTree(original_indices)
        unplaced = 0

        for fruit in fruits:
            left, right = 0, n - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if capacities[mid] >= fruit:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if pos == -1:
                unplaced += 1
                continue
            min_index = tree.query(1, 0, n - 1, pos, n - 1)
            if min_index == float('inf'):
                unplaced += 1
            else:
                update_pos = index_to_position[min_index]
                tree.update(1, 0, n - 1, update_pos, float('inf'))
        return unplaced
