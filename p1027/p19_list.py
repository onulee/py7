# 이름,국어,영어,수학,합계,평균

stus = []
# 3명의 학생성적을 입력받아 stus에 모두 저장하여 출력하시오.
#---
stu = []
name = input("학생이름을 입력하세요.")
stu.append(name)
kor = int(input("국어점수를 입력하세요."))
stu.append(kor)
eng = int(input("영어점수를 입력하세요."))
stu.append(eng)
math = int(input("수학점수를 입력하세요."))
stu.append(math)
total = kor+eng+math
stu.append(total)
avg = total/3
stu.append(avg)
stus.append(stu) # 전체리스트
#----
stu = []
name = input("학생이름을 입력하세요.")
stu.append(name)
kor = int(input("국어점수를 입력하세요."))
stu.append(kor)
eng = int(input("영어점수를 입력하세요."))
stu.append(eng)
math = int(input("수학점수를 입력하세요."))
stu.append(math)
total = kor+eng+math
stu.append(total)
avg = total/3
stu.append(avg)
# 전체리스트
stus.append(stu)

stu = []
name = input("학생이름을 입력하세요.")
stu.append(name)
kor = int(input("국어점수를 입력하세요."))
stu.append(kor)
eng = int(input("영어점수를 입력하세요."))
stu.append(eng)
math = int(input("수학점수를 입력하세요."))
stu.append(math)
total = kor+eng+math
stu.append(total)
avg = total/3
stu.append(avg)

# 전체리스트
stus.append(stu)

print(stus)


print(stus[0])    #['홍길동', 100, 100, 99, 299, 99.66666666666667]
print(stus[0][0]) #홍길동
print(stus[0][1]) #100
print(stus[1])
print(stus[2])