def mean(n1,n2,n3):
    return ((n1+n2+n3)/3)/10

def absence(absences,classes):
    x = classes * 0.25
    if absences > x:
        return True
    else:
        return False

def situation(absences,n1,n2,n3,classes):
    m = mean(n1,n2,n3)
    if absence(absences,classes):
        return "Reprovado por falta"
    else:
        if m < 5:
            return "Reprovado por nota"
        elif m < 7:
            return "Exame final"
        else:
            return "Aprovado"


