class InfiniteList:
    def __init__(self, *parts, fill_value=None):
        self.items = list(*parts)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index: int, item) -> None:
        if index >= len(self):
            for _ in range(len(self), index + 1):
                self.items.append(self.fill_value)
        self.items[index] = item

    def __str__(self):
        to_show = [str(element) for element in self.items]
        return ",".join(to_show)
    
infinite_list = InfiniteList(1, 2, 3, 4, fill_value=0)
print(infinite_list[2])
infinite_list[2] = 0
print(infinite_list[2])
infinite_list[4] = 5
infinite_list[7] = 8
