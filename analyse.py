def isolateur(liste,x,y):
    sujet=[0,0,0,0,0,0,0,0,0]
    for i in [-1,0,1]:
        for j in[-1,0,1]:
            try:
                sujet[i+4+j*3]=liste[x+i][y+j]
            except:
                pass
    return sujet


   #sujet=liste[x-1][slice(y-1,y+2)]+liste[x][slice(y,y+2)]+liste[x+1][slice(y,y+2)]
    return sujet

def traitement(liste):
    compteurcell=0
    for i in liste:
        try:
            compteurcell+=i
        except:
            pass
    etat=0
    if liste[4]==0 and compteurcell==3:
        etat=1
        
    elif liste[4]==1 and (compteurcell<3 or compteurcell>4):
        etat=-1

    return etat

def analyse(liste):
    liste2=[]
    for i in range (len(liste)):
        liste2.append([])
        for j in range (len (liste[i])):
            a=isolateur(liste,i,j)
            etat=traitement(a)
            liste2[i].append(liste[i][j]+etat)

    return liste2
            
from random import random
test=[]
for i in range(50):
    test.append([])
    for j in range(50):
        test[i].append(0)
        
