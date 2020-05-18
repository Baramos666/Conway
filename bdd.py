from tkinter import *
import os

def destruction2():
  fenetre3.destroy()

def destruction3():
  fenetre4.destroy()

def destruction4():
  fenetre5.destroy()
  
def connexion_effectue():
  global fenetre3
  fenetre3 = Toplevel(fenetre)
  fenetre3.geometry("150x100")
  Label(fenetre3, text = "connexion effectué").pack()
  Button(fenetre3, text = "OK", command =destruction2).pack()

def motdepasse_non_reconnu():
  global fenetre4
  fenetre4 = Toplevel(fenetre)
  fenetre4.geometry("150x100")
  Label(fenetre4, text = "Mauvais mot de passe").pack()
  Button(fenetre4, text = "OK", command =destruction3).pack()

def utilisateur_non_trouver():
  global fenetre5
  fenetre5 = Toplevel(fenetre)
  fenetre5.geometry("300x100")
  Label(fenetre5, text = "Utilisateur non trouvé, veuillez vous enregistrer !").pack()
  Button(fenetre5, text = "OK", command =destruction4).pack()

#Enregistrement dans un fichier du motdepasse et de l'utilisateur
  
def enregistrement_utilisateur():
  
  utilisateur_info = utilisateur.get()
  motdepasse_info = motdepasse.get()
  file=open(utilisateur_info, "w")
  file.write(utilisateur_info+"\n")
  file.write(motdepasse_info)
  file.close()
  utilisateur_entre.delete(0, END)
  motdepasse_entre.delete(0, END)
  Label(fenetre1, text = "Enregistrement effectué", fg = "green" ,font = ("calibri", 11)).pack()

#Vérification de la connexion

def connexion_verification():
  
  utilisateur1 = utilisateur_verification.get()
  motdepasse1 = motdepasse_verification.get()
  utilisateur_entre1.delete(0, END)
  motdepasse_entre1.delete(0, END)
  
  list_of_files = os.listdir()
  if utilisateur1 in list_of_files:
    file1 = open(utilisateur1, "r")
    verification = file1.read().splitlines()
    if motdepasse1 in verification:
        connexion_effectue()
    else:
        motdepasse_non_reconnu()

  else:
        utilisateur_non_trouver()
  
#Page d'enregistrement

def enregistrement():
  global fenetre1
  fenetre1 = Toplevel(fenetre)
  fenetre1.title("Enregistrement")
  fenetre1.geometry("300x250")
  global utilisateur
  global motdepasse
  global utilisateur_entre
  global motdepasse_entre
  utilisateur = StringVar()
  motdepasse = StringVar()
  Label(fenetre1, text = "Entrer vos identifiant et mot de passe").pack()
  Label(fenetre1, text = "").pack()
  Label(fenetre1, text = "Identifiant ").pack()
  utilisateur_entre = Entry(fenetre1, textvariable = utilisateur)
  utilisateur_entre.pack()
  Label(fenetre1, text = "Mot de Passe ").pack()
  motdepasse_entre =  Entry(fenetre1, textvariable = motdepasse)
  motdepasse_entre.pack()
  Label(fenetre1, text = "").pack()
  Button(fenetre1, text = "Enregistrement", width = 15, height = 1, command = enregistrement_utilisateur).pack()

# Page de connexion

def connexion():
  global fenetre2
  fenetre2 = Toplevel(fenetre)
  fenetre2.title("Connexion")
  fenetre2.geometry("300x250")
  Label(fenetre2, text = "Entrer vos identifiant et mot de passe").pack()
  Label(fenetre2, text = "").pack()
  global utilisateur_verification
  global motdepasse_verification
  utilisateur_verification = StringVar()
  motdepasse_verification = StringVar()
  global utilisateur_entre1
  global motdepasse_entre1
  Label(fenetre2, text = "Identifiant ").pack()
  utilisateur_entre1 = Entry(fenetre2, textvariable = utilisateur_verification)
  utilisateur_entre1.pack()
  Label(fenetre2, text = "").pack()
  Label(fenetre2, text = "Mot de passe ").pack()
  motdepasse_entre1 = Entry(fenetre2, textvariable =  motdepasse_verification)
  motdepasse_entre1.pack()
  Label(fenetre2, text = "").pack()
  Button(fenetre2, text = "Connexion", width = 10, height = 1, command = connexion_verification).pack()
  
# Première fenetre
  
def premiere_fenetre():
  global fenetre
  fenetre = Tk()
  fenetre.geometry("300x250")
  fenetre.title("Jeux de la vie")
  Label(text = "Jeux de la vie", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Connexion", height = "2", width = "30", command = connexion).pack()
  Label(text = "").pack()
  Button(text = "Enregistrement",height = "2", width = "30", command = enregistrement).pack()
  fenetre.mainloop()

premiere_fenetre()

  