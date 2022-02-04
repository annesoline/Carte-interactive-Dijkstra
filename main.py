from tkinter import*
from tkinter.messagebox import *
import webbrowser
import time

fenetre = Tk()
fenetre.title ("SSB")
fenetre.attributes("-fullscreen", True)
fenetre.configure(background = 'midnight blue')

#initialisation
point=0
depart=""
arrive=""

#####JULIE#####

msg = Label(fenetre, text="Etes-vous prêts à embarquer ?")
msg.config(font=('arial', 20, 'bold'))
msg.config(bg='Slateblue4', fg='white')
msg.config(height=4, width=200)
msg.pack()

varrivee = StringVar()
varrivee.set("Sélectionnez une planète d'arrivée")

msgb = Label(fenetre, textvariable = varrivee)
msgb.config(font=('arial', 14, 'bold'))
msgb.config(bg='Slateblue4', fg='white')
msgb.config(height=2, width=200)
msgb.pack(side = BOTTOM)

vdepart = StringVar()
vdepart.set("Sélectionnez une planète de départ")

msga = Label(fenetre, textvariable = vdepart)
msga.config(font=('arial', 14, 'bold'))
msga.config(bg='Slateblue4', fg='white')
msga.config(height=2, width=200)
msga.pack(side = BOTTOM)

vduree = StringVar()
vduree.set("Durée du parcours...")

rurus = Label(fenetre, textvariable = vduree)
rurus.config(font=('arial', 14, 'bold'))
rurus.config(bg='Slateblue4', fg='white')
rurus.config(height=2, width=200)
rurus.pack(side = BOTTOM)

canvas = Canvas(fenetre, width=800, height=560, background='midnight blue')

def parc () :
    global depart, arrive, point
    if depart != '' and arrive != '':
        parcours(graph, depart, arrive)
        depart = ""
        arrive = ""

def dessineDisqueRose (event) :
    global depart, arrive, point
    if (110<event.x<170) and (230<event.y<290) :
        if point==0 :
            depart="Riwai"
            point = 1
            canvas.itemconfigure(Riwai, fill='yellow')
            vdepart.set("Planète de départ : Riwai")
        elif point==1:
            arrive="Riwai"
            varrivee.set("Planète d'arrivée : Riwai")

    if (20<event.x<80) and (20<event.y<80) :
        if point==0 :
            depart="Cucurbita"
            point = 1
            canvas.itemconfigure(Cucurbita, fill='yellow')
            vdepart.set("Planète de départ : Cucurbita")
        elif point==1:
            arrive="Cucurbita"
            varrivee.set("Planète d'arrivée : Cucurbita")

    if (20<event.x<80) and (500<event.y<560) :
        if point==0 :
            depart="Kalabazin"
            point = 1
            canvas.itemconfigure(Kalabazin, fill='yellow')
            vdepart.set("Planète de départ : Kalabazin")
        elif point==1:
            arrive="Kalabazin"
            varrivee.set("Planète d'arrivée : Kalabazin")

    if (190<event.x<250) and (110<event.y<170) :
        if point==0 :
            depart="Riolé"
            point = 1
            canvas.itemconfigure(Riolé, fill='yellow')
            vdepart.set("Planète de départ : Riolé")
        elif point==1:
            arrive="Riolé"
            varrivee.set("Planète d'arrivée : Riolé")

    if (260<event.x<320) and (210<event.y<270) :
        if point==0 :
            depart="Cauliflower"
            point = 1
            canvas.itemconfigure(Cauliflower, fill='yellow')
            vdepart.set("Planète de départ : Cauliflower")
        elif point==1:
            arrive="Cauliflower"
            varrivee.set("Planète d'arrivée : Cauliflower")

    if (150<event.x<210) and (330<event.y<390) :
        if point==0 :
            depart="Kyuuri"
            point = 1
            canvas.itemconfigure(Kyuuri, fill='yellow')
            vdepart.set("Planète de départ : Kyuuri")
        elif point==1:
            arrive="Kyuuri"
            varrivee.set("Planète d'arrivée : Kyuuri")

    if (230<event.x<290) and (420<event.y<480) :
        if point==0 :
            depart="Riiki"
            point = 1
            canvas.itemconfigure(Riiki, fill='yellow')
            vdepart.set("Planète de départ : Riiki")
        elif point==1:
            arrive="Riiki"
            varrivee.set("Planète d'arrivée : Riiki")

    if (350<event.x<410) and (423<event.y<483) :
        if point==0 :
            depart="Eskarola"
            point = 1
            canvas.itemconfigure(Eskarola, fill='yellow')
            vdepart.set("Planète de départ : Eskarola")
        elif point==1:
            arrive="Eskarola"
            varrivee.set("Planète d'arrivée : Eskarola")

    if (470<event.x<530) and (375<event.y<435) :
        if point==0 :
            depart="Pomidor"
            point = 1
            canvas.itemconfigure(Pomidor, fill='yellow')
            vdepart.set("Planète de départ : Pomidor")
        elif point==1:
            arrive="Pomidor"
            varrivee.set("Planète d'arrivée : Pomidor")

    if (580<event.x<640) and (480<event.y<540) :
        if point==0 :
            depart="Masticari"
            point = 1
            canvas.itemconfigure(Masticari, fill='yellow')
            vdepart.set("Planète de départ : Masticari")
        elif point==1:
            arrive="Masticari"
            varrivee.set("Planète d'arrivée : Masticari")

    if (670<event.x<730) and (370<event.y<430) :
        if point==0 :
            depart="Arbip"
            point = 1
            canvas.itemconfigure(Arbip, fill='yellow')
            vdepart.set("Planète de départ : Arbip")
        elif point==1:
            arrive="Arbip"
            varrivee.set("Planète d'arrivée : Arbip")

    if (590<event.x<650) and (190<event.y<250) :
        if point==0 :
            depart="Ninjin"
            point = 1
            canvas.itemconfigure(Ninjin, fill='yellow')
            vdepart.set("Planète de départ : Ninjin")
        elif point==1:
            arrive="Ninjin"
            varrivee.set("Planète d'arrivée : Ninjin")

    if (700<event.x<760) and (20<event.y<80) :
        if point==0 :
            depart="Radisshu"
            point = 1
            canvas.itemconfigure(Radisshu, fill='yellow')
            vdepart.set("Planète de départ : Radisshu")
        elif point==1:
            arrive="Radisshu"
            varrivee.set("Planète d'arrivée : Radisshu")

#print('valeur de depart : ' + depart + ' et arrivee ' + arrive)

parc()

#####FIN JULIE#####




#####ANNE-SOLINE#####

####################DICTIONNAIRE####################

graph = {'Kyuuri':{'Riolé':13, 'Eskarola':8},

        'Ninjin':{'Radisshu':4, 'Arbip':5, 'Pomidor':7, 'Cauliflower':8},

        'Riiki':{'Eskarola':4},

        'Cauliflower':{'Riolé':3, 'Riwai':5, 'Ninjin':8, 'Pomidor':7},

        'Pomidor':{'Riwai':11, 'Masticari':5},

        'Riwai':{'Pomidor':11, 'Cauliflower':5, 'Riolé':6},

        'Kalabazin':{'Eskarola':15, 'Cucurbita':17},

        'Cucurbita':{'Kalabazin':17},

        'Eskarola':{'Kyuuri':8, 'Riiki':7, 'Kalabazin':15},

        'Radisshu':{'Ninjin':4},

        'Riolé':{'Kyuuri':13, 'Riwai':6, 'Cauliflower':3},

        'Masticari':{'Pomidor':5, 'Arbip':3},

        'Arbip':{'Masticari':3, 'Ninjin':5}    
    }



####################ALGORITHME####################
def Dijkstra(graph, start):
    infinity = 10000000000000000000000

    dist = {} #dictionnaire vide
    dist[start] = 0

    IC = [] #liste vide
    C = []
    C.append(start)

    previous = {}

    for u in (graph):   #pour tous les u
        if u != start :
            IC.append(u)
    for u in (IC):
        dist[u] = infinity
        previous[u] = None
  
    for u in graph[start]: #tous les successeurs de start
        dist[u] = graph[start][u] #distance entre start et u
        previous[u] = start


    while len(IC) != 0 : # nb éléments d'une chaîne de carac ou d'une liste
        u = IC[0]        #premier inconnu qu'on met dans u
        for n in (IC):        #n est un element inconnu
            if dist[n] < dist[u] :
                u = n    

        for v in graph[u]:         #successeurs de u
            if v in (IC):
                if dist[u] + graph[u][v] < dist[v] :
                    dist[v] = dist[u] + graph[u][v]        #graphuv est poids entre u et v
                    previous[v] = u

        C.append(u)
        IC.remove(u)

    #stocker resultat variable :
    return {'dist':dist, 'previous': previous }


def parcours(graph, start, end):
    result = Dijkstra(graph, start)
    global dur
    dur=str(result['dist'][end]) + ' rurus'
    print('durée du parcours : ' + dur)
    vduree.set("Durée du parcours : "+ dur)
    current = end
    parcours = ''

    while current != start:
        parcours = current + ' -> ' + parcours
        current = result['previous'][current]
    parcours = start + ' -> ' + parcours
    print (parcours)

    liste1 = parcours.split(' -> ')
    #print('liste trouvée : ' + '<' + str(liste1) + '>')


#####FIN ANNE-SOLINE#####





#####JULIE#####
for planete in liste1:# planete est la variable d'itération
    print(planete)
    pl=str(planete) + 'Etiq'
    #print(str(pl))
    canvas.itemconfigure(pl, fill='red')

print("Fin de la boucle")



####################RETOUR DE LA CARTE#########################

lignea = canvas.create_line(220,140,290,240,fill="white",width=3)
ligneb = canvas.create_line(140,260,220,140,fill="white",width=3)
lignec = canvas.create_line(140,260,290,240,fill="white",width=3)
ligned = canvas.create_line(500,405,290,240,fill="white",width=3)
lignee = canvas.create_line(620,220,290,240,fill="white",width=3)
lignef = canvas.create_line(620,220,730,50,fill="white",width=3)
ligneg = canvas.create_line(620,220,500,405,fill="white",width=3)
ligneh = canvas.create_line(620,220,700,400,fill="white",width=3)
lignei = canvas.create_line(700,400,610,510,fill="white",width=3)
lignej = canvas.create_line(610,510,500,405,fill="white",width=3)
lignek = canvas.create_line(500,405,140,260,fill="white",width=3)
lignel = canvas.create_line(50,50,50,530,fill="white",width=3)
lignem = canvas.create_line(260,450,380,455,fill="white",width=3)
lignen = canvas.create_line(380,455,180,360,fill="white",width=3)
ligneo = canvas.create_line(180,360,220,140,fill="white",width=3)
lignep = canvas.create_line(50,530,380,455,fill="white",width=3)

Riwai = canvas.create_oval(110,230,170,290,fill='plum')
txt = canvas.create_text(140, 260, text="Riwai", font="Arial 13 ", fill="black")
canvas.addtag_withtag('RiwaiEtiq', Riwai)

Cucurbita = canvas.create_oval(20,20,80,80,fill='plum')
txt = canvas.create_text(50, 50, text="Cucurbita", font="Arial 10 ", fill="black")
canvas.addtag_withtag('CucurbitaEtiq', Cucurbita)

Kalabazin = canvas.create_oval(20,500,80,560,fill='plum')
txt = canvas.create_text(50, 530, text="Kalabazin", font="Arial 10 ", fill="black")
canvas.addtag_withtag('KalabazinEtiq', Kalabazin)

Riolé = canvas.create_oval(190,110,250,170,fill='plum')
txt = canvas.create_text(220, 140, text="Riolé", font="Arial 13 ", fill="black")
canvas.addtag_withtag('RioléEtiq', Riolé)

Cauliflower = canvas.create_oval(260,210,320,270,fill='plum')
txt = canvas.create_text(290, 240, text="Cauliflower", font="Arial 10 ", fill="black")
canvas.addtag_withtag('CauliflowerEtiq', Cauliflower)

Kyuuri = canvas.create_oval(150,330,210,390,fill='plum')
txt = canvas.create_text(180, 360, text="Kyuuri", font="Arial 13 ", fill="black")
canvas.addtag_withtag('KyuuriEtiq', Kyuuri)

Riiki = canvas.create_oval(230,420,290,480,fill='plum')
txt = canvas.create_text(260, 450, text="Riiki", font="Arial 13 ", fill="black")
canvas.addtag_withtag('RiikiEtiq', Riiki)

Eskarola = canvas.create_oval(350,423,410,483,fill='plum')
txt = canvas.create_text(380, 455, text="Eskarola", font="Arial 11 ", fill="black")
canvas.addtag_withtag('EskarolaEtiq', Eskarola)

Pomidor = canvas.create_oval(470,375,530,435,fill='plum')
txt = canvas.create_text(500, 405, text="Pomidor", font="Arial 11 ", fill="black")
canvas.addtag_withtag('PomidorEtiq', Pomidor)

Masticari = canvas.create_oval(580,480,640,540,fill='plum')
txt = canvas.create_text(610, 510, text="Masticari", font="Arial 10 ", fill="black")
canvas.addtag_withtag('MasticariEtiq', Masticari)

Arbip = canvas.create_oval(670,370,730,430,fill='plum')
txt = canvas.create_text(700, 400, text="Arbip", font="Arial 13 ", fill="black")
canvas.addtag_withtag('ArbipEtiq', Arbip)

Ninjin = canvas.create_oval(590,190,650,250,fill='plum')
txt = canvas.create_text(620, 220, text="Ninjin", font="Arial 13 ", fill="black")
canvas.addtag_withtag('NinjinEtiq', Ninjin)

Radisshu = canvas.create_oval(700,20,760,80,fill='plum')
txt = canvas.create_text(730, 50, text="Radisshu", font="Arial 10 ", fill="black")
canvas.addtag_withtag('RadisshuEtiq', Radisshu)



canvas.pack(pady=50)

canvas.bind_all('<Button-1>',dessineDisqueRose)



# stringvar Mémorise une chaîne de caractères; sa valeur par défaut est ''


def callback():
    if askyesno('SSB', 'Êtes-vous sûr de vouloir quitter ?'):
        fenetre.destroy()


b_quitter = Button(fenetre,text="Quitter", font="Arial 13", borderwidth=3, relief=GROOVE,
width=20, height = 3, command= callback, background = 'midnight blue', foreground='white')

b_quitter.pack(side=RIGHT, pady=10, padx=10)


#####BOUTON RESET######

def startover():
    global depart, arrive, point, dur
    if askyesno ('SSB', 'Êtes-vous sûr de vouloir recommencer ?'):
        canvas.itemconfigure(Riwai, fill='plum')
        canvas.itemconfigure(Kyuuri, fill='plum')
        canvas.itemconfigure(Eskarola, fill='plum')
        canvas.itemconfigure(Ninjin, fill='plum')
        canvas.itemconfigure(Radisshu, fill='plum')
        canvas.itemconfigure(Arbip, fill='plum')
        canvas.itemconfigure(Pomidor, fill='plum')
        canvas.itemconfigure(Cauliflower, fill='plum')
        canvas.itemconfigure(Riolé, fill='plum')
        canvas.itemconfigure(Masticari, fill='plum')
        canvas.itemconfigure(Kalabazin, fill='plum')
        canvas.itemconfigure(Cucurbita, fill='plum')
        canvas.itemconfigure(Riiki, fill='plum')

        point=0
        depart = ""
        arrive = ""

        vdepart.set("Sélectionner une planète de départ")
        varrivee.set("Sélectionner une planète d'arrivée")
        vduree.set("Durée du parcours...")


b_reset = Button (fenetre, text = "Recommencer", font="Arial 13", borderwidth=3,
relief=GROOVE, width=20, height = 3, command=startover, background = 'midnight blue',
foreground = 'white')

b_reset.pack(side=LEFT, pady=10, padx=10)


fenetre.mainloop()


#####FIN JULIE#####
