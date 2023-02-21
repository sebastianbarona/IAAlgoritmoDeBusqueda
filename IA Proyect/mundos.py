import sys, os
import pygame
import constants


class Piso(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.filepath = os.path.join("data/images", constants.PISO_IMG)
        try:
            self.image = pygame.image.load(self.filepath).convert_alpha()
        except:
            s = "Couldn't open: {}".format(self.filepath)
            raise ValueError(s)
        self.image = pygame.transform.scale(self.image, (constants.Tamano, constants.Tamano))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x * constants.Tamano, y * constants.Tamano)


class PisoLimit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.filepath = os.path.join("data/images", constants.BLOQUE_LIMITE)
        try:
            self.image = pygame.image.load(self.filepath).convert_alpha()
        except:
            s = "Couldn't open: {}".format(self.filepath)
            raise ValueError(s)
        self.image = pygame.transform.scale(self.image, (constants.Tamano, constants.Tamano))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x * constants.Tamano, y * constants.Tamano)

# -----------------------------------------------------------
#                      class Pisos
# -----------------------------------------------------------
class Pisos:
    def __init__(self):
        self.grasses = []
        filepath = os.path.join("data", constants.MAPA)
        with open(filepath, "r") as f:
            mytiles = f.readlines()
            mytiles = [i.strip() for i in mytiles]
        # ------------------------------------------------------------------
        for col, tiles in enumerate(mytiles):
            for row, tile in enumerate(tiles):
                if tile == '.' or tile == 'p' or tile == 'O' or tile == 'T':
                    mygrass = Piso(row, col)
                    self.grasses.append(mygrass)
                if tile == 'L':
                    mygrass = PisoLimit(row, col)
                    
                    self.grasses.append(mygrass)               

    def __getitem__(self, item):
        return self.grasses[item]



class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        filepath = os.path.join("data/images", constants.LAVA)
        try:
            self.image = pygame.image.load(filepath).convert_alpha()
        except:
            s = "Couldn't open: {}".format(filepath)
            raise ValueError(s)
        self.image = pygame.transform.scale(self.image, (constants.Tamano, constants.Tamano))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x * constants.Tamano, self.y * constants.Tamano)

# -----------------------------------------------------------

class BloqueLava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        filepath = os.path.join("data/images", constants.BLOQUELAVA)
        try:
            self.image = pygame.image.load(filepath).convert_alpha()
        except:
            s = "Couldn't open: {}".format(filepath)
            raise ValueError(s)
        self.image = pygame.transform.scale(self.image, (constants.Tamano, constants.Tamano))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x * constants.Tamano, self.y * constants.Tamano)

#                      class Bloques
# -----------------------------------------------------------
class Bloques:
    def __init__(self):
        self.bloques = []
        self.loop_index = 0
        filepath = os.path.join("data", constants.MAPA)
        with open(filepath, "r") as f:
            mytiles = f.readlines()
            mytiles = [i.strip() for i in mytiles]
        # ------------------------------------------------------------------
        for col, tiles in enumerate(mytiles):
            for row, tile in enumerate(tiles):
                if tile == 'm':
                    mybloque = Bloque(row, col)
                    self.bloques.append(mybloque)
                if tile == 'B':
                    mybloque = BloqueLava(row, col)
                    self.bloques.append(mybloque)
                if tile == 'L':
                    mybloque = PisoLimit(row, col)
                    self.bloques.append(mybloque)
    
   
    def __getitem__(self, item):
        return self.bloques[item]

    def __next__(self):
        if self.loop_index >= len(self.bloques):
            self.loop_index = 0
            raise StopIteration
        else:
            this_value = self.bloques[self.loop_index]
            self.loop_index += 1
            return this_value

    def __iter__(self):
        return self



