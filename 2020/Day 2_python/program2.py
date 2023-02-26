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
    occurance = password.count(letter)
    if(min <= occurance <= max):
        valid_ = True
        valid += 1
    else:
        valid_ = False
    print(min, max, letter, password, occurance, valid_, valid)

# print(decode)
    

#print(content)

