#990101-1111111
#870101-2111111

#070101-4111111
# 1 - 남자,2 - 여자 
# 주민번호를 입력받아, 남자인지,여자인지 출력하시오.
import datetime
now = datetime.datetime.now()
month = now.month

jumin = input("주민번호를 입력하세요.")
ju1 = int(jumin[7])
if ju1 == 1:
    print("남자입니다.")
else:
    print("여자입니다.")    
    
m1 = int(jumin[2:4])
if month == m1:
    print("이벤트 대상")
else:
    print("이벤트 대상이 아닙니다.")        
    