def generate_order(arry):
    if len(arry) == 1:
        return [str(arry[0])]

    temp1 = [str(arry[0])+i for i in generate_order(arry[1:])]
    temp2 = [str(arry[-1])+i for i in generate_order(arry[:-1])]
    
    return [*temp1 , *temp2]



print(generate_order(range(int(input('enter your n number :')))))