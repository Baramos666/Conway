from tkinter import *
import os
import random
from time import sleep
from analyse import *

grid=[]



class conwayButton(Button):
    def __init__(self, parent,x,y ,*args, **kwargs):
        Button.__init__(self, parent, *args, **kwargs)
        self.x=x
        self.y=y
        
    def updateButton(self,x,y,liste):
        if liste[x*10+y]=='0':
            liste[x*10+y]='1'
        else :
            liste[x*10+y]='0'
        grid=liste

    def command():
        Button.command()

def randomgrid(filename):#génère 100 booléens aléatoires et l'inscrit sur un fichier
    f=open(filename,"w+")
    for i in range(100):
        f.write(str(round(random.random())))

def inverser(x,y,liste,fenetre):#transforme les 1 en 0 vice versa todo
    if liste[x*10+y]=="1":
        liste[x*10+y]="0"
    else :
        liste[x*10+y]="1"
    gridcreation(liste,fenetre)

def simulation(liste, frame):
    liste2=[]
    for i in range(len(liste)//10):
        liste2.append([])
        for j in range (10):
            liste2[i].append(liste[i][j])
    liste3=analyse(liste2)
    print (list3)
    print("simulation faite " )
    gridcreation(liste3,frame)



def conway(filename):#fonction qui lance le jeu
    fenetrejeu= Tk()
    frame_menu=Frame(fenetrejeu,width=50, height=900,borderwidth=2)
    frame_jeu=Frame(fenetrejeu,width=300, height=300,borderwidth=3)
    frame_menu.pack()
    frame_jeu.pack()
    Button(frame_menu, text = "options").pack()
    f=open(filename)
    a=list(f.read())
    Button(frame_menu, text="simulation", command=lambda : simulation(a,frame_jeu)).pack()
    gridcreation(a,frame_jeu)
#    x=0
 #   y=0
  #  for name in NOM_BOUTONS:
        
   #     dictionnaireNoms[name]=conwayButton(frame_jeu,x,y,text=a[x*10+y])
    #    dictionnaireNoms[name].grid(row=x,column=y)
        
     #   dictionnaireNoms[name]['command']=lambda:dictionnaireNoms[name].updateButton(x,y,a)
      #  if x==9:
       #     x=0
        #    y=y+1
        #else :
         #   x=x+1


        

    fenetrejeu.mainloop()

def gridcreation(liste,frame,reset=1):#crée une grille 10x10 à partir d'une liste # bug impossible de créer des objets différents
    if reset==1:
        for widget in frame.winfo_children():
            widget.destroy()
    for i in range (10):
        for j in range (10):
            b=[i,j]
            a=locals()["conway_button_"+str(i)+str(j)]=conwayButton(frame,x=i,y=j,text=liste[i*10+j])
            a['command']=lambda b=b: a.updateButton(b[0],b[1],liste)
            a.grid(row=i,column=j)
            #print(i,j)
            
    frame.update()    

conway("a.txt")
