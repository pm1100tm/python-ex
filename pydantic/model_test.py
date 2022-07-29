import random
import typing

from typing import Optional, Generic, TypeVar, List, Dict, Union
from pydantic import BaseModel, ValidationError, validator
from pydantic.generics import GenericModel


ResultDataType = TypeVar('ResultDataType')


class Error(BaseModel):
    ok: bool
    err_msg: str


class Result(GenericModel, Generic[ResultDataType]):
    data: Optional[ResultDataType]
    err_msg: Optional[Error]

    @validator('error', always=True, check_fields=False)
    def validate(cls, v):
        ret_ok      = v['ok']
        ret_result  = v.get('result')
        ret_err_msg = v.get('err_msg')

        if ret_result and not ret_ok:
            raise ValueError('inconsistent ok value was given')
        if ret_err_msg and ret_ok is False:
            raise ValueError('inconsistent ok value was given')
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
    # return Result[ResultDataType](data={'ok': False, 'err_msg': 'failed to process order'})
    # return Result[ResultDataType](error={'ok': True, 'result': order})
    # return None
    # return {'ok': False, 'err_msg': 'failed to process order'}
    # return {'ok': True, 'result': order}

    if random.random() < 0.5:
        return {'ok': False, 'err_msg': 'failed to process order'}
    else:
        order.status = 'finish'
        return {'ok': True, 'result': order}

@validate_ret_val
def process_order2(order: OrderType2) -> Result[OrderType1]:
    """Assume orders are processed with a probability of 50 %"""
    if random.random() < 0.5:
        return {"ok": False, "err_msg": "failed to process order"}
    else:
        order.status = 'finish'
        return {"ok": True, "result": order}

@validate_ret_val
def process_order1_wrong(order: OrderType1) -> Result[OrderType1]:
    """Assume orders are processed with a probability of 50 %"""
    # required fields are missing
    return {}

    # order.status = 'finish'
    # return {"ok": False, "result": order}

    # return {}
    # if random.random() < 0.5:
    #     # required fields are missing
    #     return {}
    # else:
    #     order.status = 'finish'
    #     # inconsistent ok value
    #     return {"ok": False, "result": order}


if __name__ == '__main__':
    for i in range(10):
        u_order = OrderType1(status='ready')
        print(f'process order {i}')
        print(process_order1(u_order))
    print()

    for i in range(10):
        order = OrderType2(status='ready')
        print(f'process order {i}')
        print(process_order2(order))
    print()

    for i in range(1):
        order = OrderType1(status='ready')
        print(f'process order {i}')
        try:
            print(process_order1_wrong(order))
        except Exception as e:
            print(e)
            print()
        print()
