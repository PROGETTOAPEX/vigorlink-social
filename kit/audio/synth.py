# Original backing track for the Reels, generated here (no samples, no third-party material): free of rights.
import numpy as np, wave
sr=44100; bpm=96; beat=60/bpm; bars=12; L=int(sr*beat*4*bars)
t=np.arange(L)/sr; out=np.zeros(L)
def note(m): return 440*2**((m-69)/12)
def lp(x,a):
    y=np.empty_like(x); acc=0.0
    for i in range(len(x)): acc+=a*(x[i]-acc); y[i]=acc
    return y
# Am7 - Fmaj7 - Cmaj7 - G6, one bar each
chords=[[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,64]]
bass=[45,41,36,43]
rng=np.random.default_rng(7)
pad=np.zeros(L); bs=np.zeros(L); pl=np.zeros(L)
barN=int(sr*beat*4)
for b in range(bars):
    c=chords[b%4]; s=b*barN; tt=np.arange(barN)/sr
    env=np.minimum(tt/0.6,1)*np.minimum((tt[-1]-tt)/0.5,1)
    for m in c:
        f=note(m)
        for d in (-0.004,0,0.004):
            pad[s:s+barN]+=env*(np.sin(2*np.pi*f*(1+d)*tt)+0.3*np.sin(2*np.pi*2*f*(1+d)*tt)+0.12*np.sin(2*np.pi*3*f*tt))
    f=note(bass[b%4])
    for k,(st,ln) in enumerate([(0,1.5),(1.5,0.5),(2,1.5),(3.5,0.5)]):
        a=s+int(st*beat*sr); n=int(ln*beat*sr); x=np.arange(n)/sr
        e=np.minimum(x/0.01,1)*np.exp(-x*2.2)
        bs[a:a+n]+=e*(np.sin(2*np.pi*f*x)+0.25*np.sin(2*np.pi*2*f*x))
    # plucked arpeggio, eighth notes, from bar 2 on
    if b>=2:
        seq=[c[0]+12,c[2]+12,c[1]+12,c[3]+12,c[2]+12,c[3]+12,c[1]+12,c[2]+12]
        for i,m in enumerate(seq):
            a=s+int(i*beat/2*sr); n=int(0.45*sr); x=np.arange(n)/sr
            if a+n>L: n=L-a; x=x[:n]
            pl[a:a+n]+=np.exp(-x*7)*(np.sin(2*np.pi*note(m)*x)+0.4*np.sin(2*np.pi*2*note(m)*x))*(0.8 if i%2==0 else 0.5)
# drums from bar 2: soft kick on 1 and 3, rim/clap on 2 and 4, hats on eighths
dr=np.zeros(L)
for b in range(2,bars):
    s=b*barN
    for q in range(4):
        a=s+int(q*beat*sr)
        if q in (0,2):
            n=int(0.28*sr); x=np.arange(n)/sr
            dr[a:a+n]+=1.1*np.exp(-x*14)*np.sin(2*np.pi*(48*x+38*(1-np.exp(-x*30))/30))
        else:
            n=int(0.14*sr); x=np.arange(n)/sr
            dr[a:a+n]+=0.35*np.exp(-x*38)*lp(rng.standard_normal(n),0.5)
    for h in range(8):
        a=s+int(h*beat/2*sr); n=int(0.05*sr); x=np.arange(n)/sr
        nz=rng.standard_normal(n); nz=nz-lp(nz,0.35)
        dr[a:a+n]+=(0.10 if h%2 else 0.06)*np.exp(-x*90)*nz
pad=lp(pad,0.12)
mix=0.050*pad+0.42*bs+0.16*pl+0.55*dr
# simple stereo: pluck delayed on the right
d=int(0.012*sr); left=mix.copy(); right=mix.copy(); right[d:]+=0.10*pl[:-d]; left[d:]+=0.02*pl[:-d]
st=np.stack([left,right],1); st/=np.max(np.abs(st))/0.85
w=wave.open('bed.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
print(L/sr)
