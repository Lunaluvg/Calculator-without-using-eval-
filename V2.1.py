# Luna calculator V2.1 
def checking_operator(first_input):
    # checking operators part
    list_number = []
    list_operator = []
    temporary = "" 
    first_time = 1
    already_operate = 0
    normal = ['+','-','*','/']

    for f in enumerate(first_input,0): 

        if (f[1] in normal) and (first_input[f[0]+1] in normal and first_input[f[0]+1] != "-") or (first_input[-1] in normal):
            print("!! Your equation is incomplete or wrong !!")
            print()
            return 3.14

        if f[1] == "-" and first_time == 1:
            temporary += f[1]
            first_time = 0

        elif f[1].isdigit() == True or f[1] == ".":
            temporary += f[1]
            first_time = 0
            already_operate = 0

            if f[0] == (len(first_input) - 1):
                list_number.append(float(temporary))
                temporary = ""

        elif (f[1] == "-") and (already_operate == 1):
            temporary += "-"
            already_operate = 0

        elif f[1] in normal:

            list_operator.append(f[1])
            already_operate = 1

            if temporary.isdigit() == True or temporary[-1].isdigit() == True:

                list_number.append(float(temporary))
                temporary = ""

    return list_number,list_operator

    #print(list_number) 
    #print(list_operator)

def group(af_c):

    list_number = af_c[0]
    list_operator = af_c[1]

    group_main = []
    temp_list = []
    grouping = 0

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

    return group_main,list_operator
    #print(group_main)

def calculation(af_g):
    # calculation part
    group_main = af_g[0]
    list_operator = af_g[1]

    group_main_2 = []
    operating = 0
    k = 0

    for from_group_main in enumerate(group_main,0): # from_group_main = (2 , [3,5,3])

        if type(from_group_main[1]) == list: # [3,5,3]

            temp_number = 1 

            for number in enumerate(from_group_main[1],0):  # from_group_main[1] = [3,5,3] , number{round 1} = (0, 3) ; number[1] == 3
                
                if number[0] == len(from_group_main[1]) - 1:
                    group_main_2.append(temp_number)
                    temp_number = 1
                    operating = 0
                    break

                elif (list_operator[from_group_main[0]+k] == "*" or list_operator[from_group_main[0]+k] == "/") and operating == 0: 

                    if list_operator[from_group_main[0]+k] == "*":

                        temp_number *= number[1] * from_group_main[1][number[0]+1]

                    if list_operator[from_group_main[0]+k] == "/":

                        temp_number = 0
                        try:
                            temp_number += number[1] / from_group_main[1][number[0]+1]
                        except Exception:
                            break

                    operating = 1


                elif (list_operator[from_group_main[0]+k] == "*" or list_operator[from_group_main[0]+k] == "/") and operating == 1:

                    if list_operator[from_group_main[0]+k] == "*":

                        temp_number *= from_group_main[1][number[0]+1]

                    if list_operator[from_group_main[0]+k] == "/":
                        try:
                            temp_number /= from_group_main[1][number[0]+1]
                        except Exception:
                            break

                k += 1

        else:
            group_main_2.append(from_group_main[1])

    return group_main_2,list_operator

def if_all_operator(af_cal): # af_cal = tuple( group_main_2 , list_operator )
    
    group_main_2 = af_cal[0]
    list_operator = af_cal[1]

    last_operator = [j for j in list_operator if j == "+" or j == "-"]

    #print(group_main_2)

    final,plus_minius = 0,0

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

while 1: # main program

    skip = False
    start = input("Calculate: ")

    for s in start:

        if (s not in ['+','-','*','/','.'] and s.isdigit() != True) or (start[0] in ['+','*','/','.']):
            skip = True
            print("Sorry I don't know that :(")
            after_check = 3.14
            print()
            break
            
    if start.isdigit() == True:
        print(start)
        continue

    if skip == False:
        after_check = checking_operator(start)

    #print("af_check",after_check)
    divide_by_zero = 0
    
    if after_check != 3.14:
        if 0.0 in after_check[0] and "/" in after_check[1]:

            for z in range(0,len(after_check[0])-1):

                if after_check[1][z] == "/" and after_check[0][z+1] == 0.0:
                    divide_by_zero = 1

                if z == len(after_check[0]) - 1 and divide_by_zero == True:
                    break

    if divide_by_zero == 0 and after_check != 3.14:
        after_group = group(after_check)

    if divide_by_zero == 0 and after_check != 3.14:
        after_calculation = calculation(after_group)

    if divide_by_zero == 0 and after_check != 3.14:
        if ("+") not in after_calculation[1] and ("-") not in after_calculation[1]:
            print("=",after_calculation[0][0])

        else:
            after_calculation = if_all_operator(after_calculation)

    if divide_by_zero == 1:
        print("!! Divide by zero detected !!")
        print()
