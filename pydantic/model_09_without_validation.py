"""
============usage model 09 create models without validation
pydantic은 또한 검증 없이 모델을 만들 수 있는 construct(구성) 방법을 제공합니다.
이것은 데이터가 이미 검증되었거나 신뢰할 수 있는 소스에서 나왔고,
가능한 한 효율적으로 모델을 만들고 싶을 때 유용할 수 있습니다
(전체 검증이 있는 모델을 만드는 것보다 일반적으로 약 30배 빠릅니다).

construct()는 유효성 검사를 수행하지 않으므로 유효하지 않은 모델을 만들 수 있습니다.
construct() 메서드는 이미 검증된 데이터 또는 신뢰할 수 있는 데이터만 사용해야 합니다.
"""
from pydantic import BaseModel


class User(BaseModel):
    id: int
    age: int
    name: str = 'swd'


if __name__ == '__main__':
    user = User(id=1, age=20)
    user_data = user.dict()
    print(user_data)

    field_set = user.__fields_set__
    print(field_set)
    # user_data 및 field_set을 RPC에 전달하거나 데이터베이스 등에 저장

    # 그런 다음 다시 유효성 검증 없이 사용자의 새 인스턴스를 생성할 수 있습니다.
    # 이 시점에서 다시 유효성 검증을 하는 것은 불필요합니다.

    # construct can be dangerous, only use it with validated data!:
    bad_user = User.construct(id='asf')
    print(repr(bad_user))

    # construct()에 _fields_set 키워드 인수는 선택 사항이지만,
    # 원래 설정된 필드와 그렇지 않은 필드를 보다 정확하게 지정할 수 있습니다.
    # 생략된 경우 __fields_set_는 제공된 데이터의 키일 뿐입니다.




















