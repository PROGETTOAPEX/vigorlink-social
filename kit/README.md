# Kit social VigorLink

Sorgenti dei post Instagram (decisioni di Andrea del 15/11/2026).

- `engine.html` + `render.py`: disegnano le slide (4:5 e 9:16) e i Reel da un file JSON. Serve Playwright con Chromium e ffmpeg.
  `python3 render.py posts_plan.json <codice>` rifà un post; `only:stills` solo le immagini.
- `plan/`: il piano di 3 mesi (17/11/2026 – 13/02/2027). I testi sono in `c_mon_tue.py`, `c_wed_thu.py`, `c_fri_sat.py`;
  `build.py` assegna le date e scrive `posts_plan.json` e `plan/calendar.json` (data, codice, formato, didascalia).
- `audio/brand.py`: il suono VigorLink (originale, generato qui: nessun campione di terzi). Firma finale scelta: variante A.
  `python3 audio/brand.py <durata in secondi> out.wav A`.
- `plan/package.py`: aggiunge il suono ai Reel e prepara i JPG dei caroselli nella cartella `plan/` di questo repo.
- `img/`: schermate usate nelle slide (dalla demo, robot della Guida del 12/11/2026, più quelle rifatte il 15/11).

Regole dei testi: solo frasi verificate sull'app; VigorLink è «in arrivo nel primo trimestre 2027»; mai «prova gratis»;
nessun concorrente nominato; chiusura sulla lista Fondatori.
