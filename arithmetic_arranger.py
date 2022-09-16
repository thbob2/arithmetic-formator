import re

def error_handler(operand1, operand2, operator):
    #? case 3  Each number (operand) should only contain digits.
    #? Otherwise, the #function will return: Error: Numbers must only contain digits.
    
    try:
        int(operand1)
        int(operand2)
    except:
        return 'Error: Numbers must only contain digits.'
    
    #? case 4
    #?Each operand has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    
    if len(operand1) > 4 or len(operand2) > 4 :
        return 'Error: Numbers cannot be more than four digits.'
    
    #* case 2 
    #? The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    
    if operator not in "+-":
        return "Error: Operator must be '+' or '-'."

    #!if not any of the previous cases return a checked
    
    return 'cleared'

def arithmetic_arranger(problems, calculate=False):
    lines = ["" for i in range(0,4)]
    side_jump = "    "
    first_prob = True
    
    #* case 1
    #* too many problems
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems: 
        operand1, operator, operand2 = problem.split()
       
        cleared = error_handler(operand1, operand2, operator)
        if cleared != "cleared" :
            return cleared
        
        space = max(len(operand2), len(operand1))
        
        if first_prob :
            lines[0] += operand1.rjust(space + 2)
            lines[1] += operator + ' ' + operand2.rjust(space)
            lines[2] += '-' * (space + 2)
            if calculate:
                if operator == "+":
                    lines[3] += str(int(operand1) + int(operand2)).rjust(space + 2)
                else:
                    lines[3] += str(int(operand1) - int(operand2)).rjust(space + 2)
            
            first_prob = False
        else:
            lines[0] += operand1.rjust(space + 6)
            lines[1] += operator.rjust(5) + ' ' + operand2.rjust(space)
            lines[2] += side_jump+ '-' * (space + 2)
            if calculate:
                if operator == "+":
                    lines[3] += side_jump + str(int(operand1) + int(operand2)).rjust(space + 2)
                else:
                    lines[3] += side_jump + str(int(operand1) - int(operand2)).rjust(space + 2)
            
    
    if calculate:
        return "\n".join(map(str,lines))
    else:
        return "\n".join(map(str,[lines[0],lines[1],lines[2]]))
        