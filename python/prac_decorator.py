"""
데코레이터란?
기존의 코드에 여러가지 기능을 추가하는 파이썬 구문
만들어져 있는 기존의 코드를 수정하지 않고도, 래퍼(wrapper) 함수를 이용하여,
여러가지 기능을 추가할 수 있다.
"""
# 1 단계
# def deco_func(origin_func):
#     def wrapper_func():
#         return origin_func()
#
#     return wrapper_func
#
# def display():
#     print('exec display func')
#
# decorated_display_func = deco_func(display)
# decorated_display_func()

# 2 단계
# def deco_func(origin_func):
#     def wrapper_func():
#         print('{0} 함수 실행전'.format(origin_func.__name__))
#         return origin_func()
#
#     return wrapper_func
#
# def display1_func():
#     print('함수 실행 전')
#
# def display2_func():
#     print('함수 실행 전')
#
# decorated_display1_func = deco_func(display1_func)
# decorated_display2_func = deco_func(display2_func)
#
# decorated_display1_func()
# decorated_display2_func()


# 3단계
# def deco_func(origin_func):
#     def wrapper_func():
#         print('{0} 함수 실행전'.format(origin_func.__name__))
#         return origin_func()
#
#     return wrapper_func
#
# @deco_func
# def display1_func():
#     print('함수 실행 전')
#
# @deco_func
# def display2_func():
#     print('함수 실행 전')
#
# display1_func()
# display1_func()


# 4단계
# def deco_func(origin_func):
#     def wrapper_func(*args, **kwargs):
#         print('{0} 함수 실행전:: args:{1}, kwargs:{2}'.format(origin_func.__name__, args, kwargs))
#         return origin_func(*args, **kwargs)
#
#     return wrapper_func
#
# @deco_func
# def display_func(name: str, x:int):
#     print('함수 실행 전')
#
# display_func('swd', 20)


# 5 단계 : 클래스 형식 (주로 사용되는 것은 함수형 데코레이터. 이렇게 할 수 있다는 것만 알아두기!)
# class DecoClass:
#
#     def __init__(self, origin_func):
#         self.origin_func = origin_func
#
#     def __call__(self, *args, **kwargs):
#         print(f'함수 호출 전 {self.origin_func.__name__}')
#         return self.origin_func(*args, **kwargs)
#
# @DecoClass
# def display():
#     print('display func 호출함')
#
# display()
#
# @DecoClass
# def display_param(name: str, age:int):
#     print(f'display func 호출함:: name-{name}, age-{age}')
#
# display_param('swd', 20)
# display_param(name='swd', age=20)


# ==================================================================================================
# 실사용의 예 1)
# logging 데코레이터 1
# import datetime
# import time

# def logging(origin_func):
#     import logging
#     filename = f'{origin_func.__name__}.log'
#     logging.basicConfig(handlers=[logging.FileHandler(filename, 'a', 'utf-8')], level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         logging.info(msg=f'[{timestamp}] 실행 결과 args-{args}, kwargs-{kwargs}')
#         return origin_func(*args, **kwargs)
#
#     return wrapper

# @logging
# def display(name: str, age: int):
#     # time.sleep(1)
#     print('display_info({}, {}) 함수가 실행 됐습니다.'.format(name, age))

# display(name='swd', age=20)
# display.log 파일 확인

# def logging(func):
#     import logging
#     filename = f'{func.__name__}.log'
#     logging.basicConfig(handlers=[logging.FileHandler(filename=filename, mode='a', encoding='utf-8')],
#                         level=logging.INFO)
#
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         log_msg = f'[{timestamp}] args:{args}, kwargs-{kwargs}'
#         print(log_msg)
#         logging.info(msg=log_msg)
#         return func(*args, **kwargs)
#
#     return wrapper
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time() - t1
#         print(f'{func.__name__} 함수 실행 시간: {t2}초')
#         return result
#
#     return wrapper
#
# @logging
# @timer
# def display(name:str, age:int) -> None:
#     time.sleep(1)
#     print(f'display:: {name} / {age}')
#
# display(name='swd', age=1)

# [2022-06-06 14:57:47] args:(), kwargs-{'name': 'swd', 'age': 1}
# display:: swd / 1
# wrapper 함수 실행 시간: 1.0045058727264404초

# wrapper.log 란 파일이 생성되고 로그가 남는다. display.log 에는 기록되지 않았다.
# 복수의 데코레이터를 사용하면, 아래쪽 데코레이터부터 실행되는데,
# logging 이 실행되고, 그 후 timeer 에게 wrapper 함수를 인자로 전달하기 때문에 생기는 현상이다.
# 이 현상을 막기 위해서 functools 의 wraps() 데코레이터를 사용한다.
# from functools import wraps
# from datetime import datetime
# import time
#
#
# def my_logger(func):
#     import logging
#     filename = f'{func.__name__}.log'
#     logging.basicConfig(handlers=[logging.FileHandler(filename=filename, mode='a', encoding='utf-8')],
#                         level=logging.INFO)
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         log_msg = f'[{log_time}] 실행결과 args-{args}, kwargs-{kwargs}'
#         logging.info(msg=log_msg)
#         return func(*args, **kwargs)
#
#     return wrapper
#
# def my_timer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'{func.__name__} func start!')
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time() - t1
#         print(f'{func.__name__} func end!')
#         print(f'{"*" * 10}{func.__name__} exec time - {t2}')
#         return result
#     return wrapper
#
# @my_timer
# @my_logger
# def display(name:str, age:int):
#     time.sleep(1)
#     print(f'display:: {name} / {age}')
#
# display('swd', 20)


# 실사용의 예 2)
# 로그인 데코레이터
# def login_decorator(login_required=False):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f'login_required::{login_required}')
#             data = kwargs.get('request_data')
#             if login_required:
#                 if not data['auth'] or data['user_id'] == 0:
#                     raise Exception('Login Required!')
#                 data['user'] = 'user'
#                 kwargs['request_data'] = data
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @login_decorator(login_required=False)
# def get_product_data_1(user_id: int=None):
#     print(f'exec get_product_data:: {user_id}')
#     print()
#
# @login_decorator(login_required=True)
# def get_product_data_2(request_data: dict=None):
#     print(f'exec get_product_data:: {request_data}')
#     print()
#
#
# get_product_data_1()
#
# user_data = {
#     'auth' : True,
#     'user_id'  : 1,
#     'user_name': 'swd'
# }
#
# get_product_data_2(request_data=user_data)
#
# user_data = {
#     'auth' : True,
#     'user_id'  : 0,
#     'user_name': 'swd'
# }
# get_product_data_2(request_data=user_data)
