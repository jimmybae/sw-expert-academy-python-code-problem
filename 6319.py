def palindrome(word):
    return ''.join(reversed(word))

word = input()
if word == palindrome(word):
    print("입력하신 단어는 회문(Palindrome)입니다.")