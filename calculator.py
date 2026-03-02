# සරල කැල්කියුලේටරයක්

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "දෝෂයකි! 0න් බෙදිය නොහැක."
    return x / y

print("ක්‍රියාව තෝරන්න:")
print("1. එකතු කිරීම (+)")
print("2. අඩු කිරීම (-)")
print("3. ගුණ කිරීම (*)")
print("4. බෙදීම (/)")

choice = input("ඔබේ තේරීම (1/2/3/4): ")

num1 = float(input("පළමු සංඛ්‍යාව ඇතුළත් කරන්න: "))
num2 = float(input("දෙවන සංඛ්‍යාව ඇතුළත් කරන්න: "))

if choice == '1':
    print("පිළිතුර:", add(num1, num2))
elif choice == '2':
    print("පිළිතුර:", subtract(num1, num2))
elif choice == '3':
    print("පිළිතුර:", multiply(num1, num2))
elif choice == '4':
    print("පිළිතුර:", divide(num1, num2))
else:
    print("වැරදි තේරීමකි!")
