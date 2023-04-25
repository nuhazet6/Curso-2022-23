class InfiniteList:
    def __init__(self, *parts, fill_value=None):
        self.parts = list(parts)
        self.fill_value = fill_value

    def __setitem__(self, index: int, part: str) -> None:

        new_elements = [self.fill_value for _ in range(index - len(self))]
        self.parts.extend(new_elements)
        self.parts[index] = part

    def __getitem__(self, index: int) -> str:
        return self.parts[index]

    def __len__(self):
        return len(self.parts)


infinite_list = InfiniteList(1, 2, 3, 4, fill_value=0)
print(infinite_list[2])
infinite_list[2] = 0
print(infinite_list[2])
infinite_list[4] = 5
infinite_list[7] = 8
