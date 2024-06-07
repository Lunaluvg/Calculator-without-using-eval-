import math # Luna calculator V2.2.1 Now you can use bracket () example 1/(5+5) , 1/-(5+5) or you want more longer 20/11*(15+7/10*(14/6-(9/54))+11/8-3*(13/9+6/4))+10*(8/12-5/3)+7*(12/15-(14/10*2)) = -7.530303030303033
print("Note: You can use p as 3.141592 or e as 2.718281, example --> calculate: 1/p ; output: = 0.3183")

def my_eval(first_input):
    for starting in enumerate(first_input):
        if (starting[1] in '+-*/.') and ( first_input[starting[0]+1] in '+-/*.' and first_input[starting[0]+1] not in "-") or (first_input[-1] in '+-*/'):
            return False
        
        elif (starting[1] not in '+-*/.' and (starting[1].lower() != "p" and starting[1].lower() != "e") and starting[1].isdigit() != True) or (first_input[0] in '+*/.'):
            return False
        
        elif first_input[starting[0]] == '/' and first_input[starting[0]+1] == '0':
            return "Can not divide by zero!"
    try:
        float(first_input)
        return str(first_input)

    except ValueError:
        if first_input.isdigit() == True:
            return str(first_input)

        elif first_input.lower() == "p":
            return str(math.pi)
 
        elif first_input.lower() == "e":
            return str(math.e)

    # checking operators part
    list_number = []
    list_operator = []
    temporary = ""
    already_operate = 0

    for first_check in enumerate(first_input,0): 

        if first_check[1] == "-" and first_check[0] == 0:
            temporary += first_check[1]

        elif first_check[1].isdigit() == True or first_check[1] == "." or (first_check[1] == "p" or first_check[1] == "e") :
            if first_check[1].lower() == "p":
                temporary += str(math.pi)
                already_operate = 0
            elif first_check[1].lower() == "e":
                temporary += str(math.e)
                already_operate = 0
            else:
                temporary += first_check[1]
                already_operate = 0

            if first_check[0] == (len(first_input) - 1):
                list_number.append(float(temporary))
                temporary = ""

        elif (first_check[1] == "-") and (already_operate == 1):
            temporary += "-"
            already_operate = 0
            
        elif first_check[1] in '+-*/':
            list_operator.append(first_check[1])
            already_operate = 1

            if temporary.isdigit() == True or temporary[-1].isdigit() == True:
                list_number.append(float(temporary))
                temporary = ""

    group_main = []
    temp_list = []
    grouping = 0

    #grouping part
    for operator in range(0,len(list_operator)):

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

    group_main_2 = []
    operating = 0
    k = 0

    for from_group_main in enumerate(group_main,0): 
        if type(from_group_main[1]) == list: 
            temp_number = 1 
            for number in enumerate(from_group_main[1],0): 
                
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

    last_operator = [j for j in list_operator if j == "+" or j == "-"]

    if last_operator == []:
        return str(group_main_2[0])
    else:
        final,plus_minius = 0,0

        # summation part
        for j2 in range(0,len(group_main_2)): 

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

        return str(final)

equation = []
position = []

def find_bracket(check_bracket):

    for check_b in enumerate(check_bracket,0):

        if check_b[1] == "(":

            remove_bracket(check_b[0])

# ----------------------------------------------------------------------------

def remove_bracket(start):

    count_open,count_close = 0,0
    count_n = start
    list_position = []

    while True: 

        if f1[count_n] == "(":
            count_open += 1

        elif f1[count_n] == ")":
            count_close += 1

        count_n += 1

        if count_close == count_open:
            break

    equation.append(f1[start+1:count_n-1])
# -----------------------------------------------------------------------------

while 1:

    f1 = input("Calculate: ")

    equation.append(f1[0:])

    after_split = find_bracket(f1)

# -----------------------------------------------------------------------------

    dict_equation_value = {}

    for e1 in enumerate(list(reversed(equation)),0):
        
        tof = my_eval(e1[1])

        if type(tof) == str:

            dict_equation_value.update({e1[1]:tof})

        elif tof == False:

            real_temp_str = "" 
            ref_temp_str = "" 
            temp_str = ""
            negative = False
            keep_str = False
            keep_bracket = False
            open_bracket,close_bracket = 0,0
            wait_for_bracket = True
            

            for t1 in enumerate(e1[1],0):

                if t1[1] == ')' and open_bracket != close_bracket:

                    close_bracket += 1

                if (close_bracket == open_bracket) and (close_bracket != 0 and open_bracket != 0):

                    ref_temp_str = temp_str
                    
                    for t2 in dict_equation_value: 

                        if ref_temp_str == t2:

                            if negative != True:

                                real_temp_str += dict_equation_value[t2]

                            else: # -1*-(-1) = -1

                                result_after_negative = my_eval(dict_equation_value[t2]+'*-1')
                                
                                if float(result_after_negative) > 0 and real_temp_str == "":
                                    
                                    real_temp_str += "+"+result_after_negative
                                    
                                elif float(result_after_negative) > 0 and (real_temp_str[-1] != '*' and real_temp_str[-1] != '/'): # fixed case -(5)-(-5) = 0

                                    real_temp_str += "+"+result_after_negative

                                else:
                                    real_temp_str += result_after_negative

                            negative = False
                            ref_temp_str = ""
                            temp_str = ""
                            keep_str = False
                            keep_bracket = False
                            wait_for_bracket = True
                            open_bracket = 0
                            close_bracket = 0


                elif t1[1] != '(' and keep_str == True:

                    temp_str += t1[1]

                elif wait_for_bracket == True and t1[1] != '(':

                    if e1[1][t1[0]] == '-' and e1[1][t1[0]+1] == '(':

                        negative = True

                    else:
                        real_temp_str += t1[1]

                elif t1[1] == '(' and keep_bracket == True:

                    temp_str += t1[1]
                    open_bracket += 1

                elif t1[1] == '(' and keep_bracket == False:
                        
                    wait_for_bracket = False 
                    keep_bracket = True
                    keep_str = True 
                    open_bracket += 1

            if real_temp_str[0] == "+":
                real_temp_str = real_temp_str[1:]

            result_tof_false = my_eval(real_temp_str)

            dict_equation_value.update({e1[1]:result_tof_false})

    print("=",dict_equation_value[f1])
