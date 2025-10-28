# 년도 가져오기
import datetime
now = datetime.datetime.now()
year = now.year


# 주민번호를 입력받아, 나이를 출력하시오.
#990101-1111111
#070101-3111111
jumin = "070101-3111111" # 문자열
a1 = jumin[7]     # a1타입 - 문자열
num = int(a1)     # 문자열 -> 정수타입변경
year1 = jumin[:2] # 문자열
y_num = int(year1) # 문자열 -> 정수타입변경
# 1900년대생인지, 2000년대생인지 확인하시오.
# 조건문
if num==1 or num==2:
    print(year - (1900+y_num))
else:
    print(year - (2000+y_num))    