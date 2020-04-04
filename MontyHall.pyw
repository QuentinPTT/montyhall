from random import *
import time
import pygame

# Déclaration des variables
nb_gagnant = 1
nb_perdu = 1

# Initialisation de la charte graphique (résolution, titre, couleur..)
pygame.init()
pygame.font.init()
res = (1170, 747)
icon_32x32 = pygame.image.load("test.png")
pygame.display.set_icon(icon_32x32)
pygame.display.set_caption("Simulation MontyHall - QuentinPTT")
screen = pygame.display.set_mode((res))
currentColor = (13,26,154)
currentColor2 = (18,49,235)
white = (255,255,255)
launched = True
changementPorte = True

#test
font = pygame.font.Font('ProductSans-Bold.ttf', (35))
titrefont = pygame.font.Font('ProductSans-Bold.ttf',55)
probatext = font.render('Probabilité :', 1,(255, 255, 255))
castext = font.render('Nombre de cas :', 1,(255, 255, 255))
victoiretext = font.render('Nombre de victoire :', 1,(255, 255, 255))
defaitetext = font.render('Nombre de défaite :', 1,(255, 255, 255))
titretext = titrefont.render('Simulation MontyHall :', 1,(255, 255, 255))


# Boucle infini
while launched:

    # Condition pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    # Assignation des valeurs aléatoires, le choix, et la solution
    choix = randint(1,3)
    solution = randint(1,3)

    # Si on veut changer de porte
    if changementPorte:
        if choix == 1:
            if solution == 1:
                choix = 2
            if solution == 2:
                choix = 2
            if solution == 3:
                choix = 3
        elif choix == 2:
            if solution == 1:
                choix = 1
            if solution == 2:
                choix = 1
            if solution == 3:
                choix = 3
        else:
            if solution == 1:
                choix = 1
            if solution == 2:
                choix = 2
            if solution == 3:
                choix = 1

    # Si on gagne, on incrémente de 1 le nombre de partie gagnées
    if choix == solution:
        nb_gagnant = nb_gagnant + 1

    # Si on gagne, on incrémente de 1 le nombre de partie perdues
    else:
        nb_perdu = nb_perdu + 1

    # On fait le calcul de probabilité
    nb_total= nb_gagnant + nb_perdu
    proba = nb_gagnant/(nb_perdu+nb_gagnant)

    # On affiche toutes les variables à l'écran, couleur de fond, police..
    screen.fill(currentColor)
    pygame.draw.rect(screen, white, (300,97,560,2), 0)
    pygame.draw.rect(screen, currentColor2, (0,0,1170,146), 0)
    screen.blit(probatext, (620,400))
    screen.blit(victoiretext, (150,250))
    screen.blit(defaitetext, (150,400))
    screen.blit(castext, (150,550))
    screen.blit(titretext, (300,38))
    probarender = font.render(str(proba), 1, (255, 255, 255))
    nb_perdurender = font.render(str(nb_perdu),1,(255, 255, 255))
    nb_gagnantrender = font.render(str(nb_gagnant),1,(255, 255, 255))
    nb_totalrender = font.render(str(nb_total), 1, (255, 255, 255))
    screen.blit(probarender, (620,436))
    screen.blit(nb_gagnantrender, (150,286))
    screen.blit(nb_perdurender, (150,436))
    screen.blit(nb_totalrender, (150,586))
    pygame.display.update()

