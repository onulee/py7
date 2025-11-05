# 학생성적 1명 클래스
class Student:
    # 전역변수 만들어짐.
    def __init__(self,stuno,name,kor,eng,math):
        self.stuno = stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
    # 객체,참조변수를 출력하면 함수실행을 시킴
    def __str__(self):
        return (f"{self.stuno}\t{self.name}\t{self.kor}\t\
{self.eng}\t{self.math}\t{self.total}\t\
{self.avg:.2f}\t{self.rank}\t")

    def s_total(self):
        self.total = self.kor+self.eng+self.math  
    def s_avg(self):
        self.avg = self.total/3  

# 학생성적리스트 클래스                
class Students:
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
    def print(self):
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*65)
        print(*self.titles,sep="\t")
        print("-"*65)
        for stus in self.stu_list:
            print(stus)
        print()
    
    def add(self,student):
        self.stu_list.append(student)

stus = Students()                

# Students 클래스에서 리스트에 추가
stus.add(Student(10101,'홍길동',100,100,99))
stus.add(Student(10102,'유관순',90,90,99))
stus.add(Student(10103,'이순신',80,80,99))

stus.print()

