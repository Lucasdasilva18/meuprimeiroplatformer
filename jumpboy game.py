import pygame , constantes , random
from pygame.locals import *

pygame.init()
pygame.font.init()
alturadatela = 700
larguradatela = 1200
tela = pygame.display.set_mode((larguradatela, alturadatela))
framerate = pygame.time.Clock()
fontepadrao = pygame.font.SysFont('arial black',40,True,False)
titulo='JUMPMAN ADVENTURES'
nomedojogo = fontepadrao.render(titulo,True,(255,255,50))
comojogar = 'aperte enter para jogar!'
jogar=fontepadrao.render(comojogar,True,(100,100,255))
class fasesdojogo():
    def __init__(self):
        self.menu = True
        map1grass = []
        modelodomapa=[
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
             1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
             1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2,
             2, 2, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
             1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2,
             2, 2, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1,
             1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 1, 1, 1]]
        map1coins = []
        a = 0
        b = -240

        for list in modelodomapa:
            for tile in list:
                if a>=3200:
                   a=0
                   b+=40
                if tile == 0:
                   a+=40
                if tile == 1:
                   map1grass.append([a,b])
                   a+=40
                if tile == 2:
                   map1coins.append([a,b])
                   a+=40


        o =80
        p =400
        for value in range(10):
            n=[o,p]
            if value < 10:
               o += 40
            map1coins.append(n)
        z=800
        x=280

        for value in range(20):
            line = [z, x]
            if value < 10:
                z += 40
            if value ==10:
                x+=40
                z=800
            if value<20 and value>10:
                z+=40
            map1coins.append(line)
        map1soil = []
        l=0
        g=0

        for s in range(1,201):
            v = [0+40*g,560-l]
            if s <= 80:
               g+=1
            if s > 80 and s <= 100:
               l+=40
            if s > 100 and s <=180:
               g-=1
            if s > 180 and s <=200:
               l-=40
            map1soil.append(v)
        peso = 2
        pulo = 0
        x = 550
        y = 250
        parado1 = constantes.spriteparado1
        parado2 = constantes.spriteparado2
        parado3 = constantes.spriteparado3
        frente1 = constantes.spriterun1
        frente2 = constantes.spriterun2
        frente3 = constantes.spriterun3
        frente4 = constantes.spriterun4
        costas1 = constantes.spriterun1esquerda
        costas2 = constantes.spriterun2esquerda
        costas3 = constantes.spriterun3esquerda
        costas4 = constantes.spriterun4esquerda
        pulo1 = constantes.pulofrente1
        pulo2 = constantes.pulofrente2
        pulo3 = constantes.pulofrente3
        pulo1tras = constantes.pulotras1
        pulo2tras = constantes.pulotras2
        pulo3tras = constantes.pulotras3
        parado1costas = constantes.spriteparado1esquerda
        parado2costas = constantes.spriteparado2esquerda
        parado3costas = constantes.spriteparado3esquerda

        pygame.mixer.music.load('sons/musica de fundo.ogg')
        som_de_moeda=pygame.mixer.Sound('sons/coin sound.ogg')
        pygame.mixer.music.play(-1)

        direção=parado1
        respiraçãoprafrente=False
        respiraçãopratras=False
        movrespfrente=0
        andandoprafrente = 0
        andandopratras = 0
        direita=True
        esquerda=False
        velocidadedireita=0
        velocidadeesquerda=0
        alturadopulo=70
        xnuvem1=-100
        ynuvem1=random.randint(0,350)
        xnuvem2 = 300
        ynuvem2 = random.randint(0, 350)
        xnuvem3 = 500
        ynuvem3 = random.randint(0, 350)
        xnuvem4 = -200
        ynuvem4 = random.randint(0, 350)
        xnuvem5 = -300
        ynuvem5 = random.randint(0, 350)
        xsol= 800
        ysol=100
        xcenário1=0
        ycenário1=400
        while self.menu:

           tela.fill((147, 222, 255))
           tela.blit(constantes.cenário1,(xcenário1,ycenário1))
           tela.blit(constantes.sol,(xsol,ysol))
           contatodecima = False
           contatodebaixo = False
           tela.blit(constantes.nuvem1, (xnuvem1, ynuvem1))
           xnuvem1 += 0.5
           if xnuvem1 > 1300:
               xnuvem1 = -100
               ynuvem1 = random.randint(0, 350)
           tela.blit(constantes.nuvem2, (xnuvem2, ynuvem2))
           xnuvem2 += 0.5
           if xnuvem2 > 1300:
               xnuvem2 = -100
               ynuvem2 = random.randint(0, 350)
           tela.blit(constantes.nuvem3, (xnuvem3, ynuvem3))
           xnuvem3 += 0.5
           if xnuvem3 > 1300:
               xnuvem3 = -100
               ynuvem3 = random.randint(0, 350)
           tela.blit(constantes.nuvem4, (xnuvem4, ynuvem4))
           xnuvem4 += 0.5
           if xnuvem4 > 1300:
               xnuvem4 = -100
               ynuvem4 = random.randint(0, 350)
           tela.blit(constantes.nuvem5, (xnuvem5, ynuvem5))
           xnuvem5 += 0.5
           if xnuvem5 > 1300:
               xnuvem5 = -100
               ynuvem5 = random.randint(0, 350)
           playerrect = direção.get_rect()
           playerrect.x = x
           playerrect.y = y

           tela.blit(direção, playerrect)
           if respiraçãoprafrente == True:
              movrespfrente+=1
           if respiraçãoprafrente == False:
              movrespfrente = 0

           if movrespfrente >0 and movrespfrente <=20:
              direção = parado1
           if movrespfrente >20 and movrespfrente <=40:
              direção = parado2
           if movrespfrente >40 and movrespfrente <=60:
              direção = parado3
              movrespfrente = 0
           if respiraçãopratras == True:
               movresptras += 1
           if respiraçãopratras == False:
               movresptras = 0

           if movresptras > 0 and movresptras <= 20:
               direção = parado1costas
           if movresptras > 20 and movresptras <= 40:
               direção = parado2costas
           if movresptras > 40 and movresptras <= 60:
               direção = parado3costas
               movresptras = 0


           contatoaoandarDIREITA = False
           contatoaoandarESQUERDA = False
           framerate.tick(60)
           for element in map1grass:
                element[1] -= peso
           for element in map1soil:
                element[1] -= peso
           for element in map1coins:
                element[1] -= peso

           for coordinates in map1coins:
               coin=pygame.draw.circle(tela,(201,201,25),(coordinates[0],coordinates[1]),10)
               if playerrect.colliderect(coin):
                  map1coins.remove([coordinates[0],coordinates[1]])
                  som_de_moeda.play()
           for coordinates in map1grass:
               recttile=constantes.grasstile.get_rect()
               recttile.x=coordinates[0]
               recttile.y=coordinates[1]
               tela.blit(constantes.grasstile,recttile)

               if playerrect.colliderect(recttile):
                   if playerrect.y+55 <= recttile.y+3:
                       contatodecima = True
                   if playerrect.y>= recttile.y+30:
                       contatodebaixo= True
                   if playerrect.y+55 >= recttile.y+4 and playerrect.y+55< recttile.y+80 and playerrect.x +28 <= recttile.x + 3:
                       contatoaoandarDIREITA = True
                   if playerrect.y+55 >= recttile.y+4 and playerrect.y+55< recttile.y+80 and playerrect.x >= recttile.x - 3:
                       contatoaoandarESQUERDA = True
           for coordinates in map1soil:
               soilrecttile=constantes.soiltile.get_rect()
               soilrecttile.x=coordinates[0]
               soilrecttile.y=coordinates[1]
               tela.blit(constantes.soiltile,soilrecttile)

               if playerrect.colliderect(soilrecttile):
                   if playerrect.y+55 <= soilrecttile.y+3:
                       contatodecima = True
                   if playerrect.y>= soilrecttile.y+30:
                       contatodebaixo= True
                   if playerrect.y+55 >= soilrecttile.y+4 and playerrect.x +28 <= soilrecttile.x + 3 or playerrect.y >=soilrecttile.y +1 and playerrect.x +28 <= soilrecttile.x:
                       contatoaoandarDIREITA = True
                   if playerrect.y+55 >= soilrecttile.y+4 and playerrect.y+55< soilrecttile.y+40 and playerrect.x >= soilrecttile.x - 3:
                       contatoaoandarESQUERDA = True

           if  pygame.key.get_pressed()[K_RIGHT] and contatoaoandarDIREITA == False:
               respiraçãopratras=False
               andandoprafrente += 4
               velocidadedireita = 4
               direita= True
               esquerda = False
               for element in map1grass:

                   element[0] -= velocidadedireita
               for element in map1soil:

                   element[0] -= velocidadedireita
               for element in map1coins:
                   element[0] -= velocidadedireita
           else:
               andandoprafrente=0
           if  pygame.key.get_pressed()[K_LEFT] and contatoaoandarESQUERDA==False:
               respiraçãoprafrente= False
               andandopratras+=4
               velocidadeesquerda=4
               esquerda= True
               direita = False
               for element in map1grass:
                   element[0] += velocidadeesquerda
               for element in map1soil:
                   element[0] += velocidadeesquerda
               for element in map1coins:
                   element[0] += velocidadeesquerda
           else:
               andandopratras=0
           if andandoprafrente==0 and direita == True:
              respiraçãoprafrente = True
           if andandopratras==0 and esquerda == True:
              respiraçãopratras = True

           if respiraçãoprafrente ==True:
              respiraçãopratras = False
           if respiraçãopratras == True:
              respiraçãoprafrente = False

           if direita == True and peso ==0:
                 if andandoprafrente > 0 and andandoprafrente <=20:
                    direção = frente1
                 if andandoprafrente >20 and andandoprafrente <=40:
                    direção = frente2
                 if andandoprafrente >40 and andandoprafrente <=60:
                    direção = frente3
                 if andandoprafrente > 60 and andandoprafrente <=80:
                    direção = frente4
                    andandoprafrente=1
           if esquerda == True and peso == 0:
                 if andandopratras >0 and andandopratras <=20:
                    direção = costas1
                 if andandopratras >20 and andandopratras <=40:
                    direção = costas2
                 if andandopratras >40 and andandopratras <=60:
                    direção = costas3
                 if andandopratras > 60 and andandopratras <=80:
                    direção = costas4
                    andandopratras=1
           if peso > 0 and direita==True and contatodecima == False or peso<0 and direita == True and contatodecima== False:
              direção=pulo3
           if peso > 0 and esquerda==True and contatodecima == False or peso<0 and esquerda == True and contatodecima== False :
              direção=pulo3tras
           if contatodecima ==True:
               peso=0
           if contatodebaixo==True:
               pulo=0
           if contatodecima== False:
               peso=2
           if pulo>=1 and pulo<alturadopulo:
              pulo+=1
              peso=-2

           if pulo>=alturadopulo:
              pulo=0


           for event in pygame.event.get():
              if event.type == QUIT:
                 pygame.quit()
                 exit()
              if event.type == KEYDOWN:
                  if event.key ==K_UP and contatodecima== True:
                     pulo=1

           pygame.display.flip()

class Menu_Principal():
    def __init__(self):
        self.menu = True
        while self.menu:

            tela.fill((0, 255, 150))
            framerate.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key==K_KP_ENTER:
                        self.menu=False
            tela.blit(nomedojogo,(300,100))
            tela.blit(jogar, (300,200))
            pygame.display.flip()
menu = Menu_Principal()
fases = fasesdojogo()