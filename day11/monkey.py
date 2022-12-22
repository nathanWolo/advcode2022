class Monkey:
    items: list[int]
    operation: str
    val: int
    test_criteria: int
    targets: list[int]

    def __init__(self, items, operation, test_criteria: int, targets: list[int], val):
        self.operation = operation
        self.test_criteria = test_criteria
        self.items = items
        self.targets = targets
        self.val = val
    def __str__(self):
        return f"Monkey {self.items}, {self.operation}, {self.test}, {self.targets}"

    def operate(self, item):
        if self.operation == '*':
            return item * self.val
        elif self.operation == '+':
            return item + self.val
        elif self.operation == '**2':
            return item ** 2
        return self.operation(item)
    def test(self, item):
        return item % self.test_criteria ==0