class TimeMap:

    def __init__(self):
        self.backing = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if not key:
            return

        if not key in self.backing:
            self.backing[key] = []
        self.backing[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.backing:
            return ""

        entries = self.backing[key]

        def search(left: int, right: int) -> str:
            if left > right:
                return ""

            mid = (left + right) // 2
            mid_val, mid_ts = entries[mid]

            if mid_ts > timestamp:
                return search(left, mid - 1)

            # mid_ts <= timestamp, mid is a candidate; try right side for a later one
            right_candidate = search(mid + 1, right)
            return right_candidate if right_candidate != "" else mid_val

        return search(0, len(entries) - 1)