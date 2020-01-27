def isolateur(liste,x,y):
    sujet=liste[x-1][slice(y-1,y+2)]+liste[x][slice(y,y+2)]+liste[x+1][slice(y,y+2)]
    return sujet
