fruits = ['사과','배','복숭아','딸기','포도']
print("[ 과일리스트 ]")
# enumerate(리스트) - 리스트번호,리스트값
#  
for idx,f in enumerate(fruits):   #enumerate() 함수 : index번호 리턴
    print("{}.{}".format(idx+1,f))  # 1.사과 2.배 3.복숭아
    
print("[ 과일리스트 - range ]")    
# for i in range(5):
for i in range(len(fruits)):
    print("{}.{}".format(i+1,fruits[i]))
    
        





# 501 ~ 1000까지 홀수의 합을 출력하시오.
# sum = 0
# for i in range(501,1001):
#     if i%2 == 1:
#        sum = sum + i
# print("합계 : ",sum)        

# # 1~100까지 3의 배수의 합을 출력하시오.
# sum = 0
# for i in range(1,101):
#     if i%3 == 0:
#        sum = sum + i
# print("합계 : ",sum) 




# for문을 2번 사용 - 중첩for문
# for i in range(2,10):
#     if i%2 != 0:
#         continue #1번만 제외(9번을 실행), break:완전중지
#     print(" [ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j),end=" ")
#     print()


# 중첩for문을 사용해서 000,001,002,003....011,12,13....99
# for i in range(0,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print("kb국민 번호표 : {}{}{}".format(i,j,k))