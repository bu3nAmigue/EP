Scale.default = "minor"
Root.default.set("B")
Clock.bpm=80

def note2index(note):
    scale = list(Scale.default)
    return scale[note]
def play2notes(notas,sample="b",dur=1,ritmo=8,oct=0,player=p1):
    rates = []
    for nota in notas:
        nota = note2index(nota)
        rates.append(math.pow(2,(nota+12*oct)/12))
    player >> play(sample,dur=var(ritmo,dur), rate=var(rates,dur),amp=0.5,sample=2)

### ABAJO/ARRIBA

def abajo():
    d_all.lpf=500
    d_all.solo()
def arriba():
    d_all.lpf=0
    d_all.solo(0)
def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())

####################
##### CANCION ######
####################

### VOCES ###

voice([0,0,0,0],dur=[1],lyrics="earth, air, fire, water",file="v2",lang="en",octave=4)
voice([0,6,4],dur=[1,1,2],lyrics="earth, air, fire",file="oscuro1",lang="en",octave=4)
voice([3,6,3,2,2,1],dur=[0.5]*4+[1,1],lyrics="my name is good friend",file="oscuro2",lang="en",octave=4)
voice([6,0,3,5,6,5,6,1,3,5,6,5], dur = ([0.5]*4+[1,1])*2,lyrics="my name is good friend",file="oscuro3",lang="en",octave=4)

v1.reload()
v1 >> loop('oscuro2',P[4:8], amp=var([2],[1]), formant=var([0],4),chop=0)

v1.reload()
v1 >> loop('oscuro3',P[4:8], amp=var([2],[1]), formant=var([0],4),chop=0)

v2.reload()
v2 >> loop('oscuro1',P[4:5], dur=PSum(6,4), amp=var([2],[8]), formant=var([0,[2,4]],4),chop=0, room=0, mix=0)

def intro1():
    v1 >> loop('oscuro1',P[4:8], amp=var([1],[1]), formant=var([3],4),room=0.9,mix=0.9)
def intro2():
    m2 >> gong(var([p2.pitch],4), dur=1/4, pan=linvar([-1,1],4), amp=linvar([0,2],8)).sometimes('stutter', 4)    
def intro3():
    d2 >> play('w' ,dur=PSum([1,6],4), rate=1/4) 
def intro4():
    d3 >> play('K', dur=2, sample=3)
def verso1():
    m2.stop()
    play2notes([0],"Q",dur=[4],ritmo=[4],oct=-2,player=q1)
def verso2():
    pass
def verso3():
    v1 >> loop('oscuro3_2',P[6:7], dur=PSum(6,4), amp=var([0,2],[8]), formant=var([0],4),chop=0, room=0, mix=0)
    p1 >> piano(var([0,2],4), drive=0.3, dur=PSum(7,4),amp=0.7,pan=PWhite(-1,1)).every(4,'stutter',2,dur=1) + var([0,2],8)
    #v2 >> loop("o1",P[2:6], lpf=0, rate=[2,0.5], drive=0.3, echo=0, amp=var([0.5,0],4),dur=var([2,4,1],4))
def puenteA1():
    d2.solo()
    d3 >> play('---[--]',sample=2,dur=0.5,amp=1)
    c1 >> glass([0],oct=4)
def puenteA2():
    y1 >> ambi(linvar([0,5],16), dur=1/8, cut=0, chop=0, room=0.6, mix=0.8, pan=linvar([-1,1]), amp=linvar([1,1.5,1.5,1]))
def cierre1():
    pass
def cierre2():
    Clock.clear()

### CANCION ###

intro = [intro1, intro2,intro3,intro4]
verso = [verso1,verso2,verso3]
puenteA = [puenteA1,puenteA2]
cierre = [cierre1, cierre2]
cancion = intro + verso + puenteA + verso + puenteA + verso + puenteA + verso + cierre

### EFECTOS #####

def efecto1():
    p1 >> piano([0,0,5,5,4,2], drive=0.5, dur=PSum(4,4),amp=0.4,pan=PWhite(-1,1))
    v1 >> loop('oscuro2_2',P[6:7], dur=PSum(6,4), amp=var([0,2],[8]), formant=var([0],4),chop=0, room=0, mix=0)
def efecto2():
    d3.reset() >> play('K', dur=2, sample=3)
    d3.dur=PSum(5,4)
    d3.rate=var([1,2],4)
efectos = {
    "verso3": {"efecto": efecto1, "restantes": 1},
    "verso1": {"efecto": efecto2, "restantes": 2}
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
        if fname in efectos and countRepetitions(fname,cancion) == efectos[fname]["restantes"]:
            efectos[fname]["efecto"]()
        Clock.schedule(lambda : reproducir(cancion[1:],efectos,reset,start+8),start + 8)

def arrancarCancion():
    start = Clock.mod(8) - 0.1
    Clock.schedule(lambda : reproducir(cancion,efectos,reset,start), start)
    
arrancarCancion()
