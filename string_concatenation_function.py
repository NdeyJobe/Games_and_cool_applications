"""A function that concatenates strings is the same as a function that sums up numbers"""
n = ["Michael", "Lieberman", "love"]
n = [3, 5, 7]
#function 1
def join_strings(words):
    results = ""
    for i in words:
        results += i
    return results
print join_strings(n)

#function 2
def totals(numberss):
    results = ""
    for i in range(len(numberss)):
        results += numberss[i]
    return results
print totals (n)

#function 3
def total(numbers):
    result = 0
    for i in numbers:
        result += i
    return result
print total (n)

