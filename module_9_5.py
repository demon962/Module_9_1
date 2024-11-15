class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, end, step):
        if step == 0:
            raise StepValueError("Шаг указан неверно")
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
            raise StopIteration

        current_value = self.current
        self.current += self.step
        return current_value


try:
    iter1 = Iterator(100, 200, 0)  # Это вызовет исключение
except StepValueError:
    print('Шаг указан неверно')

    iter2 = Iterator(-5, 2, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 0, -1)
    iter5 = Iterator(10, 0, -1)

    for i in iter2:
        print(i, end=' ')
    print()

    for i in iter3:
        print(i, end=' ')
    print()

    for i in iter4:
        print(i, end=' ')
    print()

    for i in iter5:
        print(i, end=' ')
    print()
