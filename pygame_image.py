import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    
    tmr = 0
    ko_img=pg.image.load("ex01/fig/3.png")
    ko_img=pg.transform.flip(ko_img,True,False)
    ko1_img=pg.transform.rotozoom(ko_img,10,1.0)
    koimages=[ko_img,ko1_img]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if tmr==1599:
            tmr=0
        x=-tmr
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img,[1599+x,0])
        if tmr%2==0:
            screen.blit(koimages[0],[400,200])
        else:
            screen.blit(koimages[1],[400,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()