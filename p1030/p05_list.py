stu_list = [
    ['홍길동',80,80,80,240,80.00],
    ['유관순',90,90,90,280,90.00],
    ['이순신',100,100,100,300,100.00]
] 
print('''\
    [ 수정할 학생번호 ]
    0.홍길동
    1.유관순
    2.이순신
    '''
)
num = int(input("수정할 학생번호를 입력하세요.>> "))
# 1번 선택
# 국어점수를 70점으로 변경하고, 합계,평균변경해서 출력하시오.
stu_list[1][1] = 70
stu_list[1][4] = stu_list[1][1]+stu_list[1][2]+stu_list[1][3]
stu_list[1][5] = stu_list[1][4]/3
print(stu_list)




# stu_list[2][2] = 70
# stu_list[2][4] = stu_list[2][2]+stu_list[2][3]+stu_list[2][4]
# stu_list[2][5] = stu_list[2][4]/3

# print(stu_list)





# # 
# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2] = 80
# print(stu_list)

# a_list = [1,2,3]
# a_list[1] = 100
# print(a_list[1])
# print(a_list)



# a_list = [1,2,3,4,5,6,7,8,9]  # len(a_list) 9
# b_list = [                    # len(b_list) 3
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a_list[3] = 100
# print(a_list)
# b_list[1][0] = 100
# print(b_list)
# b_list[2][1] = 50
# print(b_list)


# # 1차원 리스트 출력
# for a in a_list:
#     print(a,end="\t")
# print()

# print("-"*50)    
# for bs in b_list:
#     for b in bs:
#         print(b,end="\t")    



