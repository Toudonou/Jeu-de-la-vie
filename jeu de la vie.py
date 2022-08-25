import pygame
import time
pygame.init()

generation = 0
nombre = 0
cote = 50
l_color = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
cellule_morte = white
font_color = (0, 0, 255)
vitesse = 0.001
taille = (1366, 720)

pygame.display.set_caption("JEU DE LA VIE")
fenetre = pygame.display.set_mode(taille)

liste_etat = []
liste_cellule = []
liste_index = []
liste_non_exclu = []
liste_exclu = []
font = pygame.font.SysFont("robotoslab", 30)


def cellule_creation():
    for j in range(fenetre.get_height() // cote):
        for i in range(fenetre.get_width() // cote):
            liste_cellule.append(pygame.Rect(cote * i, cote * j, cote, cote))
    for i in liste_cellule:
        pygame.draw.rect(fenetre, white, i)
    print(len(liste_cellule))
def index_creation():
    h = 0
    for j in range(fenetre.get_height() // cote):
        for i in range(fenetre.get_width() // cote):
            liste_etat.append(0) 
            liste_index.append(h)
            h += 1

def play():
    global liste_non_exclu
    global nombre
    global liste_exclu
    mourrir = []
    vivre = []
    nombre = fenetre.get_width() // cote 

    for i in liste_index:
        if i%nombre == 0: 
            liste_exclu.append(i)
            liste_exclu.append(i + nombre - 1)
        if i < nombre: liste_exclu.append(i)
        if i >= len(liste_index) - nombre -1 and i <= len(liste_index) - 1: liste_exclu.append(i)
     
    liste_non_exclu = list(set(liste_index) - set(liste_exclu))
    
    
    for j in liste_non_exclu:
        compteur = 0
        if liste_etat[j - nombre] == 1: compteur += 1
        if liste_etat[j - nombre - 1] == 1: compteur += 1
        if liste_etat[j - nombre + 1] == 1: compteur += 1
        if liste_etat[j + nombre] == 1: compteur += 1
        if liste_etat[j + nombre - 1] == 1: compteur += 1
        if liste_etat[j + nombre + 1] == 1: compteur += 1
        if liste_etat[j - 1] == 1: compteur += 1
        if liste_etat[j + 1] == 1: compteur += 1

        if liste_etat[j] == 1:
            if compteur == 2 or compteur == 3:
                vivre.append(j)
            else:
                mourrir.append(j)
        if liste_etat[j] == 0:
            if compteur == 3:
                vivre.append(j)
            else:
                mourrir.append(j)
    for k in vivre:
        liste_etat[k] = 1

    for s in mourrir:
        liste_etat[s] = 0


def quadrillage():
    global liste_exclu
    l_x = 0
    l_y = 0
    a, b = 10, 23
    while l_x <= fenetre.get_width():
        pygame.draw.line(fenetre, l_color, (l_x, 0), (l_x, fenetre.get_height()))
        l_x += cote
    while l_y <= fenetre.get_height():
        pygame.draw.line(fenetre, l_color, (0, l_y), (fenetre.get_width(), l_y))
        l_y += cote
    for i in liste_exclu:
        pygame.draw.rect(fenetre, black, liste_cellule[i])

index_creation(); cellule_creation()

play()
boucle = True
jouer = False

while boucle:
    if jouer:
        play()
        generation += 1 
        time.sleep(vitesse)
    else:
        quadrillage()
    generation_text = font.render(str("Génération(s) : "+str(generation)), True, font_color)
    fenetre.blit(generation_text, [20, 10])
    pygame.display.flip()
    for j in range(len(liste_cellule)):
        if liste_etat[j] == 1:
            pygame.draw.rect(fenetre, green, liste_cellule[j])
        if liste_etat[j] == 0:
            pygame.draw.rect(fenetre, cellule_morte, liste_cellule[j]) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            for j in range(len(liste_cellule)):
                i = liste_cellule[j]    
                if not jouer:
                    if event.pos[0] > i.x  and event.pos[0] < i.x + cote and event.pos[1] > i.y and event.pos[1] < i.y + cote:
                        liste_etat[j] = (liste_etat[j] + 1)%2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jouer: jouer = False
                else: jouer = True
    
                        

pygame.quit()

