# MyFirstCalculator
# !!(double operator)!! New updated , Now you can do this!! 1--1 = 2 or 1+-5*-7--5 = 41 etc.

# Luna calculator V2.0
first_input = input("Calculate: ") 
list_number = []
list_operator = [] 
temporary = "" 
already_operate = 0

# checking operators part
for f in enumerate(first_input,0):

    if f[0] == (len(first_input) - 1) and f[1].isdigit() != True:
        print("Your equation is incomplete!")
        quit()

    if f[1] == "-" and f[0] == 0:
        temporary += f[1]

    elif f[1].isdigit() == True or f[1] == ".":
        temporary += f[1]
        already_operate = 0

        if f[0] == (len(first_input) - 1):
            list_number.append(float(temporary))
            temporary = ""

    elif (f[1] == "-") and (already_operate == 1):
        temporary += "-"
        already_operate = 0

    elif f[1] in '+-*/':

        list_operator.append(f[1])
        already_operate = 1

        if temporary.isdigit() == True or temporary[-1].isdigit() == True:

            list_number.append(float(temporary))
            temporary = ""
    
# print(list_number) 
# print(list_operator)
group_main = []
temp_list = []
grouping = 0
# 1+2+3*5*3+2/4*2/4-5/8-5.5+10 ignore it, just my debug :)
# [1 2 3 5 3 2 4 2 4 5 8 5.5 10]  len() = 13
# [ + + * * + / * / - / - + ]  len() = 12

#grouping part
for operator in range(0,len(list_operator)):  # range(0,12) = 0,1,2,...,11

    if list_operator[operator] == "*" or list_operator[operator] == "/":

        temp_list.append(list_number[operator]) 
        grouping = 1

    if grouping == 1 and (list_operator[operator] == "+" or list_operator[operator] == "-"):

        temp_list.append(list_number[operator])
        group_main.append(temp_list)
        temp_list = []
        grouping = 0

    elif grouping == 0 and (list_operator[operator] == "+" or list_operator[operator] == "-"):
        group_main.append(list_number[operator])

    if operator == len(list_operator)-1 and grouping == 0:
        group_main.append(list_number[operator+1])

    if grouping == 1 and operator == len(list_operator) - 1:
            temp_list.append(list_number[operator+1])
            group_main.append(temp_list)

# print(group_main)

group_main_2 = []
operating = 0
k = 0

# calculation part
for i in enumerate(group_main,0): # i = (2 , [3,5,3])

    if type(i[1]) == list: # [3,5,3]

        temp_number = 1 

        for number in enumerate(i[1],0):  # i[1] = [3,5,3] , number{round 1} = (0, 3) ; number[1] == 3
            
            if number[0] == len(i[1]) - 1:
                group_main_2.append(temp_number)
                temp_number = 1
                operating = 0
                break

            elif (list_operator[i[0]+k] == "*" or list_operator[i[0]+k] == "/") and operating == 0: 

                if list_operator[i[0]+k] == "*":

                    temp_number *= number[1] * i[1][number[0]+1]
            
                if list_operator[i[0]+k] == "/":

                    temp_number = 0
                    try:
                        temp_number += number[1] / i[1][number[0]+1]
                    except Exception:
                        print("Divide by zero is detected!")
                        quit()

                operating = 1

            elif (list_operator[i[0]+k] == "*" or list_operator[i[0]+k] == "/") and operating == 1:

                if list_operator[i[0]+k] == "*":

                    temp_number *= i[1][number[0]+1]

                if list_operator[i[0]+k] == "/":
                    try:
                        temp_number /= i[1][number[0]+1]
                    except Exception:
                        print("Divide by zero is detected!")
                        quit()
            k += 1

    else:
        group_main_2.append(i[1])


if ("+") not in list_operator and ("-") not in list_operator:
    print("=",group_main_2[0])
    quit()

last_operator = []

#print(group_main_2)

for j in list_operator:

    if j == "+" or j == "-":
        last_operator.append(j)

final = 0
plus_minius = 0

#print(last_operator)
# summation part

for j2 in range(0,len(group_main_2)): # 0 - 6

    if j2 == len(group_main_2)-1:
        break

    if last_operator[j2] == "+" and plus_minius == 0:

        final = group_main_2[j2] + group_main_2[j2+1]
        plus_minius = 1

    elif last_operator[j2] == "-" and plus_minius == 0:
        final = group_main_2[j2] - group_main_2[j2+1]
        plus_minius = 1

    elif last_operator[j2] == "+" and plus_minius != 0:
        final += group_main_2[j2+1]

    elif last_operator[j2] == "-" and plus_minius != 0:
        final -= group_main_2[j2+1]

print("=",final)