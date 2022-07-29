"""
https://docs.python.org/ko/3/library/enum.html
열거형(enumeration)은 고유한 상숫값에 연결된 기호 이름(멤버)의 집합입니다.
열거형 내에서, 멤버를 아이덴티티로 비교할 수 있고, 열거형 자체는 이터레이트 될 수 있습니다.

참고: Enum 멤버의 케이스
열거형은 상수를 나타내는 데 사용되기 때문에 열거형 멤버에 대해 대문자(UPPER_CASE) 이름을 사용하는 것이 좋으며,
예제에서는 이 스타일을 사용합니다.

Enum 모듈의 내용
# enum.Enum
# 열거형 상수를 만들기 위한 베이스 클래스. 대체 구성 문법은 함수형 API 섹션을 참조하십시오.

# enum.IntEnum
# int의 서브 클래스이기도 한 열거형 상수를 만들기 위한 베이스 클래스.

# enum.IntFlag
# IntFlag 멤버십을 잃지 않고 비트 연산자를 사용하여 결합할 수 있는 열거형 상수를 만들기 위한 베이스 클래스.
# IntFlag 멤버도 int의 서브 클래스입니다.

# enum.Flag
# Flag 멤버십을 잃지 않고 비트 연산을 사용하여 결합할 수 있는 열거형 상수를 만들기 위한 베이스 클래스.

# enum.unique()
# 한 값에 하나의 이름 만 연결되도록 하는 Enum 클래스 데코레이터.

# enum.auto
# 인스턴스는 Enum 멤버에 적절한 값으로 바뀝니다. 기본적으로, 초깃값은 1부터 시작합니다.
# 버전 3.6에 추가: Flag, IntFlag, auto
"""
# ==========================================================================================
# 1. Enum 만들기
# 열거형은 class 문법을 사용하여 작성되므로 쉽게 읽고 쓸 수 있습니다.
# 대체 작성 방법은 함수형 API에 설명되어 있습니다.
# 열거형을 정의하려면, 다음과 같이 Enum을 서브 클래스 하십시오.
# 시작 번호로 0이 아니라 1을 기본값으로 설정하는 이유는 0이 불리언 의미로 False 이지만,
# 열거형 멤버는 모두 True 로 평가되기 때문입니다.
# 멤버 값은 아무것이나 될 수 있습니다: int, str 등.
# 정확한 값이 중요하지 않다면, auto 인스턴스를 사용할 수 있으며 적절한 값이 선택됩니다.
# auto를 다른 값과 혼합 할 경우 주의를 기울여야 합니다.
# Color 클래스는 열거형(enumeration) (또는 enum) 입니다.
# Color.RED, Color.GREEN 등의 어트리뷰트는 열거형 멤버(enumeration members)(또는 enum members)이며 기능상 상수입니다.
# 열거형 멤버에는 이름(names)과 값(values)이 있습니다 (Color.RED의 이름은 RED, Color.BLUE의 값은 3, 등)

from enum import Enum, auto
print('*' * 50)


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 참고
# class 문법을 사용하여 Enum을 만들더라도, Enum은 일반적인 파이썬 클래스가 아닙니다.
# 자세한 내용은 열거형은 어떻게 다릅니까? 를 참조하십시오.
# https://docs.python.org/ko/3/library/enum.html#how-are-enums-different

# 열거형 멤버는 사람이 읽을 수 있는 문자열 표현을 갖습니다
print(Color.RED) # Color.RED

# repr에는 더 자세한 정보가 있습니다
print(repr(Color.RED)) # <Color.RED: 1>

# 열거형 멤버의 형은 그것이 속한 열거형입니다
print(type(Color.RED)) # <enum 'Color'>
print(isinstance(Color.RED, Color)) # True

# Enum 멤버에는 항목 이름만 포함하는 프로퍼티와, 항목의 값만 포함하는 프로퍼티가 있습니다.
print(Color.RED.name) # RED
print(Color.RED.value) # 1

# 열거형은 정의 순서로 이터레이션을 지원합니다:
for c in Color:
    print(c)

# Color.RED
# Color.GREEN
# Color.BLUE

# 열거형 멤버는 해시 가능하므로, 딕셔너리와 집합에 사용할 수 있습니다:
colors = {}
colors[Color.RED] = 'red color'
colors[Color.GREEN] = 'green color'
print(colors)
print(colors == {Color.RED: 'red color', Color.GREEN: 'green color'}) # True

# 열거형 멤버와 그들의 어트리뷰트에 프로그래밍 방식으로 액세스하기
# 때로는 프로그래밍 방식으로 열거형의 멤버에 액세스하는 것이 유용합니다
# (즉, 프로그램 작성 시간에 정확한 색상을 알 수 없어서 Color.RED를 쓸 수 없는 상황). Enum는 그런 액세스를 허용합니다:
Color(1)
# <Color.RED: 1>

Color(2)
# <Color.GREEN: 2>

# 고유한 열거형 값 보장하기
# 기본적으로, 열거형은 여러 이름을 같은 값에 대한 별칭으로 허용합니다.
# 이 동작이 바람직하지 않을 때, 다음 데코레이터를 사용하여 각 값이 열거에서 한 번만 사용되도록 보장할 수 있습니다:
# @enum.unique

from enum import Enum, unique

def test_unique_enum():
    @unique
    class MisTake(Enum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 3

# test_unique_enum()
# ValueError: duplicate values found in <enum 'MisTake'>: FOUR -> THREE

# 정확한 값이 중요하지 않으면, auto를 사용할 수 있습니다.
# auto() 함수를 사용하면 기존 상수에 어떤 숫자가 할당해놨었는지 구애 받지 않고 새로운 상수를 추가할 수 있는 장점도 있습니다
# 뿐만 아니라, Enum 클래스의 _generate_next_value_() 메서드를 오버라이드(override)하면 숫자가 아닌
# 다른 값을 자동 할당할 수 있습니다.
# 예를 들어, 상수의 이름과 동일한 문자열을 상수의 값으로 자동 할당할 수 있습니다.
print('*' * 50)
class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print(list(Color))
# [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

class StudyClass(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    PYTHON = auto()
    JAVA_SCRIPT = auto()

print(list(StudyClass))
# [<StudyClass.PYTHON: 'PYTHON'>, <StudyClass.JAVA_SCRIPT: 'JAVA_SCRIPT'>]


# 이터레이션
# 열거형 멤버를 이터레이트 해도 별칭은 제공되지 않습니다:
# 특수 어트리뷰트 __members__는 이름에서 멤버로의 읽기 전용 순서 있는 매핑입니다.
# 별칭을 포함하여, 열거형에 정의된 모든 이름을 포함합니다:

class Shape(Enum):
    SQUARE = 1
    DIAMOND = 2
    CIRCLE = 3

print(list(Shape))
# [<Shape.SQUARE: 1>, <Shape.DIAMOND: 2>, <Shape.CIRCLE: 3>]

for name, member in Shape.__members__.items():
    print(f"{name} / {member} / {member.value}")

# SQUARE / Shape.SQUARE / 1
# DIAMOND / Shape.DIAMOND / 2
# CIRCLE / Shape.CIRCLE / 3

# 비교
# 열거형 멤버는 아이덴티티로 비교됩니다:
print(Color.RED == Color.RED) # True
print(Color.RED == Color.BLUE) # False
print(Color.RED is not Color.BLUE) # True

# 열거형 값 사이의 순서 비교는 지원되지 않습니다. 열거형 멤버는 정수가 아닙니다 (그러나 아래의 IntEnum을 참조하십시오):
try:
    print(Color.RED < Color.BLUE)
except TypeError as e:
    print(e)
    # '<' not supported between instances of 'Color' and 'Color'

# 그러나 동등 비교는 지원됩니다.
print(Color.BLUE == Color.RED)
# False
print(Color.BLUE != Color.RED)
# True
print(Color.BLUE == Color.BLUE)
# True

# Enum 클래스를 사용한 서브클래스의 멤버 변수의 순서비교는 지원되지 않으나, IntEnum 은 지원됩니다.
# 게다가 다른 정수 열거형도 서로 비교할 수 있습니다
from enum import IntEnum
class Size(IntEnum):
    M = 1
    L = 2
    XL = 3

print(Size.M < Size.L) # True
print(Size.M > Size.L) # False


# Enum 을 함수로 생성하기
def test_make_enum():
    # return types.new_class(name, (enum_type, Enum), exec_body=exec_body)
    from typing import Tuple
    import types

    def create_enum(name: str, choices: list[Tuple], enum_type=str) -> Enum:
        def exec_body(ns: dict):
            for val, enum_name, _ in choices:
                assert enum_name.isupper(), "enum name should be uppercase"
                ns[enum_name] = val

        return types.new_class(name, (enum_type, Enum), exec_body=exec_body)

    class User:
        LANGUAGE_CHOICES = [
            ("en", "EN", "English"),
            ("kr", "KR", "Korean(한국어)")
        ]

        LanguageEnum = create_enum(name="LanguageEnum", choices=LANGUAGE_CHOICES)

    user = User()
    print(user.LanguageEnum) # <enum 'LanguageEnum'>
    print(user.LanguageEnum.EN) # LanguageEnum.EN
    print(user.LanguageEnum.EN.value) # en

    # print(user.LanguageEnum.__members__.items())

test_make_enum()

# 함수형으로 정의하기
Skill = Enum("Skill", "HTML CSS JS")
print(list(Skill))
# [<Skill.HTML: 1>, <Skill.CSS: 2>, <Skill.JS: 3>]


# MixIn
# enum 을 사용할 때 한 가지 불편할 수 있는 점은 상수의 이름이나 값에 접근할 때 name, value 를 사용해야 한다는 점이다.
# 왜냐하면 모든 상수는 결국 해당 enum 타입의 인스턴스이기 때문입니다.
# 하지만 enum 타입을 사용해서 코딩을 하다보면, 매번 name이나 value를 사용하는 것이 귀찮다.
# 이럴 때는 enum mixin(믹스인) 기법을 활용하여 str을 확장하는 enum 클래스를 작성합니다.
print('*' * 50)
from typing import Any

class StrEnum(str, Enum):

    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        return name

    def __repr__(self):
        print('repr')
        print(self.name)
        return self.name

    def __str__(self):
        print('str')
        print(self.name)
        return self.name


class Programming(StrEnum):
    PYTHON = auto()
    JAVA = auto()
    JAVA_SCRIPT = auto()


print(list(Programming))
# [PYTHON, JAVA, JAVA_SCRIPT]
print(Programming.PYTHON == 'PYTHON') # True


class Programming2(IntEnum):
    PYTHON = 1
    JAVA = 2
    JAVA_SCRIPT = 3

print()
print(Programming2.PYTHON) # Programming2.PYTHON
print(Programming2.PYTHON == 1) # True

















