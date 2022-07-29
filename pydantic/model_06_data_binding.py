""" usage model 06 data binding
임의의 클래스는 모든 클래스에 사전과 같은 인터페이스를 제공하는 GetterDict 클래스를 사용하여 pydantic 에 의해 처리된다.
GetterDict 의 하위 클래스를 Config.getter_dict 값으로 설정하여 이 동작 방식을 사용자 정의할 수 있다.

per=True 를 사용하여 root_validator 를 사용하여 클래스 검증을 사용자 지정할 수도 있다.
이 경우 검증자 함수는 복사 및 수정할 수 있는 GetterDict 인스턴스를 전달한다.

GetterDict 인스턴스는 보초를 풀백으로 사용하여 각 필드에 의해 호출된다.
(다른 기본 값이 설정되지 않은 경우).
이 보초병을 돌려보낸다는 것은 들판이 없어졌다는 것을 의미한다. 다른 값은 필드 값으로 해석됩니다.
"""
from pydantic import BaseModel
from typing import Any, Optional
from pydantic.utils import GetterDict
from xml.etree.ElementTree import fromstring


xmlstring = """
<User Id="2138">
    <FirstName />
    <LoggedIn Value="true" />
</User>
"""


class UserGetter(GetterDict):

    def get(self, key: str, default: Any) -> Any:

        # element attributes
        if key in {'Id', 'Status'}:
            print('1')
            return self._obj.attrib.get(key, default)

        # element children
        else:
            try:
                print('2')
                return self._obj.find(key).attrib['Value']
            except (AttributeError, KeyError):
                print('3')
                return default


class User(BaseModel):
    Id: int
    Status: Optional[str]
    FirstName: Optional[str]
    LastName: Optional[str]
    LoggedIn: bool

    class Config:
        orm_mode = True
        getter_dict = UserGetter


if __name__ == '__main__':
    # r = fromstring(xmlstring)
    user = User.from_orm(fromstring(xmlstring))
    print(user)