from re import X
from telnetlib import SE
import pygame
import constants
from mundos import Pisos, Bloques
from shutil import copyfile
import os, sys
from personajes import Player, Monster, Princess
from algoritmo import BFSMatriz 
import time                                                                

# ------------------------------------------------------------
#                    class TextDialog
# ------------------------------------------------------------

class TextDialog:
    def __init__(self, text,imagen):
        self.text_list = []
        self.fondo = pygame.image.load(imagen)
        if type(text) == type("abc"):
            self.text_list = "" + text
        else:
            s = "Doh! That type of data shouldn't be here!"
            raise ValueError(s)
        # -------------------------
        if len(self.text_list) > 40:
            s = "Error! Textbox should not contain more than 12 lines."
            raise ValueError(s)
        # -------------------------
        pygame.init()
        self.font = pygame.font.Font(None, 35)
        # -------------------------
        text_width, text_height = self.font.size("a")
        self.screen = pygame.display.set_mode((constants.Pantalla_Ancho, constants.Pantalla_Alto))
        # ----
        self.line_height = -1
        for elem in self.text_list:
            try:
                text_width, text_height = self.font.size(elem)
            except:
                try:
                    text_width, text_height = self.font.size(elem[0])
                except:
                    raise ValueError("Error!")
            if text_height > self.line_height:
                self.line_height = text_height
        # -------------------------
        # ----- Text Window -------
        self.keep_looping = True

    
    def _draw_lines(self):
        # karen
            surface = self.font.render(self.text_list, True, (0, 0, 0))
            # ----------------------
            left = 30
            top = 420
            # ----------------------
            self.screen.blit(surface, (left, top), area=None)

    def draw(self):
        self.screen.blit(self.fondo,(0,0))
        # ----------------------
        self._draw_lines()
        time.sleep(5)
        self.keep_looping = False
        # --------------------------------------------------
        pygame.display.flip()

    def main(self):
        while self.keep_looping:
            self.draw()



class Game:
    def __init__(self):
        self.init_pygame()
        self.pisos = Pisos()
        self.bloques = Bloques() 
        self.monster = Monster()
        self.princess = Princess()
        self.player = Player()
        self.bfs = BFSMatriz(self.player.x,self.player.y,self.princess.x,self.princess.y)
  
        self.all_sprites = pygame.sprite.Group()
        # -------------------------------------
        self.keep_looping = True
        # -------------------------------------
        source_file = os.path.join("data", constants.MONSTERS_ORIGINAL_DATA_FILE)
        destination_file = os.path.join("data", constants.MONSTERS_DATA_FILE)
        copyfile(source_file, destination_file)
        source_file = os.path.join("data", constants.PLAYER_ORIGINAL_DATA_FILE)
        destination_file = os.path.join("data", constants.PLAYER_DATA_FILE)
        copyfile(source_file, destination_file)

    def read_data(self):
        self.player.read_data_first()
        self.monster.read_data()
        self.princess.read_data()       

    def init_pygame(self):
        pygame.init()
        self.BG_COLOR = constants.BG_COLOR
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Enter {}".format(constants.TITLE))
        self.screen = pygame.display.set_mode((constants.Pantalla_Ancho, constants.Pantalla_Alto))
        print("ANCHO:" + str(constants.Pantalla_Ancho) + ", ALTO:" + str(constants.Pantalla_Alto))
        self.font = pygame.font.Font(None, 40)

    def monsterenubicacion(self, x, y):
        if self.monster.x == x and self.monster.y == y:
            return True
        return False

    def princcessubicacion(self, x, y):
        if self.princess.x == x and self.princess.y == y:
            return True
        return False

    def recorrido(self,conteo,x):        
                print("Recorrido")
                coordenadas = [] 
                malvadox= self.monster.x
                malvadoy= self.monster.y

                princessx = self.princess.x
                princessy = self.princess.y

                for i in self.bfs:
                    coordenadas.append(i)
                              
                tamano=len(coordenadas);
                if conteo == tamano:
                    im = 'data/images/' + constants.WINNER                            
                    mydialog = TextDialog("Vivieron Felices Y Comieron Perdices",im)
                    mydialog.main()      
                    time.sleep(15)
                    self.keep_looping = False
                    return True
                                        
                if conteo+1 < tamano:                                    
                        x=(coordenadas[conteo][1])
                        y=(coordenadas[conteo][0])
                                                   
                        rutax=(coordenadas[conteo +1][1])
                        rutay=(coordenadas[conteo +1][0])
                        
                        if x == malvadox and y == malvadoy:
                            im = 'data/images/' + constants.BATTLE
                            
                            mydialog = TextDialog("Link Se Encuentra En Una Feroz Batalla ",im)
                            mydialog.main()      
                            time.sleep(10)
                            self.filepath = os.path.join("data/images", constants.PISO_IMG)                                                 
                            self.monster.image = pygame.image.load(self.filepath).convert_alpha()
                            self.monster.image = pygame.transform.scale(self.monster.image, (constants.Tamano, constants.Tamano))
                            self.monster.rect = self.monster.image.get_rect()
                            self.monster.rect = self.monster.rect.move(x * constants.Tamano, y * constants.Tamano)
                                                                        
                        
                        if x == rutax and y == rutay:                            
                            #STOP
                            print("STOP")
                            return self.player.move(dx=0, dy=0, bloques=self.bloques)
           
                        if x > rutax and y == rutay:
                            #LEFT
                            print("LEFT")
                            return self.player.move(dx=-1, dy=0, bloques=self.bloques)
                            
                        if x < rutax and y == rutay:
                            #RIGHT
                            print("RIGHT")                                                    
                            return self.player.move(dx=1, dy=0, bloques=self.bloques)
                                                
                        if y > rutay and x == rutax:
                            #UP
                            print("UP")
                            return self.player.move(dx=0, dy=-1, bloques=self.bloques)
                        if y < rutay and x == rutax:
                            #Down
                            print("DOWN")
                            return self.player.move(dx=0, dy=1, bloques=self.bloques)
                    

            

    def handle_events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.keep_looping = False
                    return True                                                                            

    def update_classes(self):
        for elem in self.pisos:
            self.all_sprites.add(elem)
        for elem in self.bloques:
            self.all_sprites.add(elem)
        self.all_sprites.add(self.monster)        
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.princess)

    def draw(self):
        self.screen.fill(self.BG_COLOR)
        self.update_classes()
        # ----
        self.all_sprites.update(self.bfs)
        self.all_sprites.draw(self.screen)
        # ----
        pygame.display.flip()

    def main(self):
        self.clock.tick(constants.FRAME_RATE)
        contador=0
        contadorx=1
        
        while self.keep_looping:                
                for i in self.bfs:
                    self.handle_events()
                    self.recorrido(conteo = contador,x=contadorx)
                    contador+=1
                    contadorx = 0
                    self.draw()
        self.myquit()

    def myquit(self):
        pygame.quit()
        # sys.exit()


if __name__ == "__main__":
    mygame = Game()
    mygame.read_data()
    mygame.main()



