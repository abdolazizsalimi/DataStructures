def eval_expression(arr):
    tokenlist = arr.split()
    stack = []
    operator = ['+', '-', '*','/','%']
    
    for item in tokenlist:
        if item not in operator:
            stack.append(item)
        else:
            first = int(stack.pop())
            sec = int(stack.pop())
            
            if item == '+':
                stack.append(first + sec )
                
            elif item == '-':
                stack.append(first - sec )

                    
            elif item == '*':
                stack.append(first * sec )
                    
            elif item == '/':
                stack.append(first / sec )
                    
            elif item == '%':
                stack.append(first % sec )
                

    return stack[-1]
                
        
      
print(eval_expression('2 3 * 4 +'))        