class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key] if self.timeMap[key] else [(0,"")]
        l = 0
        r = len(values) - 1
        print(values)
        print(l)
        print(r)
        prev_entry = (0,"")
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            midTimestamp = values[mid][0]
            print(midTimestamp)
            if midTimestamp <= timestamp:
                prev_entry = values[mid]
                l = mid + 1
            else:
                r = mid -1
        print(prev_entry)
        return prev_entry[1]