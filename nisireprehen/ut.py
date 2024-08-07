class MyClass:
    def __init__(self, b, c):
        self._b = b
        self._c = c

    def check_value(self, new_a):
        if new_a in (self._b, self._c):
            print(f"{new_a} is either {self._b} or {self._c}")
        else:
            print(f"{new_a} is neither {self._b} nor {self._c}")

# Example usage
my_instance = MyClass(10, 20)

my_instance.check_value(10)  # Output: "10 is either 10 or 20"
my_instance.check_value(30)  # Output: "30 is neither 10 nor 20"
