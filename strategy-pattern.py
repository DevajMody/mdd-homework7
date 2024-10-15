class StrategyA:
    def do_algorithm(self, data: list) -> list:
        return sorted(data)

class StrategyB:
    def do_algorithm(self, data: list) -> list:
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, data: list):
        return self.strategy.do_algorithm(data)

# Test Strategy Pattern
context = Context(StrategyA())
print(context.execute([3, 1, 2]))

context = Context(StrategyB())
print(context.execute([3, 1, 2]))
