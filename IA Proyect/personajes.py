import os, sys
from shutil import move
import pygame
import utils
import constants
import time
from mundos import Bloques


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = -1
        self.y = -1
        self.name = ""
        self.kind = ""
        self.direction = constants.DOWN
        # ---------------------------------------------
        x, y = utils.jugadorposicionmap()
        self.x = x
        self.y = y
        self.bloques =Bloques()
        # ---------------------------------------------
                
        self.sheet = pygame.image.load('data/images/linknuevospeque.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 40, 43))        
        #self.image = self.sheet.subsurface(self.sheet.get_clip())
        #self.rect = self.image.get_rect()
        #self.rect.topleft = (self.x,self.y)
        #self.frame = 0        
        #self.left_states = { 0: (0, 43, 40, 43), 1: (320, 217, 40, 43),2: (115, 217, 40, 43)  }
        #self.right_states = { 0: (0, 130, 40, 43), 1: (35, 304, 40, 43), 2: (360, 304, 40, 43) }
        #self.up_states = { 0: (0, 88, 40, 43), 1: (316, 259, 40, 43), 2: (120, 259, 40, 43) }
        #self.down_states = { 0: (35, 0, 40, 43), 1: (315, 175, 40, 43), 2: (115, 175, 40, 43) }
    

        
        #self.sheet = pygame.image.load('data/images/linknuevo.png')
        #self.sheet.set_clip(pygame.Rect(0, 0, 60, 64))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #self.image = pygame.image.load(filepath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x * 68, self.y * 68)

    def read_data_first(self):
        path = os.path.join("data", constants.PLAYER_DATA_FILE)
        mylist = utils.read_data_file(path, num_of_fields=3)
        mydict = mylist[0]
        # ----
        self.name = mydict["name"]
        self.kind = mydict["kind"]
        if utils.is_int(mydict["direction"]) == True:
            self.direction = int(mydict["direction"])
        else:
            self.direction = utils.convert_direction_to_integer(mydict["direction"])
        filepath = os.path.join("data", constants.MAPA)
        player_x, player_y = utils.PosicionPlayerMap(filepath)
        if not (player_x == self.x and player_y == self.y):
            s = "Coordenadas No Se Encuentran!\n"
            s += "Posicion Jugador Mapa: player_x, player_y: {},{}\n".format(player_x, player_y)
            s += "self.x, self.y: {},{}".format(self.x, self.y)
            raise ValueError(s)


    def coalisionbloques(self, dx=0, dy=0, bloques=None):
        for bloque in bloques:
               if bloque.x == self.x + dx and bloque.y == self.y + dy:               
                  return True
        return False

    def move(self, dx=0, dy=0, bloques=None):
        if not self.coalisionbloques(dx, dy, bloques):
            time.sleep(0.90000)

            self.x += dx
            self.y += dy
            self.rect = self.rect.move(dx * constants.Tamano, dy * constants.Tamano)

     

# -----------------------------------------------------------
#                      class Monster
# -----------------------------------------------------------

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = -1
        self.y = -1
        self.name = ""
        self.kind = ""
        # ---------------------------------------------
        # ---------------------------------------------
        self.image = None
        self.rect = None
        # ---------------------------------------------

    def read_data(self):
        filepath = os.path.join("data", constants.MONSTERS_DATA_FILE)
        numeroarchivo = 2
        mylist = utils.read_data_file(filepath, numeroarchivo)
        mydict = mylist[0]

        filepath = os.path.join("data", constants.MAPA)
        with open(filepath, "r") as f:
            mytiles = f.readlines()
            mytiles = [i.strip() for i in mytiles]
        # ------------------------------------------------------------------
        for col, tiles in enumerate(mytiles):
            for row, tile in enumerate(tiles):
                if tile == 'T':
                    self.x = (row)
                    self.y = (col)

        self.name = mydict["name"]
        self.kind = mydict["kind"]
        # ---------------------------------------------
        filepath = os.path.join("data", "images", constants.MONSTER_IMG)
        try:
            self.image = pygame.image.load(filepath).convert_alpha()
 
        except:
            s = "Couldn't open: {}".format(filepath)
            raise ValueError(s)
        self.image = pygame.transform.scale(self.image, (50, 55))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x * 65, self.y * 65)
        # ---------------------------------------------
  

# -----------------------------------------------------------
#                      class Monster
# -----------------------------------------------------------

class Princess(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = -1
        self.y = -1
        self.name = ""
        self.kind = ""
        # ---------------------------------------------
        x, y = utils.objetiveposicionmap()
        self.x = x
        self.y = y
        # ---------------------------------------------
        self.image = None
        self.rect = None
        # ---------------------------------------------

    def read_data(self):
        filepath = os.path.join("data", constants.PRINCESS_DATA_FILE)
        numeroarchivo = 2
        mylist = utils.read_data_file(filepath, numeroarchivo)
        mydict = mylist[0]

        filepath = os.path.join("data", constants.MAPA)
        with open(filepath, "r") as f:
            mytiles = f.readlines()
            mytiles = [i.strip() for i in mytiles]
        # ------------------------------------------------------------------
        for col, tiles in enumerate(mytiles):
            for row, tile in enumerate(tiles):
                if tile == 'O':
                    self.x = (row)
                    self.y = (col)

        self.name = mydict["name"]
        self.kind = mydict["kind"]
        # ---------------------------------------------
        filepath = os.path.join("data", "images", constants.PRINCESS)
        try:
            self.image = pygame.image.load(filepath).convert_alpha()       
        except:
            s = "Couldn't open: {}".format(filepath)
            raise ValueError(s)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x * 67, self.y * 66)
        







