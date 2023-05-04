marks=[55,64,75,80,65]

def average():
    sum_of_marks=sum(marks)
    avg=sum_of_marks/len(marks)
    return avg

r=average()

if r>=80:
    print("Gread A")
elif 60<=r<80:
    print("Gread B")
elif 50<=r<60:
    print("Gread C")
else:
    print("Gread F")        
        

