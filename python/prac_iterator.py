""" 이터레이터 (iterator)
iterable 객체 - 반복 가능한 객체
대표적으로 iterable 한 타입 - list, dict, set, str, bytes, tuple, range

Iterator 란?
값을 차례대로 꺼낼 수 있는 객체
iterator 는 iterable 한 객체를 내장함수 또는 iterable 객체의 메소드로 객체를 생성할 수 있다.

iterable 객체는 매직 메소드 __iter__ 메소드를 가지고 있다. 이것으로 iterator 를 만들 수 있다.

"""
# 1. 파이썬 내장함수 iter()를 사용해 iterator 객체를 만들기
a = [1,2,3]
a_iter = iter(a)
print(a_iter) # <list_iterator object at 0x7f8f431a98d0>
print(type(a_iter)) # <class 'list_iterator'>
print(dir(a)) # ... __iter__

b = {1,2,3}
b_iter = b.__iter__()
print(type(b_iter)) # <class 'set_iterator'>

# iterator 가 값을 차례대로 꺼낼 수 있는 객체라는 것의 의미를 코드로 보면
# next 내장 함수를 사용 할 때 마다 첫번째, 두번째, 세번째 값이 출력된다.
# 네번째 실행에서는 StopIteration 이라는 예외가 발생한다.

next(a_iter) # 1
next(a_iter) # 2
next(a_iter) # 3
next(a_iter) # StopIteration
