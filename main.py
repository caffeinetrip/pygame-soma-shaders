import pygame, sys, json

import scripts.pygpen as pp
from scripts.player import Player
from scripts.level import Level

class Game(pp.PygpenGame):
    def load(self):
        pp.init(
            (1020, 660),
            fps_cap=165,
            caption='sq',
            opengl=True,
            input_path='data/key_configs/config.json',
            frag_path='shaders/shader.frag',
        )
        
        self.background_surf = pygame.Surface((340, 220))
        self.display = pygame.Surface((340, 220), pygame.SRCALPHA)
        self.ui_surf = pygame.Surface((340, 220), pygame.SRCALPHA)
        self.light_surf = pygame.Surface((340, 220))

        self.e['Renderer'].set_groups(['default', 'ui', 'bg'])
        
        self.camera = pp.Camera(self.display.get_size(), slowness=0.3, pos=[0,0])
        
        self.data_reload()
        
    def data_reload(self):
        save_file = 'data/saves/data.json'
        
        try:
            data = pp.io.read_json(save_file)
            
            if not data:
                data = pp.io.read_json('data/saves/default.json')
                pp.io.write_json(save_file, data)
                
            self.current_level = Level(list(data.get('checkpoint')), )

            self.death_count = data.get('death_count', self.death_count)
            self.map['name'] = data.get('level', self.map['name'])
            
            self.load_level(self.map['name'])
            
            self.map['tilemap'].tilemap = data.get('tilemap', self.map['tilemap'].tilemap)
            self.map['rotateset'] = data.get('rotate_tiles', self.map['rotateset'])
            self.scroll = data.get('scroll', self.scroll)
            self.player.pos = data.get('player_pos', self.player.pos)
            self.prolog_completed = data.get('prolog_completed', self.prolog_completed)

        except (json.JSONDecodeError, FileNotFoundError) as e:
            data = pp.io.read_json('data/saves/default.json')
            pp.io.write_json(save_file, data)


    def update(self):
        self.e['Renderer'].cycle({'default': self.display, 'ui': self.ui_surf, 'bg': self.background_surf})
        self.camera.update()
        

        if self.e['Input'].pressed('quit'):
            pygame.quit()
            sys.exit()
            
        self.e['Window'].cycle({'surface': self.display, 'background_surf': self.background_surf,  'ui_surf': self.ui_surf, 'light_surf': self.light_surf})
            
Game().run()