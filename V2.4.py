import math 
# example
# 20/11*(15+7/10*(14/6-(9/54))+11/8-3*(13/-9+6/4))+10*(8^-2/12-5/3)+7*(12/15-(14/10*2)) = 1.5736268939393856
# (((1712/10)-(-(19+8/11*(13/9-(8/716))/6))+22)-(10*(16/13+14/8))-(11*(20/15-(13/7))))+(15*(21/18-(11/12^-7))) = -5912248114.172058
# -2^2 = -4 , (-2)^2 = 4 , (-2)^3 = -8
def my_eval(first_input):
    
    for starting in enumerate(first_input):
        if (starting[1] in '+-*/.') and ( first_input[starting[0]+1] in '+-/*.' and first_input[starting[0]+1] not in "-") or (first_input[-1] in '+-*/'):
            return False
        
        elif (starting[1] not in '+-*/.' and (starting[1] not in "peij") and starting[1].isdigit() != True) or (first_input[0] in '+*/.'):
            return False
    try:
        float(first_input)
        return str(first_input)

    except ValueError:
        if first_input.isdigit() == True:
            return str(first_input)

        elif first_input == "p":
            return str(math.pi)
 
        elif first_input == "e":
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
            if first_check[1] == "p":
                temporary += str(math.pi)
                already_operate = 0
            elif first_check[1] == "e":
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
                            return False

                    operating = 1

                elif (list_operator[from_group_main[0]+k] == "*" or list_operator[from_group_main[0]+k] == "/") and operating == 1:

                    if list_operator[from_group_main[0]+k] == "*":
                        temp_number *= from_group_main[1][number[0]+1]

                    if list_operator[from_group_main[0]+k] == "/":
                        try:
                            temp_number /= from_group_main[1][number[0]+1]
                        except Exception:
                            return False
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


equation_1 = []
dict_equation_value = {}

def find_bracket(check_bracket):

    for check_b in enumerate(check_bracket,0):
        if check_b[1] == "(":
            remove_bracket(check_b[0])
# ----------------------------------------------------------------------------
def remove_bracket(start):

    count_open,count_close = 0,0
    count_n = start

    while True: 
        if f1[count_n] == "(":
            count_open += 1
        elif f1[count_n] == ")":
            count_close += 1

        count_n += 1
        if count_close == count_open:
            break

    equation_1.append(f1[start+1:count_n-1])

def simplify_negative(simplify):

    last_anwser = "" 
    temp_num = "" 
    count_negative = 0 
    first_time = True 

    for last_check in enumerate(simplify,0):

        if last_check[1].isdigit() == True or last_check[1] == '.':
            temp_num += last_check[1]

            if last_check[0] == len(simplify) - 1:
                if count_negative % 2 != 0:
                    last_anwser += '-'+temp_num

                elif count_negative % 2 == 0 and last_anwser == '':
                    last_anwser += temp_num

                elif count_negative % 2 == 0 and last_anwser[-1] not in '*/+':
                    last_anwser += '+'+temp_num

                elif count_negative % 2 == 0:
                    last_anwser += temp_num

        elif last_check[1] == '-' and count_negative == 0 and first_time != True:
            last_anwser += temp_num
            temp_num = ''

        elif last_check[1] == '-' and simplify[last_check[0]-1].isdigit() == True:

            if count_negative % 2 == 0 and count_negative != 0:
                last_anwser += '+' + temp_num

            elif count_negative % 2 == 0:
                last_anwser += temp_num
            else:
                last_anwser += '-'+temp_num

            temp_num = ''
            count_negative = 0

        elif last_check[1].isdigit() != True and last_check[1] != '-':

            if count_negative % 2 == 0 and count_negative != 0:
                last_anwser += '+' + temp_num + last_check[1]

            elif count_negative % 2 == 0:
                last_anwser += temp_num + last_check[1]

            elif count_negative % 2 != 0:
                last_anwser += '-' + temp_num + last_check[1]

            temp_num = ""
            count_negative = 0

        if last_check[1] == '-':
            count_negative += 1

        first_time = False

    if my_eval(last_anwser) == False:
        return False
    else:
        return last_anwser
# ----------------------------------------------------------------------------- 
def parenthesis(equation_2):

    divide_by_zero = False

    for e1 in enumerate(list(reversed(equation_2)),0):
        
        real_temp_str = ""
        temp_str = ""
        keep_str,keep_bracket,have_bracket = False,False,False
        open_bracket,close_bracket = 0,0
        wait_for_bracket = True
        
        for t1 in enumerate(e1[1],0):

            if t1[1] == ')' and open_bracket != close_bracket:
                close_bracket += 1

            if (close_bracket == open_bracket) and (close_bracket != 0 and open_bracket != 0):
                
                for t2 in dict_equation_value:
                    if temp_str == t2:
                        real_temp_str += dict_equation_value[t2]
                        temp_str = ""
                        keep_str = False
                        keep_bracket = False
                        wait_for_bracket = True
                        open_bracket,close_bracket = 0,0

            elif t1[1] != '(' and keep_str == True:
                temp_str += t1[1]

            elif wait_for_bracket == True and t1[1] != '(':

                if t1[1] == '-':
                    real_temp_str += t1[1]
                else:
                    real_temp_str += t1[1]

            elif t1[1] == '(' and keep_bracket == True:
                temp_str += t1[1]
                open_bracket += 1

            elif t1[1] == '(' and keep_bracket == False:
                    
                wait_for_bracket = False 
                keep_bracket,keep_str = True,True
                open_bracket += 1

        if e1[1].count(')^') != 0 and e1[1].count('^(') == 0 or e1[1].count(')^(') > 0:
            have_bracket = True

        if '^' in real_temp_str:
            last_anwser_expo,temp_num_ex = "","" 
            expo,base = '',''
            in_expo,skip = False,False

            for check_expo in enumerate(real_temp_str,0):

                if skip == True:
                    skip = False
                    continue

                elif (check_expo[1].isdigit() == True or check_expo[1] == '.' or check_expo[1] in 'pe') and (in_expo == False):

                    if check_expo[1] == 'p':
                        temp_num_ex += str(math.pi)

                    elif check_expo[1] == 'e':
                        temp_num_ex += str(math.e)

                    else:
                        temp_num_ex += check_expo[1]

                    if check_expo[0] == len(real_temp_str) - 1:
                        last_anwser_expo += temp_num_ex

                elif check_expo[1] in '+-*/' and in_expo == False:
                    last_anwser_expo += temp_num_ex + check_expo[1]
                    temp_num_ex = ''

                elif in_expo == True and check_expo[1] == '-' and real_temp_str[check_expo[0]+1] == '-' and real_temp_str[check_expo[0]-1] == '^':
                    skip = True

                elif in_expo == True and check_expo[1] == '-' and real_temp_str[check_expo[0]-1] == '^':
                    expo += '-'

                elif check_expo[1] in '+-*/' and in_expo == True:
                    
                    if have_bracket == True and float(expo) < 1 and '-' in last_anwser_expo:
                        print()
                        print(":Imaginary number detected!")
                        print()
                        return False

                    elif have_bracket == True and float(expo) % 2 == 0 and '-' in last_anwser_expo:
                        last_anwser_expo += '-'+str(format(pow(float(base),float(expo)),'.25f'))

                    else:
                        last_anwser_expo += str(format(pow(float(base),float(expo)),'.25f'))

                    last_anwser_expo += check_expo[1]
                    in_expo = False
                    expo,base = '',''

                elif (in_expo == True) and (check_expo[1].isdigit() == True or check_expo[1] == '.' or check_expo[1] in 'pe'):

                    if check_expo[1] == 'p':
                        expo += str(math.pi)

                    elif check_expo[1] == 'e':
                        expo += str(math.e)
                    else:
                        expo += check_expo[1]

                    if check_expo[0] == len(real_temp_str) - 1:

                        if have_bracket == True and float(expo) < 1 and '-' in last_anwser_expo:
                            print()
                            print(":Imaginary number detected!")
                            print()
                            return False

                        elif have_bracket == True and float(expo) % 2 == 0 and '-' in last_anwser_expo:
                            last_anwser_expo += '-'+str(format(pow(float(base),float(expo)),'.25f'))
                        else:
                            last_anwser_expo += str(format(pow(float(base),float(expo)),'.25f'))

                        in_expo = False
                        expo,base = '',''

                elif check_expo[1] == '^':
                    in_expo = True
                    base += temp_num_ex
                    temp_num_ex = ''

            after_simplify = simplify_negative(last_anwser_expo)

            if after_simplify == False:
                divide_by_zero = True
                break
            else:
                dict_equation_value.update({e1[1]:my_eval(after_simplify)})

        else:
            after_simplify = simplify_negative(real_temp_str)

            if after_simplify == False:
                divide_by_zero = True
                break
            else:
                dict_equation_value.update({e1[1]:my_eval(after_simplify)})

    if divide_by_zero == True:
        print()
        print(':Divide by zero detected!')
        print()
        return False
    
while 1:
    can_cal = False
    f1 = input("Calculate: ")

    for starting in enumerate(f1):
        if (starting[1] in '+-*/.') and ( f1[starting[0]+1] in '+-/*' and f1[starting[0]+1] not in "-") or (f1[-1] in '^+-*/('):
            can_cal = False
            break
        elif (starting[1] not in '+-*/.' and starting[1] not in 'pe()^' and starting[1].isdigit() != True) or (f1[0] in ')+*/.'):
            can_cal = False
            break
        elif '()' in f1 or 'ee' in f1 or 'pp' in f1 or 'pe' in f1 or 'ep' in f1:
            can_cal = False
            break

        else:
            if f1.count('(') == f1.count(')'):
                can_cal = True
            else:
                if f1.count('(') > f1.count(')'):
                    print()
                    print("-->  '(' was never closed  <--")
                    
                elif f1.count(')') > f1.count('('):
                    print()
                    print("-->  '(' was never opened  <--")

                can_cal = False
                break

    if can_cal == True:
        equation_1.append(f1[0:])
        after_split = find_bracket(f1)
        after_parenthesis = parenthesis(equation_1)

        if after_parenthesis != False:
            print()
            print("=",float(dict_equation_value[f1]))
            print()
        else:
            equation_1 = []
    else:
        print()
        print(":Can not calculate, try again!")
        print()
