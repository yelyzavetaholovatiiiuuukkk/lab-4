# a
name = input("Podaj imię: ")
print("Witaj", name)

# b
age = input("Podaj wiek: ")
print("Twój wiek to:", age)

# c
first_name = input("Podaj imię: ")
last_name = input("Podaj nazwisko: ")
initials = first_name[0] + last_name[0]
print("Inicjały:", initials)

# d
string_to_repeat = input("Podaj łańcuch do powtórzenia: ")
print(string_to_repeat * 5)

# e
string1 = input("Podaj pierwszy łańcuch: ")
string2 = input("Podaj drugi łańcuch: ")
combined_string = string1 + string2
print("Połączone łańcuchy:", combined_string)

# f
string1 = input("Podaj pierwszy łańcuch: ")
string2 = input("Podaj drugi łańcuch: ")
half1 = string1[:len(string1)//2]
half2 = string2[len(string2)//2:]
combined_half = half1 + half2
print("Pierwsza połowa pierwszego łańcucha i druga połowa drugiego:", combined_half)
