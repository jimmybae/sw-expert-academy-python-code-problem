# madam
# 입력하신 단어는 회문(Palindrome)입니다.
a = input()
b = a[::-1]
if a == b:
    print(a)
    print("입력하신 단어는 회문(Palindrome)입니다.")