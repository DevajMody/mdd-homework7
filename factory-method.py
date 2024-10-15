class ProductA:
    def operation(self) -> str:
        return "ProductA operation"

class ProductB:
    def operation(self) -> str:
        return "ProductB operation"

class Factory:
    def create_product(self, type: str):
        if type == "A":
            return ProductA()
        elif type == "B":
            return ProductB()

# Test Factory Method
factory = Factory()
product = factory.create_product("A")
print(product.operation())

product = factory.create_product("B")
print(product.operation())
