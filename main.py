from src.ABC import *

def update_rope(G, S):
    for item in G.get_backs_id("14"):
        item["shape"] = ' '
        item["iid"] = None

    vector = S.bottom.x - S.top.x, S.bottom.y - S.top.y

    for i in range(1,5):
        x = int(vector[0] * i*0.2 + S.top.x)
        y = int(vector[1] * i*0.2 + S.top.y)

        G.draw((1,1), "14", (x,y), '.')

def main():
    t = time()
    play = True; fps = 20
    G = Engine((100,31),fps)

    G.draw_fore(10, (10,5), 'O', False)
    G.draw_fore(11, (10,5), 'O', False)

    Omega = Space(t, gravity_coord=100)
    TOP = Obj(10, 5, 0, 0, True)
    BOTTOM = Obj(10, 5, 0.1, 0, False)
    S = String(1, TOP, BOTTOM, angle = 3)

    while(1):
        Omega.update()
        S.update(Omega)
        G.move_fore(11, (int(S.bottom.x), int(S.bottom.y)))
        update_rope(G, S)
        G.display()

if __name__ == "__main__":
    main()