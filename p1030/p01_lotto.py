# 로또 맞추기 프로그램을 구현하시오.
import random
# 1. 변수선언
# my_list,an_list,count,lotto
my_list = []
an_list = []
count = 0
lotto = 0

# 2. 6개 번호생성
# 6개를 랜덤으로 추출
lotto = random.sample(range(1,46),6)
print(lotto)
# 3. 6개 번호입력
i = 0
while i<6:  # 1~45
    num = input("{}번째 로또번호를 입력하세요.".format(i+1))
    if not num.isdigit(): # 문자열이 숫자인지 확인해주는 함수
        print("숫자가 아닙니다. 숫자만 입력가능합니다.")
        continue
        
    num = int(num)
    if 1<= num <= 45:
        my_list.append(num)
        i = i + 1
    else:
        print("1~45번까지 번호 또는 숫자만 입력하셔야 합니다.")    


# 4. 번호확인
# for lo in lotto:             # [1,3,9,10,15,45]
#     for my in my_list:       # [ 5, 9, 11,12,36, 40]
#         if lo == my: #
#             an_list.append(i)
#             count = count + 1
#             break
        
for my in my_list:       # [ 5, 9, 11,12,36, 40]
    #if lo == my: #
    if my in lotto:      # 5  [1,3,9,10,15,45]
        an_list.append(my)
        count = count + 1

# 5. 결과출력
print("로또번호 : ",lotto)
print("입력번호 : ",my_list)
print("당첨번호 : ",an_list)
print("당첨개수 : ",count)