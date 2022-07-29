"""
Generator(제너레이터)

Generator 는 반복자(iterator) 와 같은 루프의 작용을 제어하기 위해 사용되는 특별한 함수 또는 루틴이다.
모든 Generator 는 반복자(iterator) 이다.
Generator 는 배열이나 리스트를 리턴하는 함수와 유사하며, 호출 할 수 있는 파라미터를 가지고 있으며,
연속적인 값을 만들어낸다.
그러나 한 번에 모든 값을 포함한 배열을 리턴하는 것이 아니다.
대신에 yield 구문을 사용하여 한 번 호출될 때마나 하나의 값만을 리턴하고, 이런 이유로 반복자(iterator) 에 비하여
아주 작은 메모리를 필요로 한다.
"""
import random
from typing import Type, List, Dict


class GeneratorEx01:

    def __init__(self):
        print(id(self))

    def general_func(self, x:int, y:int) -> int:
        """
        일반 함수가 호출되면 코드의 첫 번째 행 부터 시작하여 return, exception, 또는 리턴하지 않는 함수이면
        마지막 구문을 만날 때 까지 실행된 후 호출자(caller) 에게 모든 컨트롤를 리턴한다.
        그리고 함수가 가지고 있는 모든 내부 함수나 모든 로컬 변수는 메모리 상에서 사라진다.
        그러나, 호출되면 맡긴 일을 전부 다 끝내고 사라지는 함수가 아니라,
        자기가 했던 일을 기억하고 대기하고 있다가 다시 호출되면 전의 일을 이어서 하는 똑똑한 함수를 필요로 하게 되었다.
        그래서 나타난 것이 제너레이터이다.
        일반 함수보다 훨씬 더 좋은 퍼포먼스, 메모리 리소스도 절약할 수 있다.
        """
        print(self.__class__.__name__)
        return x + y

    @staticmethod
    def generator_ex_01(nums: List[int]):
        """
        이 함수는 제너레이터 오브젝트를 리턴한다.
        자신이 리턴할 모든 값을 메모리에 저장하지 않기 때문에, 일반 함수의 결과와 같이 한 번에 값으로 보이지 않는다.
        제너레이터는 한 번 호출될 때마다 하나의 값만을 전달(yield) 한다.
        즉, 위의 1 까지는 아무런 계산을 하지 않고, 다음 값에 대해서 물어보기를 기다리고 있는 상황이 된다.
        추출된 제너레이트 타입의 변수를
        next() 함수로 호출하게 되면, 그제서야 하나씩 값을 반환한다.
        이 때 next() 함수로 반복자의 인덱스를 넘어가면 StopIteration 에러를 반환한다.
        제너레이터는 일반적으로 for loop 를 통해서 호출한다.
        for loop 는 자신이 어디서 멈춰야 하는지 알고 있기 때문에, StopIteration 에러가 발생하지 않는다.
        """
        for n in nums:
            yield n * n

    @staticmethod
    def generator_ex2():
        """
        list comprehension 을 사용하여 제너레이터 만들기
        [] 를 () 로 변경
        generator 를 list 로 변경하면, generator 의 이점을 잃는다.
        """
        my_nums = [x * x for x in [1, 2, 3, 4, 5]]
        print(my_nums) # [1, 4, 9, 16, 25]
        print(type(my_nums)) # <class 'list'>

        my_nums = (n * n for n in [1, 2, 3, 4, 5])
        print(my_nums) # <generator object <genexpr> at 0x7fb8d74e1cb0>
        print(type(my_nums)) # <class 'generator'>

        for n in my_nums:
            yield n

    @staticmethod
    def generator_ex3(name: list[str], departments: list[str]):
        """
        제너레이터 예제 1
        """
        for idx, name in enumerate(names, start=1):
            employee = {
                "id": idx,
                "name": name,
                "department": random.choice(departments)
            }
            yield employee

    @staticmethod
    def generator_ex3_test(name: list[str], departments: list[str]) -> list:
        employees = []
        for idx, name in enumerate(names, start=1):
            employee = {
                "id": idx,
                "name": name,
                "department": random.choice(departments)
            }
            employees.append(employee)

        return employees



if __name__ == "__main__":
    generator_ex_01 = GeneratorEx01()

    # ret = generator_ex_01.general_func(1, 2)
    # print(ret)

    #############################################################################
    #### generator_ex_01
    # number_list = [i for i in range(10)]
    # ret = GeneratorEx01.generator_ex_01(number_list)
    # print(ret) # <generator object GeneratorEx01.generate_ex_01 at 0x1049d9c40>
    # print(type(ret)) # <class 'generator'>
    #
    # for _ in range(len(number_list)):
    #     print(next(ret))


    #############################################################################
    #### generator_ex_02
    # generator_ex_01.generator_ex2()


    #############################################################################
    #### generator_ex_03
    names: list[str] = [f"test_user_{i}" for i in range(1, 101)]
    departments: list[str] = [
        "영업1팀",
        "영업2팀",
        "개발1팀",
        "개발2팀",
        "인사팀",
    ]

    def execute_generator():
        ret = GeneratorEx01.generator_ex3(names, departments)
        print(ret)  # <generator object GeneratorEx01.generator_ex3 at 0x103322ea0>
        for _ in names:
            print(next(ret))

    execute_generator()

    def execute_general_func():
        ret = GeneratorEx01.generator_ex3_test(names, departments)
        print(ret)



# from __future__ import division
# import os
# import psutil
# import random
# import time


# # if __name__ == '__main__':
# #     process = psutil.Process(os.getpid())
# #     mem_before = process.memory_info().rss / 1024 / 1024
# #     t1 = time.time()
# #     people = people_list(1000000)
# #     t2 = time.time()
# #     mem_after = process.memory_info().rss / 1024 / 1024
# #     total_time = t2 - t1
# #
# #     print('*' * 50)
# #     print('시작 전 메모리 사용량: {} MB'.format(mem_before))
# #     print('종료 후 메모리 사용량: {} MB'.format(mem_after))
# #     print('총 소요된 시간: {:.6f} 초'.format(total_time))
#
#     # **************************************************
#     # 시작 전 메모리 사용량: 9.671875 MB
#     # 종료 후 메모리 사용량: 284.0546875 MB
#     # 총 소요된 시간: 1.192423 초
#
#
# # if __name__ == '__main__':
# #     process = psutil.Process(os.getpid())
# #     mem_before = process.memory_info().rss / 1024 / 1024
# #
# #     t1 = time.time()
# #     people_ge = people_generator(1000000)
# #     t2 = time.time()
# #     mem_after = process.memory_info().rss / 1024 / 1024
# #     total_time = t2 - t1
# #
# #     print('*' * 50)
# #     print('시작 전 메모리 사용량: {} MB'.format(mem_before))
# #     print('종료 후 메모리 사용량: {} MB'.format(mem_after))
# #     print('총 소요된 시간: {:.6f} 초'.format(total_time))
#
#     # **************************************************
#     # 시작 전 메모리 사용량: 9.69921875 MB
#     # 종료 후 메모리 사용량: 9.703125 MB
#     # 총 소요된 시간: 0.000002 초
#
# # 생성된 제너레이터 오브젝트를 사용해서 데이터를 처리하는 방법
# if __name__ == '__main__':
#     process = psutil.Process(os.getpid())
#     mem_before = process.memory_info().rss / 1024 / 1024
#     t1 = time.time()
#
#     loop_count = 1000000
#     # people_list = people_list(loop_count)
#     # for p in people_list:
#     #     print(p)
#
#     people_ge = people_generator(loop_count)
#     for p in people_ge:
#         print(p)
#
#     t2 = time.time()
#     mem_after = process.memory_info().rss / 1024 / 1024
#     total_time = t2 - t1
#
#     print('*' * 50)
#     print('시작 전 메모리 사용량: {} MB'.format(mem_before))
#     print('종료 후 메모리 사용량: {} MB'.format(mem_after))
#     print('총 소요된 시간: {:.6f} 초'.format(total_time))
#
#     # ************************************************** list
#     # 시작 전 메모리 사용량: 9.74609375 MB
#     # 종료 후 메모리 사용량: 287.3203125 MB
#     # 총 소요된 시간: 4.810807 초
#
#     # ************************************************** generator
#     # 시작 전 메모리 사용량: 9.6953125 MB
#     # 종료 후 메모리 사용량: 9.7109375 MB
#     # 총 소요된 시간: 4.898111 초
#
#     # 결론은
#     # 메모리의 소비를 줄여야 하는 경우, 제너레이터
#     # 실행 시간을 줄여야 하는 경우, 리스트
#     # 하지만 위의 테스트 데이터 보다 훨씬 더 많은 양의 데이터를 병행으로 동시에 처리해야 한다고 했을 때는,
#     # 약간의 시간을 줄이기 보다는 한정적인 리소스를 효율적으로 사용하는 경우가 대부분이다.
