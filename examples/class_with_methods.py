class A:
    a: int = 0

    def __init__(self) -> None:
        self.x: int = 1
        return

    def foo(self) -> int:
        return self.x

    @classmethod
    def bar(cls) -> int:
        return cls.a
