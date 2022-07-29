import random

from typing import Optional, Generic
from pydantic import BaseModel, ValidationError, validator, PydanticValueError
from pydantic.generics import GenericModel

from typing import Generic, TypeVar

# Please refer to https://pydantic-docs.helpmanual.io/usage/models/#generic-models
ResultDataType = TypeVar("ResultDataType")


# class Success(BaseModel):
#     ok: bool
#     result: ResultDataType
#
#
# class Error(BaseModel):
#     ok: bool
#     err_msg: str

class InconsitentError(PydanticValueError):
    msg_template = 'inconsistent ok was given'

class Result(GenericModel, Generic[ResultDataType]):
    ok: bool
    result: Optional[ResultDataType]
    err_msg: Optional[str]

    @validator('result', always=True)
    def is_okay_consistant(cls, v, values):

        ok = values.get('ok')
        status = v.status

        if status == 'finish' and ok is False:
            raise InconsitentError
        return v



def validate_ret_val(wrapped):
    def wrapper(*args, **kwargs):
        ret = wrapped(*args, **kwargs)
        ret_model = wrapped.__annotations__['return']
        ret_model.validate(ret)
        return ret

    return wrapper


class OrderType1(BaseModel):
    status: str


class OrderType2(BaseModel):
    status: str


@validate_ret_val
def process_order1(order: OrderType1) -> Result[OrderType1]:
    """Assume orders are processed with a probability of 50 %"""
    if random.random() < 0.5:
        return {"ok": False, "err_msg": "failed to process order"}
    else:
        order.status = 'finish'
        return {"ok": True, "result": order}


@validate_ret_val
def process_order2(order: OrderType1) -> Result[OrderType1]:
    """Assume orders are processed with a probability of 50 %"""
    if random.random() < 0.5:
        return {"ok": False, "err_msg": "failed to process order"}
    else:
        order.status = 'finish'
        return {"ok": True, "result": order}


@validate_ret_val
def process_order1_wrong(order: OrderType1) -> Result[OrderType1]:
    """Assume orders are processed with a probability of 50 %"""

    # if random.random() < 0.5:
    #     print("required fields are missing")
    #     return {}
    # else:
    order.status = 'finish'
    # print("inconsistent ok value")
    return {"ok": False, "result": order}


if __name__ == '__main__':
    # for i in range(10):
    #     order = OrderType1(status='ready')
    #     print(f'process order {i}')
    #     print(process_order1(order))
    # print()
    #
    # for i in range(10):
    #     order = OrderType2(status='ready')
    #     print(f'process order {i}')
    #     print(process_order2(order))
    # print()

    for i in range(1):
        order = OrderType1(status='ready')
        print(f'process order {i}')
        try:
            print(process_order1_wrong(order))
        except Exception as e:
            print(e)
            print()
    print()

