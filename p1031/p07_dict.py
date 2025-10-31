import random

english = {
    '사랑':'love','차':'car','커피':'coffee','전화':'phone','컴퓨터':'computer',
    '이름':'name','한국':'korea','물':'water','지구':'earth','하늘':'sky',
    '공기':'air','고양이':'cat','강아지':'dog','아기':'baby','엄마':'mother',
    '아빠':'father','집':'house','소년':'boy','소녀':'girl','열쇠':'key'
}

# 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 만드시오.
a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
quest = random.sample(a_list,5)   # 랜덤5개 - 20문제중 5개를 추출
quest.sort()                      # 랜덤5개 순서대로 정렬
quest_dic = {}                    # 정답,오답 입력을 위한 저장공간
# print(quest) #[0, 11, 12, 14, 17, 19]
num = 1
for i,k in enumerate(english.keys()): # index을 함께 추출,key
    if i in quest:
        # print(i,k,english[k])
        count = 0
        # 정답입력
        print("{} 은(는) 영어로 뭘까요? ".format(k))
        answer = input(">> ")
        # 정답확인
        if answer == english[k]:
            print("띵동! 정답입니다.")
            count = count + 1    # count += 1
            quest_dic[num]  = "정답"   #i+1= 1
        else:
            print("오답 : ",english[k])
            quest_dic[num] = "오답"
        num = num + 1
# 1:정답 2:오답 3:오답 4:정답 5:정답
print(quest_dic)
print("정답 :",count) 



# 영어맞추기 프로그램을 구현하시오.
# 사랑 ? love
# count = 0
# for k,v in english.items():
#     # 정답입력
#     print("{} 은(는) 영어로 뭘까요? ".format(k))
#     answer = input(">> ")
#     # 정답확인
#     if answer == v:
#         print("띵동! 정답입니다.")
#         count = count + 1    # count += 1
#     else:
#         print("오답 : ",v)
    
    
#     # 1:정답 2:오답 3:오답 4:정답 5:정답
#     print("정답 :",count) 