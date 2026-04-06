class CombinationLock:
    def __init__(self, combination):
        self._correct_combination = combination
        self._entered_digits = []
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        self._entered_digits.append(digit)
        
        current_length = len(self._entered_digits)
        expected_part = self._correct_combination[:current_length]
        
        if self._entered_digits == self._correct_combination:
            self.status = 'OPEN'
        elif self._entered_digits == expected_part:
            self.status = "".join(map(str, self._entered_digits))
        else:
            self.status = 'ERROR'

if __name__ == "__main__":
    cl = CombinationLock([1, 2, 3, 4, 5])
    print(cl.status)

    cl.enter_digit(1)
    print(cl.status)

    cl.enter_digit(2)
    print(cl.status)

    cl.enter_digit(3)
    print(cl.status)

    cl.enter_digit(4)
    print(cl.status)

    cl.enter_digit(5)
    print(cl.status)