"""
프로그래밍 언어에서의 클로저란 퍼스트클래스 함수를 지원하는 언어의 네임 바인딩 기술이다.

클로저는 어떤 함수를 함수 자신이 가지고 있는 환경과 함께 저장한 레코드이다.
또한 함수가 가진 프리변수를 클로저가 만들어지는 당시의 값과 레퍼런스에 맵핑하여 주는 역할을 한다.

*프리변수(free variable)란?
파이썬에서 프리변수는 코드블럭안에서 사용은 되었지만, 그 코드블럭안에서 정의되지 않은 변수를 뜻합니다.

클로저는 일반 함수와는 다르게, 자신의 영역 밖에서 호출된 함수의 변수 값과 레퍼런스를 복사하고 저장한 뒤,
이 캡쳐한 값들에 엑세스할 수 있게 도와준다.
"""
# 1 단계
# def outer_func():
#     message = 'Hi'
#
#     def inner_func():
#         print(message)
#
#     return inner_func()
#
# outer_func() # Hi


# 2 단계
# def outer_func():
#     message = 'Hi'
#     ok = True
#
#     def inner_func():
#         print(message)
#         print(ok)
#
#     return inner_func
#
# my_func = outer_func()
# print(my_func)
#
# my_func() # Hi
#
# # my_func() == inner_func() 함수가 outer_func 함수의 로컬 변수인 message 를 참조
# # 그 해답은 클로저
#
# for var in dir(my_func):
#     print(var)
#
# # __annotations__
# # __builtins__
# # __call__
# # __class__
# # __closure__ ...
#
# print(type(my_func.__closure__)) # <class 'tuple'>
# print(my_func.__closure__) # (<cell at 0x7fdff21a4070: str object at 0x7fdff21864f0>,)
# print(my_func.__closure__[0]) # <cell at 0x7feb8f9a8070: str object at 0x7feb8f944670>
# print(dir(my_func.__closure__[0]))
# # [..., 'cell_contents']
# print(my_func.__closure__[0].cell_contents) # Hi
# print(my_func.__closure__[1].cell_contents) # True


# 3 단계
# def outer_func(tag: str):
#     text = 'Some text'
#     tag_set = tag
#
#     def inner_func():
#         print('<{0}>{1}</{0}>'.format(tag_set, text))
#
#     return inner_func
#
# h1_func = outer_func(tag='h1')
# p_func = outer_func(tag='p')
#
# h1_func() # <h1>Some text</h1>
# p_func() # <p>Some text</p>


# 4 단계
# def outer_func(tag: str):
#     tag_set = tag
#
#     def inner_func(text: str):
#         print('<{0}>{1}</{0}>'.format(tag, text))
#
#     return inner_func
#
# h1_tag = outer_func('h1')
# div_tag = outer_func('div')
#
# h1_tag('title')
# div_tag('nba live')

# 클로저는 이렇게 하나의 함수로 여러 가지의 함수를 간단히 만들어 낼 수 있게도 해주며,
# 기존에 만든 함수나 모듈 등을 수정하지 않고도 wrapper 함수를 이용해 커스터마이징 할 수 있게 해준다.

# 실사용 예
