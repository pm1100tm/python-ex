""" usage model 01 method
pydantic 에서 객체를 정의하는 주요 수단은 모델을 통해서 정의된다.
모델은 단순히 BaseModel 로 부터 상속받은 클래스이다.
이 모델은 인풋 데이터와 유사하거나, API 의 end point 의 요구 사항으로 생각될 수 있다.

신뢰할 수 없는 데이터가 모델에 전달될 수 있다.
구분 문석 및 유효성 검사 후 pydantic 은 결과 모델 인스턴스의 필드가 모델에 정의된 필드 유형과 일치함을 보장한다.

*알아둬야 할 것
pydantic 은 주로 검증 라이브러리가 아닌 parsing 라이브러리이다.
검증은 목적을 위한 수단이다. 제공된 유형과 제약 조건을 준수하는 모델을 구축한다.
다시 말해서, pydantic 은 입력 데이터가 아니라, 출력 모델의 유형과 제약 조건을 보장한다는 것이다.
pydantic 의 주요 목적은 유효성 검사가 아니지만, 사용자 정의 유효성 검사에 이 라이브러리를 사용할 수 있다.

연습해보자.

BaseModel 을 상속받은 User 모델 클래스를 만들었다.
User 모델에는 id, name 이라는 클래스 변수를 만들었다.
id   - int 라는 타입 어노테이션을 주었고,
name - 기본 값으로 'Jane Doe' 를 주어, str 이라고 타입을 추론한다.

하지만 추론하게 만드는 방법은 명확하지도 않아, 권장하지 않는다.


BaseModel 을 상속받은 모델은 아래와 같은 메서드를 사용할 수 있다.
dict()
json()
copy()
parse_obj()
parse_raw()
parse_file()
from_orm()
schema()
schema_json()
construct()
__fields_set__
__config__

*dict()
모델의 키와 값을 딕셔너리로 리턴한다.
주로 모델을 딕셔너리로 컨버팅 하는 방법이다.
모델 안에 정의된 서브 모델의 타입은 재귀적으로 딕셔너리로 컨버팅된다.

*json()
모델 인스턴스를 JSON 형식으로 시리얼라이즈하여 리턴한다.
일반적으로 .json()은 차례로 .dict()를 호출하고 결과를 직렬화합니다.

*copy()
모델을 복사한다 (shallow copy)
이는 불변 모델에 특히 유용하다.


아래의 함수는 pydantic 이 데이터를 구문 분석하기 위한 3가지 헬퍼 메서드이다.
parse_obj(), parse_raw(), parse_file()

*parse_obj()
모델의 __init__ 메서드와 매우 유사하다.
전달된 개체가 딕트가 아닌 경우 ValidationError가 발생한다.

*parse_raw()
이것은 str 또는 바이트를 취하여 json으로 구문 분석한 다음 결과를 parse_obj로 전달합니다.
content_type 인자를 적절하게 설정하여 pickle 데이터를 파싱하는 것도 지원됩니다.

*parse_file()
파일 경로를 가져와 파일을 읽고 내용을 parse_raw 에 전달합니다.
content_type을 생략하면 파일의 확장자에서 추론됩니다.


*from_orm()
임의의 클래스에서 모델로 데이터를 로드한다.

*schema()
스키마의 JSON 문자열 표현을 반환한다.

*construct()
유효성 검사를 실행하지 않고 모델을 만드는 클래스 메서드이다.

*__fields__
모델 인스턴스가 초기화 될 때 설정된 필드 이름 조합이다.

*__config__
모델의 구성 클래스를 나타낸다.
"""
from typing   import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


if __name__ == '__main__':
    # =================================================================
    user_1 = User(id='123')
    print(user_1.id == 123)
    print(user_1.name == 'Jane Doe')
    print(user_1.__fields_set__ == {'id'})

    print(user_1.dict())
    print(dict(user_1))
    assert user_1.dict() == dict(user_1) == {'id': 123, 'name': 'Jane Doe'}

    user_2 = User(id=1, name=123) # name 은 '123' 으로 추론되고 에러를 발생시키지 않는다.
    user_3 = User(id='asdf', name=123) # id 로 설정한 값이 int 로 파싱되지 않기 때문에 에러를 발생시킨다.
