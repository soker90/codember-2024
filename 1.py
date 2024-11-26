input = list("528934712834")
command="URDURUDRUDLLLLUUDDUDUDUDLLRRRR"
position=0

for i in command:
    if i=='U':
        if input[position]!="9":

            input[position] = str(int(input[position]) + 1)
        else:
            input[position] = "0"
    elif i=='D':
        if input[position]!="0":
            input[position] = str(int(input[position]) - 1)
        else:
            input[position] = "9"
    elif i=='R':
        if(position!=len(input)-1):
            position+=1
        else:
            position=0
    elif i=='L':
        if(position!=0):
            position-=1
        else:
            position=len(input)-1

print("".join(input))