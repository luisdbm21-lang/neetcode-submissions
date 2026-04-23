def check_range(num: int) -> str:
    answer = ""
    
    if num < 0:
        answer = "negative"
    elif num == 0:
        answer = "zero"
    elif num > 0 and num < 10:
        answer = "positive single digit"
    elif num > 10:
        answer = "positive multi digit"
    return answer
  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))
