import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    
    tmr = 0
    x=0
    ko_img=pg.image.load("ex01/fig/3.png")
    ko_img=pg.transform.flip(ko_img,True,False)
    ko1_img=pg.transform.rotozoom(ko_img,10,1.0)
    
    koimages=[ko_img,pg.transform.rotozoom(ko_img,1,1.0),
              pg.transform.rotozoom(ko_img,2,1.0),pg.transform.rotozoom(ko_img,3,1.0),
              pg.transform.rotozoom(ko_img,4,1.0),pg.transform.rotozoom(ko_img,5,1.0),pg.transform.rotozoom(ko_img,6,1.0),
              pg.transform.rotozoom(ko_img,7,1.0),pg.transform.rotozoom(ko_img,8,1.0),pg.transform.rotozoom(ko_img,9,1.0),pg.transform.rotozoom(ko_img,10,1.0),pg.transform.rotozoom(ko_img,9,1.0),
              pg.transform.rotozoom(ko_img,8,1.0),pg.transform.rotozoom(ko_img,7,1.0),pg.transform.rotozoom(ko_img,6,1.0),pg.transform.rotozoom(ko_img,5,1.0),pg.transform.rotozoom(ko_img,4,1.0),
              pg.transform.rotozoom(ko_img,3,1.0),pg.transform.rotozoom(ko_img,2,1.0),pg.transform.rotozoom(ko_img,1,1.0)]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if x==3200:
            x=0
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[1600-x,0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[4800-x,0])
        screen.blit(koimages[tmr%20],[400,200])
        pg.display.update()
        tmr += 1  
        x+=1      
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()