import math

#Calculates the mean and convert to a grade of base 10 instead of base 100
def mean(n1,n2,n3):
    return ((n1+n2+n3)/3)/10

def absence(absences,classes):
    x = classes * 0.25
    if absences > x:
        return True
    else:
        return False

def finalExam(m):
    naf = 10 - m
    return naf


#Rounds up the first decimal place if the second is higher than 0.05
def round_half_up(n, decimals=1):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def situation(absences,n1,n2,n3,classes):
    m = round_half_up(mean(n1,n2,n3))
    print(m)
    if absence(absences,classes):
        return ["Reprovado por falta" , 0]
    else:
        if m < 5:
            return ["Reprovado por nota" , 0]
        elif m < 7:
            return ["Exame final" , finalExam(m)]
        else:
            return ["Aprovado" , 0]


