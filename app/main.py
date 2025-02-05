from abc import ABC, abstractmethod


class IntegerRange:
    def __init__(self, name: str, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.protected_name = name

    def __get__(self, obj: any = None, obj_type: type = None) -> int:
        result = getattr(obj, self.protected_name)
        print(result)
        return result
    
    def __set__(self, obj: any, value: int) -> None:
        if self.is_value_in_range(value):
            raise ValueError("Value not in range")
        elif not isinstance(value, int): 
            raise TypeError("Wrong value type")
        else: 
            setattr(obj, self.protected_name, value)
    
    def is_value_in_range(self, value: int) -> bool:
        return value <= self.max_amount and value >= self.min_amount
    
    value = property(__get__, __set__)

class Visitor:
    def __init__(self, name: str, age: int, weight: int, height: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self) -> None:
        self.age = IntegerRange("age", 333, 111)
        self.height = IntegerRange("height", 444, 444)
        self.weight = IntegerRange("weight", 233, 5011)
        pass


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self) -> None:
        self.age = IntegerRange("age", 4, 14)
        self.height = IntegerRange("height", 80, 120)
        self.weight = IntegerRange("weight", 20, 50)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self) -> None:
        self.age = IntegerRange("age", 14, 60)
        self.height = IntegerRange("height", 120, 220)
        self.weight = IntegerRange("weight", 50, 120)


class Slide:
    def __init__(self, name: str, limitation_class: SlideLimitationValidator) -> None:
        self.name = name
        self.validator = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        try:
            self.validator.age = visitor.age
            self.validator.height = visitor.height
            self.validator.weight = visitor.weight
            return True
        except Exception as error:
            return False