import pygame, sys

import scripts.pygpen as pp


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
        
    def update(self):
        self.camera.update()
        
        if self.e['Input'].pressed('quit'):
            pygame.quit()
            sys.exit()
            
Game().run()