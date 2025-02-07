from abc import ABC


class IntegerRange:
    def __init__(self, name: str, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.protected_name = "_" + name
        self._value = None

    def __get__(self, obj: any = None, obj_type: type = None) -> int:
        return getattr(obj, self.protected_name)

    def __set__(self, obj: any, value: int) -> None:
        if not self.is_value_in_range(value):
            raise ValueError("Value not in range")
        elif not isinstance(value, int):
            raise TypeError("Wrong value type")
        else:
            setattr(obj, self.protected_name, value)

    def is_value_in_range(self, value: int) -> bool:
        return self.max_amount >= value >= self.min_amount

    value = property(__get__, __set__)


class Visitor:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self) -> None:
        pass


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self) -> None:
        super().__init__()

    age = IntegerRange("age", 4, 14)
    height = IntegerRange("height", 80, 120)
    weight = IntegerRange("weight", 20, 50)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self) -> None:
        super().__init__()

    age = IntegerRange("age", 14, 60)
    height = IntegerRange("height", 120, 220)
    weight = IntegerRange("weight", 50, 120)


class Slide:
    def __init__(self, name: str, limitation_class: type) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        print(visitor.__dict__)
        try:
            self.limitation_class.age = visitor.age
            self.limitation_class.height = visitor.height
            self.limitation_class.weight = visitor.weight
            return True
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        return False


visitor = Visitor("Yan", 255, 222, 180)
Slide("slide", AdultSlideLimitationValidator).can_access(visitor)