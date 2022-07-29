# import os
# import psutil
# import time
#
#
# def calculate_memory(func):
#
#     def wrapper(*args, **kwargs):
#         process = psutil.Process(os.getpid())
#
#         t1 = time.time()
#         mem_before = process.memory_info().rss / 1024 / 1024
#         print(f"시작 전 메모리 사용량: {mem_before} MB")
#
#         func(*args, **kwargs)
#
#         t2 = time.time()
#         mem_after = process.memory_info().rss / 1024 / 1024
#         print(f"시작 후 메모리 사용량: {mem_after} MB")
#
#         total_time = t2 - t1
#         print(f"총 소요된 시간: {total_time} 초")
#
#         return func
#
#     return wrapper
