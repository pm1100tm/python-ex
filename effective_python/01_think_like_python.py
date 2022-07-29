"""
제 1장. 퍄이썬 답게 생각하기
"""
import random
from typing import Type, List, Tuple, Dict, Any


class EffectivePythonChapter1:
    snack_calories = {
        '감자칩': 140,
        '팝콘': 80,
        '땅콩': 190
    }
    item = ("호박엿", 140)
    snack = [("베이켠", 10), ("소세지", 20), ("감자칩", 30)]

    def test1(self) -> tuple:
        items = self.snack_calories.items()
        print(items)
        print(items.mapping)
        return tuple()

    def test2(self):
        """
        튜플에 있는 값은 숫자 인덱스를 사용해 접근할 수 있다.
        인덱스를 통해 새 값을 대입할 수는 없다.
        """
        items = self.test1()
        print(items[0])
        print(items[1])
        print(items[0][0])

        try:
            items[0][0] = 'test'
        except TypeError as e:
            print(str(e)) # 'tuple' object does not support item assignment

    def test3(self):
        """
        파이썬에는 언패킹(unpacking) 구문이 있다. 언패킹 구문을 사용하면 한 문장 안에서
        여러 값을 대입할 수 있다.
        """
        name, calories = self.item # unpacking
        print(name, "&", calories) # 호박엿 & 140

    @staticmethod
    def get_number_list():
        number_list = []
        for i in range(10):
            number_list.append(random.randrange(10))
        return number_list

    @staticmethod
    def bubble_sort_1(nums: List[int]):
        for _ in range(len(nums)):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    temp = nums[i-1]
                    nums[i] = nums[i-1]
                    nums[i] = temp

        return nums

    @staticmethod
    def bubble_sort_2(nums: List[int]):
        for _ in range(len(nums)):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]

        return nums

    def test_bubble_sort(self):
        number_list = self.get_number_list()
        print(number_list)

        nums = self.bubble_sort_1(number_list)
        print(nums)

        nums = self.bubble_sort_2(number_list)
        print(nums)

    @staticmethod
    def betterway_05_use_helper_function(self) -> None:
        """
        Better way 05. 복잡한 식을 쓰는 대신 도우미 함수를 작성하라.
        """
        pass

    def betterway_06_use_unpacking_than_using_index(self) -> None:
        """
        Better way 06. 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라.
        """
        for idx, (name, calories) in enumerate(self.snack, start=1): # idx 를 강제로 1로 바꿔주는 역할
            print(f"{idx}. 이름: {name}, 칼로리: {calories}")

    @staticmethod
    def betterway_07_use_enumerate_than_range() -> None:
        """
        Better way 07. range 보다는 enumerate 를 사용하라.
        """
        # 리스트를 이터레이션하면서 리스트의 몇 번째 원소를 처리 중인지 알아야 할 때가 있다.
        # 리스트의 길이를 알아야 하고, 인덱스를 사용해 배열 원소에 접근해야 한다.
        # 단계가 여러 개이며 코드를 읽기 어렵다.
        flavor_list = ["바닐라", "딸기", "초코"]
        for i in range(len(flavor_list)):
            flavor = flavor_list[i]
            # print(f"{i + 1}: {flavor}")

        # enumerate 는 이터레이터를 지연 계산 제너레이터 (lazy generator) 로 감싼다.
        # enumerate 는 루프 인덱스와 이터레이터의 다음 값으로 이루어진 쌍을 넘겨준다. (yield)
        it = enumerate(flavor_list)
        print(next(it))
        print(next(it))
        print(next(it))

        for i, flavor in enumerate(flavor_list):
            print(f"{i + 1}: {flavor}")

        for i, flavor in enumerate(flavor_list, 1):
            print(f"{i}: {flavor}")

    @staticmethod
    def betterway_08_use_zip() -> None:
        """
        Better way 08. 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip 을 사용하라.
        """
        names = ["your_english_name", "나나나", "シムウォンドゥ"]
        count_list = [len(n) for n in names]

        longest_name = None
        max_count = 0

        for i in range(len(names)):
            count = count_list[i]
            if count >= max_count:
                longest_name = names[i]
                max_count = count

        # print(longest_name)
        # print(max_count)

        for idx, name in enumerate(names):
            count = count_list[idx]
            if count >= max_count:
                max_count, longest_name = count, name

        # print(longest_name)
        # print(max_count)

        for name, count in zip(names, count_list):
            if count >= max_count:
                longest_name, max_count = name, count

        # print(longest_name)
        # print(max_count)

        # 입력 데이터의 길이가 서로 다를 경우의 zip 이 어떻게 동작하는지 주의가 필요하다.
        # zip 은 자신이 감싼 이터레이터 중 어느 하나가 끝날 때 까지 튜플을 내놓는다.
        # 즉, 더 긴 이터레이터의 뒷부분을 버리는 식으로 zip 함수가 동작한다.
        names.append("test1------------------")
        for name, count in zip(names, count_list):
            if count >= max_count:
                longest_name, max_count = name, count

        # print(longest_name)
        # print(max_count)

        # 전달한 리스트의 길이가 같이 않을 것으로 예상한다면, itertools 내중 모듈에 들어있는
        # zip_longest 를 대신 사용하는 것을 고려하라.
        # zip_longest 는 존재하지 않는 값에 대해서 fillvalue 가 사용되며, 기본 값은 None 이다.
        import itertools
        for name, count in itertools.zip_longest(names, count_list):
            print(f"{name}: {count}")

        for name, count in itertools.zip_longest(names, count_list):
            print(f"{name}: {100 if not count else count}")

    @staticmethod
    def betterway_09_not_use_else_block_to_for_or_while() -> None:
        """
        Better way 09. for 나 while 루프 뒤에 else 블록을 사용하지 말아라.
        """
        for i in range(3):
            print(f"Loop: {i}")
        else:
            print("반드시 실행됨")

        for i in range(3):
            print(f"Loop: {i}")
            if i == 1:
                break
        else:
            print("실행되지 않음")

        for x in []:
            print("실행되지 않음")
        else:
            print("반드시 실행됨")

        while False:
            print("실행되지 않음")
        else:
            print("반드시 실행됨")

        # 서로소 계산 - 두 수의 공약수가 1만 존재함
        a = 4
        b = 9
        for i in range(2, min(a, b) + 1):
            print(f"서로소 검사 중: {i}")
            if a % i == 0 and b % i == 0:
                print("서로소")
                break
        else:
            print("서로소 아님")

        # 위의 식에서 더 좋은 코드는 도우미 함수를 사용하는 것
        def coprime(a: int, b: int) -> bool:
            for i in range(2, min(a, b) + 1):
                if a % i == 0 and b % i == 0:
                    return False
            return True

        assert coprime(a, b)
        assert not coprime(3, 6)

        # 두번째 방법은 루프 안에서 원하는 대상을 찾았는지 나타내는 결과 변수를 도입하는 것이다.
        # 대상을 찾자마자 break 로 빠져나온다.
        def coprime_alternative(a:int, b:int):
            is_coprime = True
            for i in range(2, min(a, b) + 1):
                if (a % i == 0) and (b % i == 0):
                    is_coprime = False
                    break

            return is_coprime

        assert coprime_alternative(a, b)
        assert not coprime_alternative(3, 6)

    @staticmethod
    def betterway_10_avoid_duplicate_using_assignment_expression():
        """
        Better way 10. 대입식을 사용해 반복을 피하라.
        """
        fresh_fruit = {
            "사과": 10,
            "바나나": 8,
            "레몬": 5
        }

        def make_lemonade(count: int) -> None:
            print(f"레몬 {count}개를 사용하여 lemonade 를 제조한다!!")

        def make_apple_juice(count: int) -> None:
            print(f"사과 {count}개를 사용하여 apple juice 를 제조한다!!")

        def out_of_stock() -> None:
            print("out_of_stock!!")

        count = fresh_fruit.get("레몬", 0)
        if count:
            make_lemonade(count)
        else:
            out_of_stock()

        # 위 코드에서의 문제점은 일단 잡음이 만다는 것
        # count 변수는 if 문의 첫번 째 블록 안에서만 쓰인다.
        # if 앞에서 count 를 정의하면 else 블록이나 그 이후의 코드에서 count 변수에 접근해야 할 필요가
        # 있는 것 처럼 보이기 때문에 실제보다 변수가 중요해 보인다.
        # 하지만 그렇지 않다.
        # 따라서 이런 부분을 처리할 때 대입식을 사용하라.
        # := 는 왈러스 연산자라고 한다. (대입 후 평가)

        if count := fresh_fruit.get("레몬", 0):
            make_lemonade(count)
        else:
            out_of_stock()

        # 단 한 줄이 짧지만, count 가 if 문의 첫번 째 블록에서만 의미가 있다는 점이 명확해보인다.

        count = fresh_fruit.get("사과", 0)
        if count >= 4:
            make_apple_juice(count)
        else:
            out_of_stock()

        # refactoring
        if (count := fresh_fruit.get("사과", 0)) >= 4:
            make_apple_juice(count)
        else:
            out_of_stock()

    @staticmethod
    def betterway_10_avoid_duplicate_using_assignment_expression_ex2():
        """
        Better way 10. 대입식을 사용해 반복을 피하라. (두번 째)
        # 요구 사항
        - 스무디를 만들 때 필요한 바나나의 수는 최소 2개이다.
        - 바나나가 부족하면 OutOfBananas 예외를 발생시킨다.
        - 그렇지 않다면 스무디를 만들어서 리턴한다.
        """
        INGREDIENT_NAME_BANANA: str = "바나나"
        NEED_COUNT_FOR_SMOOTHIE: int = 2

        # 현재 과일의 재고
        fresh_fruit = {
            "사과": 10,
            "바나나": 8,
            "레몬": 5
        }

        class OutOfBananasException(Exception):
            pass

        def slice_ingredient(count:int):
            if fresh_fruit[INGREDIENT_NAME_BANANA] < count:
                raise OutOfBananasException(f"{INGREDIENT_NAME_BANANA} 재고 부족")
            fresh_fruit[INGREDIENT_NAME_BANANA] = (
                fresh_fruit[INGREDIENT_NAME_BANANA] - count
            )

        def make_smoothies(count: int) -> str:
            return "바나나 스무디"

        def out_of_stock(ingredient_name:str):
            print(f"{ingredient_name} 재고 부족.")

        try:
            slice_ingredient(NEED_COUNT_FOR_SMOOTHIE)
        except OutOfBananasException:
            out_of_stock(INGREDIENT_NAME_BANANA)

        ret = make_smoothies(NEED_COUNT_FOR_SMOOTHIE)
        print(ret)
        print(fresh_fruit)


if __name__ == "__main__":
    effective_python_chapter1 = EffectivePythonChapter1()
    # effective_python_chapter1.test_bubble_sort()
    # EffectivePythonChapter1.betterway_06_use_unpacking_than_using_index()
    # EffectivePythonChapter1.betterway_07_use_enumerate_than_range()
    # EffectivePythonChapter1.betterway_08_use_zip()
    # EffectivePythonChapter1.betterway_09_not_use_else_block_to_for_or_while()
    # EffectivePythonChapter1.betterway_10_avoid_duplicate_using_assignment_expression()
    # EffectivePythonChapter1.betterway_10_avoid_duplicate_using_assignment_expression_ex2()
