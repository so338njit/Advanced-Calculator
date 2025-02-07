class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation # stores the operation function for later recall

    def get_result(self):
        # Recalls the stored operation with a and b
        return self.operation(self.a, self.b)
