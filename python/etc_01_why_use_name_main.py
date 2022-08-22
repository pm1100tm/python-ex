"""
Q. if __name__ == '__main__' 은 왜 사용해야 할까?

해당 모듈이 import 된 경우가 아니라, interpreter 에서 직접 실행된 경우에만,
if 문 이하의 코드를 실행시키라는 명령어이다.
"""

def func():
    print("func working")

if __name__ == "__main__":
    # interpreter 에서 직접 실행하면, __name__ 변수에 "__main__" 이 담겨서 프린트 된다.
    # 반면 모듈에서 임포트해서 실행하면 __name__ 변수에 "executeThisModule" 에 담겨서 프린트 된다.
    # 즉, __name__ == __main__은 interpreter 에서 직접 실행했을 경우에만 if문 내의 코드를 실행하라는 명령이 됩니다.

    print("직접 실행")
    print(__name__) # __main__

    # __name__ 은 무엇일까?
    # interpreter 가 실행 전에 만들어 둔 글로벌 변수이다.

else:
    print(f"used by {__name__} module by imported")


print(1)
print(2)
print(3)

print(1)
print(2)
print(3)

print(1)
print(2)
print(3)

print(1)
print(2)
print(3)
