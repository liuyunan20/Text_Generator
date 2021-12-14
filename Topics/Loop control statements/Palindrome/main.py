word = input()
if len(word) % 2 == 0:
    back_word = ''.join(reversed(word))
    if back_word == word:
        print('Palindrome')
    else:
        print('Not palindrome')
else:
    print('Not palindrome')
