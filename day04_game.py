secret_number = 7
guess = int(input("숫자를 맞춰보세요 (1~10): "))

if guess == secret_number:
    print("정답입니다! 축하해요!")

elif guess< secret_number:
    print("UP!(더 큰 숫자입니다.)")

else:
    print("down !(더 작은 숫자입니다.)")