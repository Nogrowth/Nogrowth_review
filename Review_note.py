# Nogrowth's coding note

print("####지역변수와 전역변수####")
# 지역변수 vs 전역변수
# 지역변수 : 함수 안에서 정의된 변수. 함수 빠져나오면 저장된 값 지워진다.
# 전역변수 : 함수 밖에서 정의된 변수. 함수와 상관없다.

def func1():
    ex1 = 3
    print(ex1) # 함수 안에서 지정한 지역변수를 출력하고, 출력 후 함수 빠져나가면 값 삭제
ex1 = 1
func1()
print(ex1)

print("\n\n####변수와 객체, 변수의 저장 위치####")
# 변수와 객체
# a = 10 이라면 변수 a에 객체 10을 저장한 것
# 앞으로 a라는 변수를 통해 객체 10에 접근하게 됨, 실제 주소는 id(a)

ex2 = 2
print("2라는 객체값이 변수 ex2에 저장되었고, 그 위치는 ")
print(id(ex2))

print("\n\n####String 자료형####")
# string 자료형의 indexing과 slicing이 가능하다

ex3 = "abcde"
print("indexing : ", ex3[2])
print("공백 slicing : ", ex3[2:]) # 2번 index부터 끝까지
print("공백 slicing : ", ex3[:3]) # 0번 index부터 3번 index 전까지
print("간격 두고 slicing : ", ex3[0:4:2])
print("음수 간격 slicing : ", ex3[-1:-3:-1]) # 맨 뒤에서부터 -1, -3번 index 전까지 -1씩 움직이면서!

print("\n\n####List 자료구조####")
# 자료구조 list = [], tuple = (), dictionary = {"key":value}

# list 자료형 : indexing, slicing 가능하며 수정 가능하다
# 수정
list1 = [1, 2, 3, 4, "사과"]
list1.append('3.4') # list의 맨 뒤에 추가
print(list1)
list1.insert(3, '오렌지') # list의 3번 index 자리에 원소를 추가
print(list1)
del list1[0] # list의 원소 삭제
print(list1)


print("\n\n####Dict 자료구조####")
# 순서가 없다. key와 value만 있을 뿐
# 순서가 없기 때문에 당연히 append 등 method를 쓸 수 없다.
# key는 항상 str형태

dict1 = {'사과':3, '배':2}
dict1['오렌지'] = 4 # 오렌지라는 key에 대응하는 4라는 value를 함께 dictionary에 추가해준다.
print(dict1)

print(dict1.keys()) # dict의 key를 list로 모아서 dict_keys 형태의 자료형으로 받는다.
print(dict1.values()) # 마찬가지로 dict_values 형태의 자료형으로 받는다.
print("각각의 자료형은", type(dict1.keys()), type(dict1.values()))


print("\n\n####Formatting####")
# %을 이용한 formatting
# %d : 정수, %s : 문자열, %f : 실수, %% : 문자 % 자체
ex4 = 50
str1 = 'my age is %d' % ex4
print(str1)
print("내 나이는 %d살 입니다." % ex4)

ex5 = '철수'
print("%s의 나이는 %d살 입니다." % (ex5, ex4))

# format 함수를 이용한 formatting
# {} 안에 indexing을 하고, 뒤에 .format(, , , )에 필요한 것들을 넣어준다.
print("format 함수 사용 : {}의 나이는 {}살 입니다.".format(ex5, ex4))
print("format 함수 사용 : {1}의 나이는 {0}살 입니다.".format(ex5, ex4))


# f-string을 이용한 formatting
# f-string은 python 3.6부터 지원되는 변수
# 문자열 앞에 f만 붙이고 중괄호 안에 변수명을 써주면 자동으로 변환됨

print(f"f-string 사용 : {ex5}의 나이는 {ex4}살 입니다.")


print("\n\n####Module####")
# module이란 .py로 쓰이는 file과 같다고 생각하자
# 왜 module을 쓰는가? 한번 file을 만들어놓고, 다른 file에서 불러다 쓰기 좋다. import로

# import module1으로 불러올 경우 : module 내 함수나 변수 사용 시 module.함수 or module.변수
# from module1 import func1 으로 함수만 불러올 경우 : 그냥 함수 자체로 사용 가능
# from module1 import * : 모든 구성요소를 가져오나, module.함수 등으로 사용할 필요 없다
