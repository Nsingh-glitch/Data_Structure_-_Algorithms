class MyCalendarThree:

    def __init__(self):
        self.temp = {}
        self.ans = 0

    def book(self, st: int, et: int) -> int:
        self.temp[st] = self.temp.get(st, 0) + 1
        self.temp[et] = self.temp.get(et, 0) - 1

        cnt = 0

        for k, val in sorted(self.temp.items()):
            cnt += val
            self.ans = max(self.ans, cnt)

        return self.ans