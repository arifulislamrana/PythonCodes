class Count:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        self.num += 1
        if val <= 10:
            return val
        else:
            raise StopIteration


it = Count()
print(it.__iter__())
print(next(it))
for i in it:
    print(i)
