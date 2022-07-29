""" usage model 02 recursive models
Recursive Models🔗
계층적 데이터 구조는 모델 자체를 어노테이션의 유형으로 사용하여 정의할 수 있다.
연습해보자.
"""
from typing   import List

from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float = None


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


if __name__ == '__main__':
    # Recursive Models
    m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    print(m)
    print(m.dict())
