import copy

with open("/home/jazzhoo/Dropbox/Code/AdventOfCode/Day2/Day2_input", "r") as f:
    for line in f.readlines():
        list1 = [int(x) for x in line.split(',')]
#deepcopy of the original list
listOld = copy.deepcopy(list1)    
#creating switch case
#def one(a,b,c):



def intcode(input_list):
    i=0
    #for i in range (0, len(input_list)):
    while i < len(input_list):
        if input_list[i]==1:
            input_list[input_list[i+3]]=input_list[input_list[i+1]] + input_list[input_list[i+2]]
            i+=4
        elif input_list[i]==2:
            input_list[input_list[i+3]]=input_list[input_list[i+1]] * input_list[input_list[i+2]]
            i+=4
        elif input_list[i]==99:
            break
        else:
            i+=1
    #for j in range (0, len(input_list)):
    #   print ("{0}:{1} --> {2}".format(j,listOld[j],input_list[j]))
    return input_list[0]    

print("Result: {0}".format(intcode(list1)))    

#TODO: Finish day 2 task