def traitement(liste):
    compteurcell=0
    for i in liste:
        print(compteurcell,i)
        try:
            compteurcell+=i
        except:
            pass
    if liste[4]==0:
        if compteurcell==3:
            etat=1
    else:
        if compteurcell<3 or compteurcell>4:
            etat=-1
        else :
            etat=0
    return etat
