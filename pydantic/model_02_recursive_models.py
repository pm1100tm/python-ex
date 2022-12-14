""" usage model 02 recursive models
Recursive Models๐
๊ณ์ธต์  ๋ฐ์ดํฐ ๊ตฌ์กฐ๋ ๋ชจ๋ธ ์์ฒด๋ฅผ ์ด๋ธํ์ด์์ ์ ํ์ผ๋ก ์ฌ์ฉํ์ฌ ์ ์ํ  ์ ์๋ค.
์ฐ์ตํด๋ณด์.
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
