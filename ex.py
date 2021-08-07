
class B:
    pass
class A(type):
    def __new__(
        meta,
        name,
        bases,
        attributes
    ):
        print(meta)
        print(name)
        print(bases)
        print(attributes)

if __name__ == "__main__":
    a = A(
        name="Hello",
        bases=("object":"B"),
        attributes={
            "test": 1
        }
    )
    print(dir(a))
