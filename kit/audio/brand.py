# VigorLink sound (original, generated here: no samples, no third-party material).
# Idea: energy of a workout + tech. 124 BPM, driving pulse that builds, and a 3-note rising signature
# ("Connect. Train. Progress.") that lands on the last slide of every video.
import numpy as np, wave, sys
sr=44100; bpm=124; beat=60/bpm
def note(m): return 440*2**((m-69)/12)
def lp(x,a):
    y=np.empty_like(x); acc=0.0
    for i in range(len(x)): acc+=a*(x[i]-acc); y[i]=acc
    return y
def add(buf,a,x):
    if a>=len(buf): return
    n=min(len(x),len(buf)-a); buf[a:a+n]+=x[:n]
def make(dur,path,variant='A'):
    L=int(sr*dur); rng=np.random.default_rng(11)
    logo_at=dur-2.6                      # the signature starts here
    nb=int(np.ceil(dur/(beat*4)))+1; barN=int(sr*beat*4)
    roots=[45,45,41,43]                   # A  A  F  G
    chords=[[57,60,64],[57,60,64],[53,57,60],[55,59,62]]
    kick=np.zeros(L); bass=np.zeros(L); pl=np.zeros(L); pad=np.zeros(L); hat=np.zeros(L)
    for b in range(nb):
        s=b*barN; r=roots[b%4]; c=chords[b%4]
        build=min(1.0,(b+1)/3)            # layers come in over the first bars
        for q in range(4):
            a=s+int(q*beat*sr)
            if b>=1:
                x=np.arange(int(0.26*sr))/sr
                add(kick,a,np.exp(-x*13)*np.sin(2*np.pi*(46*x+52*(1-np.exp(-x*34))/34)))
            # off-beat bass pulse (eighths), accent off the kick
            for e in range(2):
                aa=a+int(e*beat/2*sr); x=np.arange(int(beat/2*0.92*sr))/sr; f=note(r)
                env=np.minimum(x/0.008,1)*np.exp(-x*5.5)
                w=np.sin(2*np.pi*f*x)+0.5*np.sin(2*np.pi*2*f*x)+0.22*np.sin(2*np.pi*3*f*x)
                add(bass,aa,(1.0 if e else 0.45)*env*w)
        # rising sixteenth arpeggio, from bar 2
        if b>=1:
            seq=[c[0],c[1],c[2],c[0]+12,c[1]+12,c[2]+12,c[0]+24,c[2]+12]*2
            for i,m in enumerate(seq):
                aa=s+int(i*beat/4*sr); x=np.arange(int(0.22*sr))/sr; f=note(m+12)
                add(pl,aa,build*(1.0 if i%4==0 else 0.6)*np.exp(-x*13)*(np.sin(2*np.pi*f*x)+0.35*np.sin(2*np.pi*2*f*x)))
        # hats on off-beats from bar 3
        if b>=2:
            for h in range(8):
                aa=s+int(h*beat/2*sr); n=int(0.045*sr); x=np.arange(n)/sr
                nz=rng.standard_normal(n); nz=nz-lp(nz,0.3)
                add(hat,aa,(1.0 if h%2 else 0.35)*np.exp(-x*85)*nz)
        tt=np.arange(barN)/sr; env=np.minimum(tt/0.4,1)*np.minimum((tt[-1]-tt)/0.3,1)
        p=np.zeros(barN)
        for m in c:
            for d in (-0.005,0.005):
                p+=np.sin(2*np.pi*note(m)*(1+d)*tt)+0.25*np.sin(2*np.pi*2*note(m)*(1+d)*tt)
        add(pad,s,env*p)
    pad=lp(pad,0.15)
    t=np.arange(L)/sr
    # pump: everything but the kick dips on each beat (the "breathing" of dance music)
    pump=0.45+0.55*np.minimum(((t%beat)/beat)*2.2,1)
    body=0.62*kick+pump*(0.36*bass+0.13*pl+0.035*pad)+0.07*hat
    # the body steps back when the signature comes in
    duck=np.where(t<logo_at,1.0,np.maximum(0.0,1-(t-logo_at)/0.5))
    body*=duck
    sig=np.zeros(L); rngs=np.random.default_rng(5)
    if variant=='A':
        # riser + impact: a sweep of air that climbs, then one deep hit with a bright ring (no melody)
        n=int(1.0*sr); x=np.arange(n)/sr; nz=rngs.standard_normal(n)
        sweep=np.concatenate([lp(nz[i:i+2205],0.02+0.5*(i/n)**2) for i in range(0,n,2205)])[:n]
        add(sig,int((logo_at+0.1)*sr),0.5*(x/1.0)**2*sweep)
        a=int((logo_at+1.1)*sr); x=np.arange(int(1.5*sr))/sr
        add(sig,a,1.6*np.exp(-x*5)*np.sin(2*np.pi*(40*x+70*(1-np.exp(-x*20))/20)))
        for m,g in ((57,0.5),(64,0.4),(69,0.5),(76,0.3)):
            add(sig,a,g*np.exp(-x*2.4)*np.sin(2*np.pi*note(m)*x))
    elif variant=='B':
        # "link": two notes that lock together (low, then its octave), short and dry like a click that connects
        for i,(m,g) in enumerate([(64,0.9),(76,1.0)]):
            a=int((logo_at+0.7+i*0.16)*sr); x=np.arange(int(1.7*sr))/sr; f=note(m)
            w=np.sin(2*np.pi*f*x)+0.5*np.sin(2*np.pi*2*f*x)*np.exp(-x*5)+0.25*np.sin(2*np.pi*4*f*x)*np.exp(-x*12)
            add(sig,a,g*np.minimum(x/0.003,1)*np.exp(-x*(9 if i==0 else 2.2))*w)
        a=int((logo_at+0.86)*sr); x=np.arange(int(1.4*sr))/sr
        add(sig,a,0.8*np.exp(-x*3)*np.sin(2*np.pi*note(40)*x))
    else:
        # "progress": a warm major chord that opens up and holds (A major), with a soft low landing
        a=int((logo_at+0.5)*sr); x=np.arange(int(2.0*sr))/sr
        env=np.minimum(x/0.35,1)*np.exp(-np.maximum(x-0.35,0)*1.5)
        for m,g in ((57,0.7),(61,0.55),(64,0.6),(69,0.6),(73,0.35),(76,0.3)):
            for d in (-0.003,0.003):
                add(sig,a,g*env*(np.sin(2*np.pi*note(m)*(1+d)*x)+0.2*np.sin(2*np.pi*2*note(m)*x)))
        add(sig,a,0.9*env*np.sin(2*np.pi*note(45)*x))
        sig/=max(1e-9,np.max(np.abs(sig)))/2.0
    mix=body+0.30*sig
    d=int(0.014*sr); left=mix.copy(); right=mix.copy()
    right[d:]+=0.12*sig[:-d]+0.05*pl[:-d]*duck[d:]; left[2*d:]+=0.08*sig[:-2*d]
    st=np.stack([left,right],1)
    fo=np.minimum(1,(dur-t)/0.25)*np.minimum(1,t/0.05); st*=fo[:,None]
    st/=np.max(np.abs(st))/0.9
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
if __name__=='__main__': make(float(sys.argv[1]),sys.argv[2],sys.argv[3] if len(sys.argv)>3 else 'A')
