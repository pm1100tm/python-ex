"""
============usage model 10 generic models
Pydantic은 공통 모델 구조를 더 쉽게 재사용할 수 있도록 제네릭 모델 생성을 지원합니다.

제네릭 모델은 python >= 3.7에서만 지원되며,
이는 python 3.6과 python 3.7 사이에서 제네릭이 구현되는 방법에 대한 수많은 미묘한 변화 때문이다.

제네릭 모델을 선언하려면 다음 단계를 수행합니다.
1. 하나 이상의 typing.TypeVar 인스턴스를 선언한다. 이것은 모델에 대한 파라미터로 표시한다.
2. pydantic.generics 에서 상속된 pydantic 모델을 선언한다.
   일반 모델 및 입력 제네릭 - TypeVar 인스턴스 입력 매개 변수로 전달합니다.
3. TypeVar 인스턴스를 어노테이션으로 사용한다.

다음은 GenericModel을 사용하여 쉽게 재사용되는 HTTP 응답 페이로드 래퍼를 만드는 예입니다.
"""
# from typing import Generic, TypeVar, Optional, List, Type, Any, Tuple
#
# from pydantic          import BaseModel, validator, ValidationError
# from pydantic.generics import GenericModel
#
#
# DataT = TypeVar('DataT')
#
#
# class Error(BaseModel):
#     code: int
#     message: str
#
#
# class DataModel(BaseModel):
#     numbers: List[int]
#     people: List[str]
#
#
# class Response(GenericModel, Generic[DataT]):
#     data: Optional[DataT]
#     error: Optional[Error]
#
#     @classmethod
#     @validator('error', always=True)
#     def check_consistency(cls, v, values):
#         print('*' * 50)
#         print(v)
#         print('*' * 50)
#         print(values)
#
#         if v is not None and values['data'] is not None:
#             raise ValueError('must not provide both data and error')
#         if v is None and values.get('data') is None:
#             raise ValueError('must provide data or error')
#         return v
#
#
# TypeX = TypeVar('TypeX')
#
#
# class BaseClass(GenericModel, Generic[TypeX]):
#     X: TypeX
#
#
# class ChildClass(BaseClass[TypeX], Generic[TypeX]):
#     # inherit from Generic[TypeX]
#     pass
#
#
# DataTT = TypeVar('DataTT')
#
# class ResponseTwo(GenericModel, Generic[DataTT]):
#     data: DataTT
#
#     @classmethod
#     def __concrete_name__(cls: Type[Any], params: Tuple[Type[Any], ...]) -> str:
#         return f"{params[0].__name__.title()}Response"
#
#
# T = TypeVar('T')
#
# class InnerT(GenericModel, Generic[T]):
#     inner: T
#
#
# class OuterT(GenericModel, Generic[T]):
#     outer: T
#     nested: InnerT[T]
#
#
# AT = TypeVar('AT')
# BT = TypeVar('BT')
#
# class Model(GenericModel, Generic[AT, BT]):
#     a: AT
#     b: BT


# if __name__ == '__main__':
    # data = DataModel(numbers=[1,2,3], people=[])
    # error = Error(code=404, message='Not Found')
    # print(Response[int](data=1))
    #> data=1 error=None

    # print(Response[str](data='value'))
    #> data='value' error=None

    # print(Response[str](data='value').dict())
    #> {'data': 'value', 'error': None}

    # print(Response[DataModel](data=data).dict())
    # {
    #   'data': {
    #       'numbers': [1, 2, 3],
    #       'people': []
    #   },
    #   'error': None
    # }

    # print(Response[DataModel](error=error).dict())
    # {
    #     'data': None,
    #     'error': {
    #         'code': 404,
    #         'message': 'Not Found'
    #     }
    # }

    # print(Response[DataModel](data=data, error=error).dict())
    # {
    #     'data': {
    #         'numbers': [1, 2, 3],
    #         'people': []
    #     },
    #     'error': {
    #         'code': 404,
    #         'message': 'Not Found'
    #     }
    # }

    # try:
    #     Response[int](data='value')
    # except ValidationError as e:
    #     print(e.errors())
        # 1 validation error for Response[int]
        # data
        # value is not a valid integer (type=type_error.integer)

    # try:
    #     Response[int](data=data, error=error)
    # except ValidationError as e:
    #     print(e.errors())

    # Replace TypeX by int
    # cc = ChildClass[int](X=1)
    # print(cc)  # X = 1
    #
    # print('=' * 50)
    # DataTT = TypeVar('DataTT')
    # a: DataTT = 1
    # print(a)
    # a: DataTT = 'asf'
    # print(a)

    # print(repr(ResponseTwo[int](data=1)))
    # > IntResponse(data=1)

    # print(repr(ResponseTwo[str](data='a')))
    # > StrResponse(data='a')

    # nested = InnerT[int](inner=1)
    # outer = OuterT[int](outer=1, nested=nested)
    # print(outer)
    # print(outer.dict())
    # print(outer.nested.inner)
    # # outer=1 nested=InnerT[int](inner=1)
    #
    # print('*' * 50)
    # nested = InnerT[str](inner='a')
    # print(nested)
    # print(OuterT[int](outer='a', nested=nested))

    # print(Model(a='a', b='b'))
    #
    # IntT = TypeVar('IntT', bound=int)
    # typevar_model = Model[int, IntT]
    # print(typevar_model(a=1, b=1))
    #
    # try:
    #     typevar_model(a='a', b='a')
    # except ValidationError as exc:
    #     print(exc)

    # concrete_model = typevar_model[int]
    # print(concrete_model(a=1, b=1))


from typing import Generic, TypeVar, Optional, List

from pydantic import BaseModel, validator, ValidationError
from pydantic.generics import GenericModel


DataT = TypeVar('DataT')


class Error(BaseModel):
    code: int
    message: str


class DataModel(BaseModel):
    numbers: List[int]
    people: List[str]


class Response(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    error: Optional[Error]

    @classmethod
    @validator('error', always=True)
    def check_consistency(cls, v, values):
        print(f"check_consistency:: {v}, {values}")
        if v is not None and values['data'] is not None:
            raise ValueError('must not provide both data and error')

        if v is None and values.get('data') is None:
            raise ValueError('must provide data or error')

        return v


if __name__ == '__main__':
    data = DataModel(numbers=[1, 2, 3], people=[])
    error = Error(code=404, message='Not found')
    print(Response[int](data=1))
    #> data=1 error=None

    print(Response[str](data='value'))
    #> data='value' error=None

    print(Response[str](data='value').dict())
    #> {'data': 'value', 'error': None}

    print(Response[DataModel](data=data).dict())
    """
    {
        'data': {'numbers': [1, 2, 3], 'people': []},
        'error': None,
    }
    """

    print(Response[DataModel](error=error).dict())
    """
    {
        'data': None,
        'error': {'code': 404, 'message': 'Not found'},
    }
    """

    try:
        Response[int](data='value')
    except ValidationError as e:
        print(e)
        """
        2 validation errors for Response[int]
        data
          value is not a valid integer (type=type_error.integer)
        error
          must provide data or error (type=value_error)
        """









































