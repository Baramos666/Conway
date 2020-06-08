from tkinter import *
import os
import random
from time import sleep
from analyse import *





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

        print("updated",x,y,id(self))

    def command():
        Button.command()

NOM_BOUTONS =(
    "x00","x10","x20","x30","x40","x50","x60","x70","x80","x90",
    "x01","x11","x21","x31","x41","x51","x61","x71","x81","x91",
    "x02","x12","x22","x32","x42","x52","x62","x72","x82","x92",
    "x03","x13","x23","x33","x43","x53","x63","x73","x83","x93",
    "x04","x14","x24","x34","x44","x54","x64","x74","x84","x94",
    "x05","x15","x25","x35","x45","x55","x65","x75","x85","x95",
    "x06","x16","x26","x36","x46","x56","x66","x76","x86","x96",
    "x07","x17","x27","x37","x47","x57","x67","x77","x87","x97",
    "x08","x18","x28","x38","x48","x58","x68","x78","x88","x98",
    "x09","x19","x29","x39","x49","x59","x69","x79","x89","x99")
dictionnaireNoms={}



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
            locals()["conway_button_"+str(i)+str(j)]=conwayButton(frame,x=i,y=j,text=liste[i*10+j])
            locals()["conway_button_"+str(i)+str(j)]['command']=lambda : print("TODO")
            locals()["conway_button_"+str(i)+str(j)].grid(row=i,column=j)
            #print(i,j)
            
    frame.update()    

conway("a.txt")
