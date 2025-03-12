
import scripts.pygpen as pp
import pygame

class Level(pp.Element):
    def __init__(self, chekpoint, tilemap_path, music=None):
        super().__init__()

        self.current_chekpoint = chekpoint
        self.tileset = tilemap_path
        
        self.tilemap = pp.Tilemap(tile_size=(16, 16))
        self.tilemap.load(tilemap_path, spawn_hook=chekpoint)
        
        self.rotateset = []
        
        self.music = music
        
    def play_music(self, index_):
        pygame.mixer.music.load(self.music[index_])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)