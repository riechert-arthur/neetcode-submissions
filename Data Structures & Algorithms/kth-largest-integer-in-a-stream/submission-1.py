class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self._heap_build() 
        self.k = k

        while len(self.heap) > k:
            self.pop()

    def add(self, val: int) -> int:
        self.heap.append(val)
        self._heap_up(len(self.heap) - 1)
        if len(self.heap) > self.k:
            self.pop()
        print(self.heap)
        return self.heap[0]

    def pop(self) -> int:
        self._swap(-1, 0)
        self.heap = self.heap[0:len(self.heap) - 1]
        self._heap_down(0)

    def _heap_build(self):
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self._heap_down(i)
  
    def _heap_down(self, i_parent: int):
        n = len(self.heap)
        i_left  = self._get_left_child_i(i_parent)
        i_right = self._get_right_child_i(i_parent)

        i_smallest = i_parent

        if i_left < n and self.heap[i_left] < self.heap[i_smallest]:
            i_smallest = i_left

        if i_right < n and self.heap[i_right] < self.heap[i_smallest]:
            i_smallest = i_right

        if i_smallest == i_parent:
            return

        self._swap(i_parent, i_smallest)
        self._heap_down(i_smallest)


    def _heap_up(self, i_child: int):

        i_parent = self._get_parent_i(i_child)

        if i_child <= 0:
            return

        v_child = self.heap[i_child]
        v_parent = self.heap[i_parent]

        if v_child < v_parent:
            self._swap(i_parent, i_child)
            self._heap_up(i_parent)

        return

    def _get_left_child_i(self, i: int) -> int:
        return 2 * i + 1

    def _get_right_child_i(self, i: int) -> int:
        return 2 * i + 2

    def _get_parent_i(self, i: int) -> int:
        return (i - 1) // 2

    def _swap(self, i_initial, i_final):
        temp = self.heap[i_initial]
        self.heap[i_initial] = self.heap[i_final]
        self.heap[i_final] = temp