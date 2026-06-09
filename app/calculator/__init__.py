from app.operations import Addition, Subtraction, Multiplication, Division


OPERATIONS = {
    "add": Addition,
    "subtract": Subtraction,
    "multiply": Multiplication,
    "divide": Division,
}


class Calculator:
    def __init__(self):
        self.operations = OPERATIONS

    def get_number(self, prompt: str) -> float:
        while True:
            value = input(prompt).strip()
            try:
                return float(value)
            except ValueError:
                print(f"  Invalid input '{value}'. Please enter a number.")

    def get_operation(self) -> str:
        valid = ", ".join(self.operations.keys())
        while True:
            op = input(f"Operation ({valid}) or 'quit' to exit: ").strip().lower()
            if op == "quit":
                return op
            if op in self.operations:
                return op
            print(f"  Unknown operation '{op}'. Choose from: {valid}")

    def calculate(self, operation: str, a: float, b: float) -> float:
        op_class = self.operations[operation]
        return op_class.execute(a, b)

    def run(self):
        print("=" * 40)
        print("  Welcome to the Python Calculator!")
        print("  Type 'quit' at any time to exit.")
        print("=" * 40)

        while True:
            op = self.get_operation()
            if op == "quit":
                print("Goodbye!")
                break

            a = self.get_number("Enter first number: ")
            b = self.get_number("Enter second number: ")

            try:
                result = self.calculate(op, a, b)
                print(f"  Result: {a} {op} {b} = {result}\n")
            except ValueError as e:
                print(f"  Error: {e}\n")