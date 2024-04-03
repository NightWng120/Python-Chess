
loop = True
string1 = "      a1      ,         a4      "
length1 = len(string1)

string2 =  "      a1                a4      "
length2 = len(string2)

string1 = string1.split(",")

if len(string1) < length1 and len(string1) > 1:
    for i, val in enumerate(string1):
        string1[i] = val.strip()

print(string1)

string2 = string2.split(",")

if len(string2) < length2 and len(string2) > 1:
    for i, val in enumerate(string1):
        string1[i] = val.strip()

elif len(string2) == 1:
    string2 = string2[0].split(" ")
    
    while loop:
        try:
            string2.remove('')
        except ValueError:
            loop = False

print(string2)
