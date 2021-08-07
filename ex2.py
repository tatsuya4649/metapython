class A(type):
    def __new__(
        meta,
        name,
        bases,
        attributes
    ):
        print("__new__")
        print(meta)
        print(name)
        print(bases)
        print(attributes)
        
        if attributes["number"] < 1000:
            raise ValueError(
                "number must be greater than 10000"
            )
        attributes["test"] = "test"
        return type.__new__(
            meta,
            name,
            bases,
            attributes
        )
    def __init__(
        meta,
        name,
        bases,
        attributes
    ):
        print("__init__")
        print(meta)
        print(name)
        print(bases)
        print(attributes)
        # No Added
        attributes["test2"] = "test2"

class B(metaclass=A):
    number = 10000
    def __init__(self):
        print(self.test)
    def bfunction(self):
        ...

b = B()
