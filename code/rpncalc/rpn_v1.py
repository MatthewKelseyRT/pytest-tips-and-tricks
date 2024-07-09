from rpncalc.utils import calc

class RPNCalculator:
    def __init__(self) -> None:
        self.stack = []

    def run(self) -> None:
        while True:
            inp = input("> ")
            if inp == "q":
                return
            elif inp == "p":
                print(self.stack)
            else:
                self.evaluate(inp)

    def evaluate(self, inp: str):
        if inp.isdigit(): # Bug here as we can't enter negative numbers or floats
            n = float(inp)
            self.stack.append(n)
        elif inp in "+-*/": # Bug here as entered '+-' will go into here
            b = self.stack.pop() # Bug here as stack is empty and we can just hit enter
            a = self.stack.pop()
            res = calc(a, b, inp)
            self.stack.append(res)
            print(res)


if __name__ == "__main__":
    rpn = RPNCalculator()
    rpn.run()