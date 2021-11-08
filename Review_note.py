# Nogrowth's coding note

print("####example1####")
# 지역변수 vs 전역변수
# 지역변수 : 함수 안에서 정의된 변수. 함수 빠져나오면 저장된 값 지워진다.
# 전역변수 : 함수 밖에서 정의된 변수. 함수와 상관없다.

def func1():
    ex1 = 3
    print(ex1) # 함수 안에서 지정한 지역변수를 출력하고, 출력 후 함수 빠져나가면 값 삭제
ex1 = 1
func1()
print(ex1)

print("\n####example2####")




