dust = 40

if dust > 70:
    print("미세먼지 농도는 70보다 크다.")
elif dust > 50:  # dust가 70 보다 크지 않을때 조건 검사
    print("미세먼지 농도는 50보다 크다.")
elif dust > 30:
    pass  # 아무것도 하지않는 코드 (자리만 차지)
else:
    print("미세먼지 농도는 50보다 작거나 같다.")

dust = 200

if dust > 150:
    print("매우나쁨")
elif 150 >= dust > 80:
    print("나쁨")
elif dust > 30 and dust <= 80:
    print("보통")
else:
    print("좋음")

# dust 변수에 들어있는 값을 기준으로 미세먼지 정보출력
# dust 가 150 보다 크다 : 매우나쁨
# dust 가 80 보다 크고 150 이하이다 : 나쁨
# dust 가 30 보다 크고 80 이하이다 : 보통
# dust 가 30 이하이다 : 좋음
# 이렇게 출력하는 조건문을 작성해봅시다.
