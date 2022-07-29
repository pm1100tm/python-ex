"""
============usage model 07 error handling

pydantic은 유효성 검사 중인 데이터에서 오류가 발견될 때마다 유효성 검사 오류를 발생시킵니다.
Validation 코드는 ValidationError 자체를 올리지 않고 ValueError, TypeError
또는 AssertionError(또는 ValueError 또는 TypeError의 하위 클래스)를 올리면
ValidationError 를 채우는 데 사용됩니다.

발견된 오류 수와 관계없이 ValidationError에는 모든 오류와 오류 발생 방법에 대한 정보가 포함되어 있습니다.

You can access these errors in a several ways:

e.errors()
- 메서드는 입력 데이터에서 발견된 오류 목록을 반환합니다.

e.json()
- 에러의 json 표현식을 반환한다.

str(e)
- method will return a human readable representation of the errors.


각 오류 개체에는 다음의 속성을 가지고 있습니다.
loc
오류의 위치를 목록으로 표시합니다.
목록의 첫 번째 항목은 오류가 발생한 필드이며,
필드가 하위 모델인 경우 오류의 중첩된 위치를 나타내는 후속 항목이 표시됩니다.

type
a computer-readable identifier of the error type.

msg
a human readable explanation of the error.

ctx
an optional object which contains values required to render the error message.


============usage model 08 custom errors
사용자 지정 데이터 유형 또는 검증자에서 ValueError, TypeError 또는 AssertionError를
사용하여 오류를 발생시켜야 합니다.

@validator 데코레이터 사용에 대한 자세한 내용은 검증자를 참조하십시오.


You can also define your own error classes,
which can specify a custom error code, message template, and context:
>> 사용자 정의 오류 코드, 메시지 템플릿 및 컨텍스트를 지정할 수 있는 고유한 오류 클래스를 정의할 수도 있습니다.
"""
from pydantic import BaseModel, ValidationError, validator, PydanticValueError


class Model(BaseModel):
    foo: str

    @validator('foo')
    def value_must_equal_bar(cls, v):
        if v != 'bar':
            raise ValueError('value must be a "bar"')
        return v


if __name__ == '__main__':
    try:
        model = Model(foo='bal')
    except ValidationError as e:
        print(e[0]['msg'])
        # print(e.errors())
        """
        [
            {
                'loc': ('foo',),
                'msg': 'value must be a "bar"',
                'type': 'value_error'
            }
        ]
        """

        # print(str(e))
        """
        1 validation error for Model
        foo
        """

        # print(e.json())
        """
        [
          {
            "loc": [
              "foo"
            ],
            "msg": "value must be a \"bar\"",
            "type": "value_error"
          }
        ]
        """


# class NotBarError(PydanticValueError):
#     code = 'not_a_bar'
#     msg_template = 'value is not "bar", got "{wrong_value}"'


# class Model(BaseModel):
#     foo: str
#
#     @validator('foo')
#     def value_must_be_equal_bar(cls, v):
#         if v != 'bar':
#             raise NotBarError(wrong_value=v)
#         return v
#
#
# if __name__ == '__main__':
#     try:
#         Model(foo='ber')
#     except ValidationError as e:
#         print(e.json())
#         """
#         [
#           {
#             "loc": [
#               "foo"
#             ],
#             "msg": "value is not \"bar\", got \"ber\"",
#             "type": "value_error.not_a_bar",
#             "ctx": {
#               "wrong_value": "ber"
#             }
#           }
#         ]
#         """
