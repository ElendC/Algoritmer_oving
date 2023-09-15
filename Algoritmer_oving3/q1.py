
def is_palindrome_i(word):
    is_true = True

    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            is_true = False
            return word, "is not palindrome"
        else:
            return word, "is palindrome"

print("Iteration Func: ")
print(is_palindrome_i("lolol"))
print(is_palindrome_i("Thisisnot"))

print("\n \n")


def is_palindrome_r(word):

    if len(word) <= 1:
        return "it is palindrome"
    else:
        if word[0] == word[-1]:
            return is_palindrome_r(word[1:-1])
        else:
            return "Word in not palindrome"
            
        
print(is_palindrome_r("hello"))
print(is_palindrome_r("lolol"))