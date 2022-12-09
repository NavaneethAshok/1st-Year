import collections


def endo():
    print("Upload complete ! Thank u")

j = []  # list of students
o = []  # list of term 1 marks of students later to uploaded into dictonary
u = []  # list of term 2
c = []  # total mark program for students and there marks to be uploaded into the list
Upload = str(input("Do you want to upload Marks [Yes or No]:"))
if Upload in ["Yes", "yes", "YES", "yEs", "yeS", "YEs", "yES", "YeS"]:
    n = int(input("Strength of the Class: "))
    for i in range(0, n):
        name = str(input("Name of Student: "))
        mark = float(input("Upload Term 1 Marks/50: "))
        mark2 = float(input("Upload Term 2 Marks/50: "))
        if (mark>50) or (mark2>50):
            print("Mark entered is greater than the total mark!")
            for i in range(0,1):
                name = str(input("Re enter Name of Student: "))
                mark = float(input("Upload Term 1 Marks/50: "))
                mark2 = float(input("Upload Term 2 Marks/50: "))
                if mark<=50 and mark2 <=50:
                    j.append(name)
                    o.append(mark)
                    u.append(mark2)
                    c.append(int(o[i] + u[i]))
                    break
        else:
            j.append(name)
            o.append(mark)
            u.append(mark2)
            c.append(int(o[i] + u[i]))
    # Search About a student

    ques = str(input("Do you want to search details of any student (Yes or No): "))

    dict1 = dict(zip(j, c))  # dict of name and marks
    dict2 = dict(zip(j, o))  # first marks
    dict3 = dict(zip(j, u))  # second marks
    dict4 = collections.OrderedDict(sorted(dict1.items(), key=lambda x: x[1]))
    dict5=dict4.__reversed__()

    if ques in ["Yes", "yes", "YES", "yEs", "yeS", "YEs", "yES", "YeS"]:
        getname = str(input("Name of the Student:"))
        if getname in j:
            index = list(dict5).index(getname)
            print("Details is as follow:")
            print("Total Mark obtained:  [", dict1.get(getname), "/100 in both terms combined !]")
            print(getname, "is Ranked",int(index)+1,"in class")
            print("Scored", dict2.get(getname), "marks in term 1 &")
            print("Scored", dict3.get(getname), "marks in term 2")
        else:
            print("No student Named", getname)
    elif ques in ["NO", "no", "No", "nO"]:
        print(endo())
    else:
        print("Entered value is not Yes or No : [Considered No] - Program Ended:")
elif Upload in ["NO", "no", "No", "nO"]:
    print("No Data Feeded ! Thank U ")
    print("Program Ended")
else:
    print("Input Wrong Re-run Program")