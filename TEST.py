#Here are Python solutions to all the 8 questions from the image you shared:

1. Decimal Number to Words



import inflect

def decimal_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n).capitalize()

# Example
num = int(input("Enter a number: "))
print("Output:", decimal_to_words(num))




2. Roman Numerals to Decimal

def roman_to_decimal(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(roman):
        value = roman_map[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

# Example
roman = input("Enter a Roman number: ").upper()
print("Output:", roman_to_decimal(roman))
3. Character Pattern Printing




def print_pattern(n):
    for i in range(n, 0, -1):
        left = ''.join([chr(65 + j) for j in range(i)])
        right = ''.join([chr(65 + j) for j in range(i-1, -1, -1)])
        print(left + " " + right)

# Example
rows = int(input("Enter number of rows: "))
print_pattern(rows)


4. Diamond Star Pattern





def diamond_pattern(n):
    for i in range(n):
        print(" "*(n-i-1) + "* "*(i+1))
    for i in range(n-1):
        print(" "*(i+1) + "* "*(n-i-1))

# Example
rows = int(input("Enter number of rows: "))
diamond_pattern(rows)



5. Prime Numbers in Range

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

# Example
start = int(input("Enter start: "))
end = int(input("Enter end: "))
primes_in_range(start, end)




6. Longest Word in Sentence (No inbuilt string methods)

def longest_word(sentence):
    max_len = 0
    longest = ''
    word = ''
    for ch in sentence + ' ':
        if ch != ' ':
            word += ch
        else:
            length = 0
            for _ in word:
                length += 1
            if length > max_len:
                max_len = length
                longest = word
            word = ''
    return longest

# Example
sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(sentence))




7. Fibonacci Series Till n Terms

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example
n = int(input("Enter n: "))
fibonacci(n)
8. GCD of Multiple Numbers
python
Copy
Edit
def find_factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def gcd_of_list(nums):
    common = set(find_factors(nums[0]))
    for num in nums[1:]:
        common &= set(find_factors(num))
    return max(common)

# Example
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("GCD is:", gcd_of_list(numbers))
