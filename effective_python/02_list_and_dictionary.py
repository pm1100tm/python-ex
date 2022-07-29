"""
제 2장. 리스트 & 딕셔너리
"""
from typing import Any


class EffectivePythonChapter2:
    """
    시퀀스를 슬라이싱하는 방법을 익혀라.
    슬라이싱을 사용하면 최소한의 노력으로 시퀀스에 들어 있는 아이템의 부분집합에 쉽게 접근할 수 있다.
    어떤 파이썬 클래스에도 슬라이싱을 추가할 수 있다.
    __getitem__
    __setitem__
    매직 메서드를 구현하면 된다.
    커스텀 컨테이너 타입은 collections.abc 를 상속하라.
    """
    num_list = [i for i in range(10)]
    car_ages_1 = [0, 5, 6, 9, 7, 1, 20, 14, 16, 3, 2]
    car_ages_2 = [0, 5, 6]
    car_ages_3 = [5, 6]

    @classmethod
    def _print_id(cls, obj: Any):
        print(id(obj))

    def be_careful_to_negative_int_using_slice(self):
        """
        슬라이싱 할 때 음수 인덱스를 사용할 때 0 이 들어가서 [-0:] 식이 들어가게 된다면,
        [:] 와 같기 때문에, 원래의 리스트를 복사하여 새롭게 생성한 리스트를 얻게 된다.

        스트라이드와 슬라이스를 한 식에 함께 사용하지 말아라.
        """
        var_list = self.num_list
        self._print_id(var_list)

        print(var_list[3:])
        self._print_id(var_list[3:])

        print(var_list[:])
        self._print_id(var_list[:])

        # 리스트를 슬라이싱한 결과는 새로운 리스트이며,
        # 결과 값으로 얻은 리스트를 변경하면, 원래의 리스트는 바뀌지 않는다.
        # 슬라이싱에서 시작과 끝 인덱스를 모두 생략하면 원래 리스트를 복사한 새 리스트를 얻는다.
        a = var_list[:]
        b = var_list[:]
        print(id(a) == id(b))
        assert id(a) != id(b)

        b.append(100)
        print(a)
        print(b)

        c = b[:]
        assert b == c and b is not c

    def betterway_13_use_unpacking_than_slicing(self) -> None:
        """
        슬라이싱보다는 나머지를 모두 잡아내는 언패킹을 사용하라.
        꼭 언패킹해야만 하는 값 외에 여분의 슬라이스가 하나 필요한 경우,
        나머지를 모두 잡아내는 (에러없이) 이 기능의 이점을 살릴 수 있다.
        """
        # 이 코드는 더 짧고, 읽기 쉽고, 인덱스 경계 값이 어긋나서 오류가 발생할 여지가 없다.
        # !!warning: do not assign a lambda expression, use a def
        lambda_sorted = lambda x: sorted(x, reverse=True)

        car_age_1, car_age_2, car_age_3 = (
            lambda_sorted(self.car_ages_1),
            lambda_sorted(self.car_ages_2),
            lambda_sorted(self.car_ages_3),
        )

        oldest, second_oldest, *others = car_age_1
        print(oldest, second_oldest, others) # 0 5 [6, 9, 7, 1, 20, 14, 16, 3, 2]

        oldest, second_oldest, *others = car_age_2
        print(oldest, second_oldest, others) # 0 5 [6]

        oldest, second_oldest, *others = car_age_3
        print(oldest, second_oldest, others) # 5 6 []

        # * 를 다른 위치에 사용할 수도 있다.
        oldest, *others, youngest = car_age_1
        print(oldest, others, youngest) # 20 [16, 14, 9, 7, 6, 5, 3, 2, 1] 0

        oldest, *others, youngest = car_age_2 # 6 [5] 0
        print(oldest, others, youngest)

        oldest, *others, youngest = car_age_3
        print(oldest, others, youngest) # 6 [] 5

        *others, second_oldest, youngest = car_age_1
        print(oldest, second_oldest, youngest)

        # 하지만 * 식이 포함된 언패킹 대입을 처리하려면 필수인 부분이 적어도 하나는 있어야 한다.
        # 그렇지 않으면 SyntaxError 가 발생한다. 별표 식만 사용하여 언패킹할 수 없다.
        # *others = car_age_1 # Starred assignment target must be in a list or tuple

        # 또한 한 수준의 언패킹 패턴에 별표 식을 두 개 이상 쓸 수 없다.
        # first, *middle, *second_middle, last = car_age_1 # SyntaxError: multiple starred expressions in assignment
        # print(first, middle, second_middle, last)

        it = iter(range(1, 3))
        print(it) # <range_iterator object at 0x1015d7570>

        first, second = it
        print(first, second)

        def generate_csv():
            yield '날짜', '제조사', '모델', '연식', '가격'
            # ...
        all_csv_rows = list(generate_csv())
        print(all_csv_rows)

        header = all_csv_rows[0]
        rows = all_csv_rows[1:]
        print(header)
        print(rows)

        it = generate_csv()
        header, *rows = it
        print('CSV 헤더', header)
        for r in rows:
            print('CSV rows', r)

        # 하지만 * 식은 항상 리스트를 만들어내기 때문에, 이터레이터를 별표 식으로 언패킹하면
        # 컴퓨터 메모리를 모두 다 사용해서 프로그램이 멈출 수 있다.
        # 따라서 결과 데이터가 모두 메모리에 들어갈 수 있다고 확신할 때만,
        # 나머지를 모두 잡아내는 언패킹을 사용해야 한다.


if __name__ == "__main__":
    effective_python_chapter2 = EffectivePythonChapter2()
    # effective_python_chapter2.be_careful_to_negative_int_using_slice()
    effective_python_chapter2.betterway_13_use_unpacking_than_slicing()


