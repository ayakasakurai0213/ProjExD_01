import pygame as pg         # pygameモジュールをimport
import sys

def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    fonto  = pg.font.Font(None, 80)
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
        txt = fonto.render(str(tmr), True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(txt, [300, 200])
        pg.display.update()
        clock.tick(1)


if __name__ == "__main__":
    pg.init()           # pygameモジュールを初期化
    main()              # main関数(上で定義した)
    pg.quit()           # pygameモジュールの初期化を解除
    sys.exit()          # プログラムを終了