
def evennumbers():
    i = 1
    even = []
    while i <=100:
        if i%2 ==0:
            even.append(i)
        i = i + 1
    return even
def oddnumbers():
    i = 1
    odd = []
    while i <=100:
        if i%2 !=0:
            odd.append(i)
        i = i + 1
    return odd

print("the even numbers are:",evennumbers())
print("the odd numbes are:",oddnumbers())