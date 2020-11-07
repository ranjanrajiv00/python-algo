# 1st approach
def reverse(str):
    start = 0
    result = ""

    for s in str:
        result = s + result
        start = start+1
    return result

print(reverse("rajiv ranjan"))

# 2nd approach
def reverse2(str):
    if(len(str) == 0):
        return str
    return reverse2(str[1:]) + str[0]

print(reverse2("rajiv ranjan"))

# 3rd approach
def reverse3(str):
    arr = list(str)
    start = 0
    end = len(str) - 1

    while start<end:
        temp = arr[end]
        arr[end] = arr[start]
        arr[start] = temp

        start = start + 1
        end = end -1

    return "".join(arr)

print(reverse3("rajiv ranjan"))