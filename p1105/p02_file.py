import os

# 1. 통로(stream) : 파일열기
# r:읽기모드, w:쓰기모드, a:추가모드
# f = open("C:/down/aaa.txt","r",encoding="utf8")
# while True:
    # txt = f.read()
    # if txt == "": break
    # print(txt,end="")

# readline() : 1줄씩 가져오기
# while True:
#     txt = f.readline()  # read()-속도느림,readline()-1줄,readlines()-전체
#     if txt == "": break
#     print(txt,end="")  # print완료후 줄바꿈을 해줌.
    
# readlines() : 전체 가져오기    
# txt_list = f.readlines()   # 1줄씩 리스트에 담아서 가져옴.
# for txt in txt_list:
#     print(txt,end="")   
    
# f.close()