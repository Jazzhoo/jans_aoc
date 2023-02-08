filepath = "Input.txt"
content = []
decode =[]
valid = 0
with open(filepath) as f:
    content = f .readlines()


for i, line in enumerate(content):   
    # decode.append({"Min":line.split("-")[0], "Max": line.split("-")[1].split(" ")[0]})
    # decode[i]["letter"] = line.split(" ")[1][0]
    # decode[i]["password"]= line.split(" ")[2].strip("\n")
    min = int(line.split("-")[0])
    max = int(line.split("-")[1].split(" ")[0])
    letter = line.split(" ")[1][0]
    password = line.split(" ")[2].strip("\n")
    valid_1=False
    valid_2=False
    valid_3=False
    if(password[min-1]==letter):
        valid_1=True
    if(password[max-1]==letter):
        valid_2=True
    if valid_1 != valid_2:
        valid_3=True
        valid+=1

    print(min, max, letter, password, valid_1, valid_2, valid_3, valid)

# print(decode)
    

#print(content)

