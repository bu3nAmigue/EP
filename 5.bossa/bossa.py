
Root.default = -3
Scale.default = 'lydian'
Clock.bpm=117
def changemode(root,scale):
    Root.default.set(root)
    Scale.default.set(scale)

### PLAYERS ###
if not sh: sh = Player();
if not gt: gt = Player();
if not ba: ba = Player();
if not go: go = Player();
if not gb: gb = Player();

## PARTES ###
changemode(0, 'minor')
bases = var([0,1,P[2,2, -3],P[4,1, -2]],4)
def intro1():
    p2 >> play('f  f  f   f  f  ',dur=1/2,amp=0.1,sample=3)
def intro2():
    sh >> play('s',dur=1/2,amp=P[1.7,0.9,1.15,0.9]*0.4)
def levada():
    gt >> orient(0,dur=P[2,3,2,2,2,2,2,1]/2,amp=0.24,sus=1,lpf=300) + var([(-1,2,4),(-1,2,3)],P[3,5])
    ba >> orient([0,0,-3,-3],dur=P[3,1]/2,amp=0.24,sus=1,lpf=300,oct=3)
def levada2():
    gt.reset() >> orient(bases,dur=P[2,3,2,2,2,2,2,1]/2,amp=PRand([0.45]),sus=1,lpf=300,oct=5).every(6,'stutter',3,dur=2,oct=6,amp=0.5,lpf=400,delay=3).every(4,'jump',2,delay=1/2) + var([(-1,2,4),(-1,2,3)],P[3,5])
    ba >> orient(P[0,0,-3,-3] + bases,dur=P[3,1]/2,amp=0.3,sus=1,lpf=300,oct=3)
def percussion():
    sh >> play('s',amp=P[1.7,0.9,1.15,0.9]*0.4)
    bd >> play('v(   ( v))(   v)(vvv )',dur=1/2,amp=0.3,sus=P[P[1,100],0,0,1]/1000,sample=4)
    p2 >> play('f  f  f   f  f  ',amp=0.1,sample=3)
def breakkicks():
    bd >> play('v(   ( v))(   v)(vvv )',dur=ritmos[-1],amp=0.3,sus=P[P[1,100],0,0,1]/1000,sample=4)
def phrase():
    changemode(-5,'lydian')
    go >> blip(P['97 434' + '6  543210 '],dur=1/2,amp=var([0,1],8),delay=1,lpf=1000)
def phr1():
    changemode(-5,'lydian')
def pause_melodies():
    go.stop()
    gt.stop()
    ch.stop()
def upper_melody():
    notes = var(PWalk(5)[:8],1)
    go.reset() >> nylon(notes,dur=silencio(3,8)/2,sus=2,amp=var([0,1],8)*0.5,delay=1,lpf=1000,oct=7)
def pause_percussion():
    sh.stop()
    p2.stop()
def glitch_percussion():
    gb >> play('N',dur=1/4,amp=PRand(3)[:29]/3,sus=0.1,sample=PRand(5)[:13], pan=PRand([-1,0,1])[:17]).sometimes('reverse')
def snare():
    sn >> play('  u ', dur=1, amp=0.7, lpf=2000 + sinvar([0,1500],16), echo=1, mix=0.5)
def staccatto():
    gt.sus=PRand(4)[:16]/4 + 0.1
def ending1():
    pause_melodies()
    pause_percussion()
    glitch_percussion()
    go.reset() >> nylon([0],dur=ritmos[-2],sus=3,amp=var([1],8)*0.1,delay=1,lpf=1200,oct=4,formant=0) + (P[-1,0,3,4], P[9,7,6])
def ending2():
    m1 >> nylon([0],dur=4,chop=0,oct=3,lpf=1000,amp=0.5)
def hiblips():
    go >> blip([0],dur=silencio(0,8)/4,sus=2,amp=var([0,1],8)*0.3,delay=1,lpf=1000,oct=7)
def solo_alto():
    notes = var(PWalk(5)[:8],1)
    g2 >> nylon(notes,dur=silencio(2,8)/2,sus=g2.dur*1,amp=var([1],8)*0.4,delay=2,lpf=1000,oct=7,drive=0.0)
def campanas():
    ch >> bell(var([0,2],4),dur=ritmos[-2],amp=0.1,delay=PRand([0]),oct=5).every(6,'stutter',6,dur=3,pan=[-1,1],oct=6) + var([0,2],8) + var([go.pitch],0.5)
def espacio():
    pp >> space(var([[0],-1],P[2,3,1,2]/2),dur=P[2,3,2,1,2,3,2,1]/2,amp=P[0.9]*(0.5,0.25),oct=var([5,6],16),delay=PRand([0,0.5]),amplify=PRand([1,1,0,1]),hpf=1000) + var([0,-2],8) + P[0,2,0,0].every(4,'shuffle')
def espacio2():
    go.reset() >> blip(dur=0.25,sus=2,delay=1,amp=0.24,lpf=1000,oct=9).follow(pp) + [0,2,4,6]

# levada2()

def createMelody():
    notes = PWalk(5)[:5]
    return notes

def silencio(index,dur):
    durs = [1 for i in range(dur)]
    durs[index] = rest(1)
    return Pattern(durs)




# sintes()
# sonando()
# Group(sn,gt,go,d1).solo(0)
# arpy()
# changeDur(0.5)
# abajoarriba(8)
# ch.stop()
# bases = var([0,2,0,-1],16)
# changemode(-4,'lydianAug')
# changemode(-2, 'mixolydian')
# changemode(1, 'lydian')
# changemode(-4, 'lydian')
# changemode(-5, 'phrygian')
# changemode(-4, 'lydianAug')
#


### EFECTOS #####

efectos = {}

### RESET ###

def reset():
    pass

intro = [intro1, intro2, phrase]
cancion = intro + [levada, phr1, percussion]

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
