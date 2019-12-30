
# Para hacer

# Samples
    # Grabar de nuevo voces mejorables
    # Ajustar frase "esta de da un disco al final", correrla un beat o algo asi

# Arreglos
    # Entrar con el bajo primero y despues la voz, o la voz y despues el bajo. O reforzar la idea de que todo arranca junto
    # En la segunda vuelta del verso que hayan mas cosas. Agregar arreglos. Sacar cosas y despues sumar instrumentos, samples/timbres y demás, ritmo mas complejo o rapido. Buscar variantes
    # Hacer mas prolijas y emocionantes las transiciones
    # No abusar del platillo invertido, usarlo en los momentos claves

Root.default = -3
Scale.default = 'minor'
Clock.bpm=100
acordes = [(2,4,6),(-1,1,3),(0,2,4)]
escalera = P[5,4,3,2]
def nada():
    pass
def intro1():
    p1 >> space([0,0,4,2,0,0,5,2],dur=1,amp=[0,1,1,1])
    d1 >> play("X ",amp=1)
    pt >> play('#', dur=16,sus=4, rate=-1/2, amp=var([1,0],[16,inf],start=now))
def intro2():
    p1 >> space([4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
def verso1():
    p1 >> space([0,0,4,2,0,0,5,2],dur=1,amp=[0,1,1,1])
    b1 >> ambi([0,-2,4,3],dur=4,sus=3,oct=3,chop=3,amp=3)
    v1 >> loop("verso",P[0:8],formant=0,amp=2,room=0.0,mix=0.0,glide=0,chop=0)
    p2.stop()
def verso2():
    p1 >> space([4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
    v1 >> loop("verso",P[8:16],formant=0,amp=2,room=0.0,mix=0.0,glide=0,chop=0)
    d3 >> play("-")
def verso3():
    p1 >> space([0,0,4,2,0,0,5,2],dur=1,amp=[0,1,1,1])
    v1 >> loop("verso",P[0:8],formant=2,amp=2,room=0.0,mix=0.0,glide=0,chop=0)
def verso4():
    p1 >> space([4,4,2,0,3,3,2,1],dur=1,amp=[0,1,1,1])
    v1 >> loop("verso",P[8:16],formant=2,amp=2,room=0.0,mix=0.0,glide=0,chop=0)
def puenteA1():
    p1.solo()
    pt >> play('#', dur=16,sus=4, rate=-1/2, amp=var([1,0],[16,inf],start=now))
    b1 >> ambi([0],dur=4,sus=2,oct=3,chop=3)
def puenteA2():
    p1 >> space([(0,2,4)]*4,dur=2,amp=1)
    p2 >> prophet([(0,2,4)]*4,dur=2,amp=0.5)
def estribillo1():
    d1 >> play("X ",amp=1)
    d3 >> play("-",dur=PSum(6,4))
    b1 >> bass([2,-1,0,-2],dur=4,chop=2,sus=3,amp=0.7,oct=5)
    n = 5
    p1.stop()
    pt.stop()
    p2 >> prophet([(2,4,6)]*n+[(-1,1,3)]*n+[(0,2,4)]*n+[5,4,3,2],dur=list(PSum(n,4)[:n*3])+[1]*4,amp=[1,1,1,1]*3 + [1,1,1,1])
    v1 >> loop("estribillo1_pablito_rack",P[0:8],formant=[0],amp=1)
def estribillo2():
    v1 >> loop("estribillo1_pablito_rack",P[8:16],formant=[0],amp=1)
def estribillo3():
    v1 >> loop("estribillo2_mathi_rack",P[0:8],formant=[0],amp=0.7)
def estribillo4():
    v1 >> loop("estribillo2_mathi_rack",P[8:16],formant=[0],amp=0.7)
def estribillo5():
    v1 >> loop("estribillo3_pablito_rack",P[0:8],formant=[0],amp=1)
def estribillo6():
    v1 >> loop("estribillo3_pablito_rack",P[8:16],formant=[0],amp=1)
def estribillo7():
    v1 >> loop("estribillo4_pablito_rack",P[0:8],formant=[0],amp=1)
def estribillo8():
    v1 >> loop("estribillo4_pablito_rack",P[8:16],formant=[0],amp=1)
def puenteB1():
    p1.solo()
    b1 >> bass([2],dur=4,chop=3,sus=2)
    p1 >> space([(2,4,6)]*4,dur=2,amp=1)
    p2 >> prophet([(2,4,6)]*4,dur=2,amp=1)
def cierre1():
    v1 >> loop('estribillo4_pablito_rack',P[0:8], formant=0,amp=1)
    v2 >> loop('estribillo4_mathi_rack', P[8:16],formant=0, amp=0.5)
def cierre2():
    Group(v1,v2).solo()


### CANCION ###

intro = [intro1, intro2]
verso = [verso1,verso2,verso3,verso4]
puenteA = [puenteA1,puenteA2]
puenteB = [puenteB1,nada]
estribillo = [estribillo1,estribillo2,estribillo3,estribillo4,estribillo5,estribillo6,estribillo7,estribillo8]
cierre = [cierre1, cierre2]
cancion = intro + verso + puenteA + estribillo + puenteB + verso + puenteA + estribillo + cierre


### EFECTOS #####

def efecto1():
    v1.formant = 2
    d2 >> play("-")
    d1 >> play("X O ",amp=1,dur=0.25)
def efecto2():
    v1.room=0.4
    v1.mix=0.4
    d1 >> play('O ', dur=0.5)
    d2 >> play('-', dur=0.5)
def efecto3():
    d1.dur=var([1/2,1/4,1/8,1/16], [4,4,4,inf],start=now)
efectos = {
    "estribillo1": {"efecto": efecto1, "vuelta": 1},
    "verso1": {"efecto": efecto2, "vuelta": 1},
    "verso3": {"efecto": efecto3, "vuelta": 1}
}

### RESET ###

def reset():
    pass

### REPRODUCTOR ###

def countRepetitions(fname,cancion):
    fnames = list(map(lambda x : x.__name__,cancion))
    return fnames.count(fname)
def reproducir(cancion,efectos,reset,start):
    reset()
    if len(cancion) > 0:
        cancion[0]()
        fname = cancion[0].__name__
        if fname in efectos and countRepetitions(fname,cancion) == efectos[fname]["vuelta"]:
            efectos[fname]["efecto"]()
        Clock.schedule(lambda : reproducir(cancion[1:],efectos,reset,start+8),start + 8)

start = Clock.mod(8) - 0.1
Clock.schedule(lambda : reproducir(cancion,efectos,reset,start), start)