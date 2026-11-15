"""Monday (a problem → how VigorLink answers it) and Tuesday (a feature shown live). Reels.
Every product claim comes from the landing page reviewed on 10/11/2026, the in-app Guide screenshots of 12/11/2026
or checks done on 15/11/2026. Not used on purpose: Google Calendar sync, Apple Health, Android, videos of the
catalogue, "works offline" without its condition, plan prices, "automations included"."""
from lib import *

MON = [
 # 23/11
 P("M01_scheda_e_poi_buio", [
   hero("Ti è mai successo?", "Gli mandi la scheda.", "E poi? Buio.", "Si allena? La segue? L'ha capita? Lo scopri al prossimo incontro, se va bene.",
        chips=[chip("«Tutto ok con la scheda?»", "visualizzato 3 giorni fa", y=0.70)]),
   dev("VigorLink", "Lo vedi", "mentre accade.", "Chi si allena, chi si è fermato, chi ti aspetta: aggiornato mentre i tuoi atleti si allenano.", laptop="showcase-pt-athletes"),
   lst("Per ogni atleta", "Niente più", "«com'è andata?»", [("Ogni serie registrata", "kg e ripetizioni, allenamento per allenamento"), ("Chi è fermo da giorni", "lo vedi subito, senza scorrere le chat"), ("I record", "segnati da soli quando arrivano")]),
   cta()],
   "Gli mandi la scheda. E poi? Buio. 🌑\nSi allena? La segue? L'ha capita? Con VigorLink lo vedi mentre accade: ogni serie registrata, chi si è fermato, chi ti aspetta.\n\nQuanti dei tuoi clienti sai per certo che si sono allenati questa settimana? 👇"),
 # 30/11
 P("M02_che_peso_metto", [
   hero("Ore 23:04", "«Coach, che peso", "metto domani?»", "La domanda più frequente della settimana. E arriva sempre quando hai staccato.",
        chips=[chip("Che peso metto oggi?", "23:04", y=0.70)]),
   dev("VigorLink", "Il carico consigliato", "è già scritto.", "Calcolato da quello che ha fatto l'ultima volta, con le regole che scegli tu.", phone="social-player-consigliato"),
   lst("Come funziona", "Decidi tu", "la regola.", [("Prima le ripetizioni o prima il carico", "scegli il metodo una volta, vale per le tue schede"), ("Conta RPE o RIR", "se l'ultima serie era al limite, il carico resta uguale"), ("L'atleta può cambiarlo", "quello che vede sullo schermo è quello che salva")],
       note="Per i fisioterapisti il carico consigliato è spento: decide sempre il professionista."),
   cta()],
   "«Coach, che peso metto domani?» Ore 23:04. 😅\nCon VigorLink il carico consigliato è già scritto nella serie da fare: lo calcola da quello che l'atleta ha fatto l'ultima volta, con le regole che scegli tu. E lui può sempre cambiarlo.\n\nA che ora ti arriva di solito questa domanda? 👇"),
 # 7/12
 P("M03_macchinario_occupato", [
   hero("In sala pesi, ore 18:30", "Macchinario occupato.", "E adesso?", "L'atleta aspetta, salta l'esercizio o ti scrive. Di solito salta.",
        chips=[chip("La pressa è occupata, che faccio?", "18:31", y=0.70)]),
   dev("VigorLink", "Sostituzione rapida,", "dal Player.", "Due o tre alternative con lo stesso target muscolare. Solo per questa sessione.", phone="m-athlete-substitute"),
   lst("E tu lo sai", "La scheda", "resta la tua.", [("Vale solo per oggi", "la scheda non cambia"), ("Lo vedi nell'allenamento", "«variato in sessione», con l'esercizio che ha sostituito"), ("I carichi restano separati", "ogni esercizio tiene il suo storico")]),
   cta()],
   "Macchinario occupato. E adesso? 🏋️\nCon VigorLink l'atleta apre «Sostituzione rapida» dal Player: due o tre alternative con lo stesso target muscolare, solo per quella sessione. La scheda resta la tua e tu vedi cosa ha cambiato.\n\nCosa fanno oggi i tuoi clienti quando l'attrezzo è occupato? 👇"),
 # 14/12
 P("M04_rincorrere_pagamenti", [
   hero("Il messaggio che nessuno vuole scrivere", "«Ciao, mi mancherebbe", "il bonifico di novembre…»", "Fare il personal trainer non dovrebbe voler dire fare il recupero crediti."),
   dev("VigorLink", "La richiesta", "la manda l'app.", "L'atleta la trova in Home e paga dal telefono, con il metodo che hai scelto tu.", phone="showcase-athlete-home"),
   lst("Senza imbarazzo", "Tu alleni.", "Il resto è scritto.", [("Carta, bonifico, PayPal, Satispay, SumUp o contanti", "decidi tu quali metodi offrire"), ("0 € trattenuti da VigorLink", "restano solo le commissioni del metodo che usi"), ("Scaduti in evidenza", "sai sempre chi deve ancora pagare")]),
   cta()],
   "«Ciao, mi mancherebbe il bonifico di novembre…» 😬\nCon VigorLink la richiesta di pagamento la manda l'app: l'atleta la trova in Home e paga dal telefono, con il metodo che hai scelto tu. VigorLink non trattiene nulla (restano solo le commissioni del metodo che usi).\n\nQuanto tempo perdi ogni mese a ricordare i pagamenti? 👇"),
 # 21/12
 P("M05_quanto_ho_incassato", [
   hero("Domanda semplice", "Quanto hai incassato", "questo mese?", "Se la risposta è «devo controllare su tre app», è già una risposta."),
   dev("Finance", "Un numero.", "Sempre aggiornato.", "Incassato del mese, un anno in una curva, scaduti da sollecitare, risultato.", laptop="showcase-pt-finance-1511"),
   lst("Per decidere", "Non è contabilità.", "È chiarezza.", [("Incassi e uscite in un posto", "anche letti dalle fatture elettroniche che hai già"), ("Previsione dei prossimi mesi", "tre scenari con le ipotesi dichiarate"), ("La contabilità ufficiale resta dov'è", "dal tuo commercialista o nel tuo programma di fatturazione")]),
   cta()],
   "Quanto hai incassato questo mese? 💶\nSe devi aprire tre app per rispondere, è già una risposta. In Finance il numero è uno, sempre aggiornato: incassato, scaduti da sollecitare, risultato.\nNon sostituisce il commercialista: ti serve per decidere.\n\nTu dove tieni i conti oggi? 👇", kind="biz"),
 # 28/12
 P("M06_cliente_sparisce", [
   hero("Succede piano", "Salta una volta.", "Poi due. Poi sparisce.", "Quando te ne accorgi ha già disdetto nella sua testa."),
   dev("VigorLink", "Te lo dice", "prima.", "Un punteggio per ogni atleta: allenamenti, appuntamenti e pagamenti incrociati.", laptop="m-pt-athletes-health"),
   lst("In Home, ogni giorno", "«Hanno bisogno", "di te».", [("Chi è a rischio", "con il motivo scritto in chiaro"), ("Chi è fermo da giorni", "prima che diventino settimane"), ("Decidi tu cosa fare", "un messaggio, una chiamata, una scheda nuova")]),
   cta()],
   "Salta una volta. Poi due. Poi sparisce. 👻\nCon VigorLink lo vedi prima: un punteggio per ogni atleta e, in Home, la lista «Hanno bisogno di te» con il motivo scritto in chiaro. Poi decidi tu cosa fare.\n\nDa cosa capisci oggi che un cliente sta per mollare? 👇"),
 # 4/1
 P("M07_gennaio_pieno", [
   hero("Buon anno, coach", "Gennaio:", "dieci clienti in dieci giorni.", "Il mese più bello e più caotico dell'anno. Schede, anamnesi, pagamenti: tutto insieme."),
   dev("VigorLink", "Parti da un modello,", "non da zero.", "Le tue schede tipo, pronte da assegnare e adattare in pochi minuti.", laptop="m-pt-templates"),
   lst("Il nuovo cliente", "Dentro", "in pochi passaggi.", [("Lo inviti con un link", "attiva l'account e sceglie la sua password"), ("Consensi e questionario nell'app", "niente moduli di carta da rincorrere"), ("Scheda assegnata da un modello", "e lui la trova subito sul telefono")]),
   cta()],
   "Gennaio: dieci clienti nuovi in dieci giorni. 🎆\nCon VigorLink parti dai tuoi modelli di scheda, inviti il cliente con un link e consensi e questionario li compila nell'app.\n\nCom'è il tuo gennaio di solito: pieno o pienissimo? 👇"),
 # 11/1
 P("M08_vocali", [
   hero("3 minuti e 47 secondi", "Un altro", "vocale lungo.", "Lo ascolti tra un cliente e l'altro, poi ti dimentichi cosa chiedeva.",
        chips=[chip("🎤 Messaggio vocale", "3:47", y=0.70)]),
   dev("VigorLink", "I vocali", "li leggi.", "Trascritti nella chat: capisci in dieci secondi cosa ti serve sapere.", laptop="showcase-pt-messages"),
   lst("La chat del lavoro", "Separata", "dalla tua vita.", [("Vocali trascritti", "li leggi quando non puoi ascoltare"), ("Risposte salvate", "per le domande che arrivano sempre uguali"), ("Fuori da WhatsApp", "il numero personale torna personale")]),
   cta()],
   "Un altro vocale da 3 minuti e 47. 🎤\nIn VigorLink i vocali vengono trascritti nella chat: li leggi in dieci secondi, anche quando non puoi ascoltare. E la chat del lavoro resta separata dal tuo WhatsApp.\n\nIl vocale più lungo che hai ricevuto da un cliente? 👇"),
 # 18/1
 P("M09_tasse_a_sorpresa", [
   hero("Giugno e novembre", "Le tasse", "a sorpresa.", "Non sono una sorpresa: è che nessuno ti dice prima quanto mettere da parte."),
   dev("Finance · regime forfettario", "Una stima,", "mese per mese.", "Imposta e contributi stimati dai tuoi incassi, con le scadenze in calendario.", laptop="m-finance-taxes"),
   lst("Con i piedi per terra", "Una stima,", "non la dichiarazione.", [("Parte dai tuoi incassi veri", "e si aggiorna quando ne registri di nuovi"), ("Ti avvisa se ti avvicini al limite", "del regime forfettario"), ("La dichiarazione resta al commercialista", "tu arrivi all'appuntamento sapendo già l'ordine di grandezza")]),
   cta()],
   "Le tasse «a sorpresa» di giugno e novembre. 🧾\nIn regime forfettario Finance stima imposta e contributi dai tuoi incassi e ti avvisa se ti avvicini al limite. È una stima per organizzarti: la dichiarazione resta al tuo commercialista.\n\nMetti da parte ogni mese o speri bene? 👇", kind="biz"),
 # 25/1
 P("M10_pensata_per_altri", [
   hero("Lo hai notato anche tu?", "App pensate", "per un altro Paese.", "Dollari, libbre, menu tradotti a metà. E del regime forfettario nessuna traccia."),
   lst("VigorLink", "Nato in italiano.", "Per chi lavora in Italia.", [("Tutta l'app in italiano", "anche per i tuoi atleti, senza traduzioni a metà"), ("Regime forfettario e fatture elettroniche", "le fatture XML che hai già si leggono da sole"), ("Bonifico, Satispay, PayPal, SumUp, carta", "i metodi che i tuoi clienti usano davvero")], icons=["🇮🇹", "🧾", "💶"]),
   lst("E per i fisioterapisti", "L'app parla", "la tua lingua.", [("«Paziente» e «seduta»", "in tutta l'app, nei PDF e nelle email"), ("Valutazioni, consenso, diario delle sedute", "gli strumenti del tuo lavoro"), ("Nessun giudizio automatico", "decide sempre il professionista")]),
   cta()],
   "App per PT pensate per un altro Paese: dollari, libbre, menu tradotti a metà. 🌍\nVigorLink è nato in italiano, per chi lavora in Italia: regime forfettario, fatture elettroniche, i metodi di pagamento che i tuoi clienti usano davvero.\n\nQual è la cosa più «americana» della tua app di oggi? 👇"),
 # 1/2
 P("M11_non_capisce_esercizio", [
   hero("In palestra, da solo", "«Ma questo esercizio", "come si fa?»", "Il nome sulla scheda non basta. E tu non sei lì."),
   dev("VigorLink", "«Come si esegue»,", "a un tocco.", "Muscoli coinvolti e istruzioni passo passo, accanto a ogni esercizio.", phone="showcase-athlete-exercise"),
   lst("E le tue indicazioni", "La tua voce,", "nella scheda.", [("Le note del coach sull'esercizio", "l'atleta le legge prima di iniziare"), ("Muscoli principali e secondari", "disegnati, non solo scritti"), ("Se ha un dubbio ti scrive", "dalla chat, senza uscire dall'app")]),
   cta()],
   "«Ma questo esercizio come si fa?» 🤔\nIn VigorLink accanto a ogni esercizio c'è «Come si esegue»: muscoli coinvolti e istruzioni passo passo. Più le tue note, che l'atleta legge prima di iniziare.\n\nQual è l'esercizio che i tuoi clienti sbagliano più spesso? 👇"),
 # 8/2
 P("M12_scheda_cambiata", [
   hero("Scheda_finale_v3_DEFINITIVA.pdf", "Qual era", "la versione giusta?", "Modifichi la scheda, poi il cliente ti chiede com'era prima. E non lo sai più."),
   lst("VigorLink", "Ogni modifica", "resta nella storia.", [("Le versioni della scheda", "vedi quando è cambiata e cosa"), ("Le differenze a colpo d'occhio", "esercizi aggiunti, tolti, modificati"), ("Torni indietro quando vuoi", "ripristini una versione precedente")], icons=["🕘", "🔍", "↩️"]),
   lst("E lo storico dell'atleta", "Quello che ha fatto", "non si perde.", [("Le serie registrate restano", "anche se togli l'esercizio dalla scheda"), ("I progressi continuano", "da una scheda alla successiva"), ("Niente file da rinominare", "la scheda attuale è sempre una sola")]),
   cta()],
   "Scheda_finale_v3_DEFINITIVA.pdf 😅\nIn VigorLink ogni modifica resta nella storia della scheda: vedi cosa è cambiato e, se serve, torni a una versione precedente. E le serie già registrate dall'atleta non si perdono.\n\nQuante versioni ha la scheda più modificata che hai fatto? 👇"),
]

TUE = [
 # 17/11
 P("T00_player_una_serie", [
   hero("Dentro VigorLink · il Player", "Una serie", "alla volta.", "Chi spinge in palestra ha la vista annebbiata dalla fatica. Lo schermo deve essere chiaro."),
   dev("In allenamento", "La serie da fare", "è una sola.", "Evidenziata, con il carico consigliato già scritto. Un tocco e parte il recupero.", phone="social-player-recupero"),
   lst("Pensato per la sala pesi", "Meno errori,", "più allenamento.", [("Tocchi ✓ e hai finito", "la serie è salvata, il recupero parte da solo"), ("+15 secondi o salta", "con un tocco, senza cercare menu"), ("Record segnalati subito", "anche se correggi una serie")]),
   cta()],
   "Il Player di VigorLink: una serie alla volta. 🎯\nLa serie da fare è evidenziata, con il carico consigliato già scritto. Tocchi ✓ e parte il recupero. Pensato per chi ha il fiatone, non per chi è seduto alla scrivania.\n\nCosa usano oggi i tuoi clienti per segnare le serie? 👇"),
 # 24/11
 P("T01_editor_a_righe", [
   hero("Dentro VigorLink · l'editor", "Scrivi", "«Squat 5x5 75% 3′».", "E l'esercizio è pronto. Come sul quaderno, ma ordinato."),
   dev("Editor a righe", "Una riga,", "un esercizio.", "Serie, ripetizioni, intensità e recupero: li riconosce mentre scrivi.", laptop="showcase-pt-editor"),
   lst("Per andare veloce", "Meno clic,", "più programmazione.", [("L'ultima volta e il massimale accanto", "programmi guardando i numeri veri dell'atleta"), ("Blocchi AMRAP, EMOM e Tabata", "da salvare e riusare"), ("O parti dal tuo file", "PDF, Excel, Word o foto letti dall'IA: tu controlli e salvi")]),
   cta()],
   "Scrivi «Squat 5x5 75% 3′» e l'esercizio è pronto. ✍️\nL'editor a righe di VigorLink riconosce serie, ripetizioni, intensità e recupero mentre scrivi. Accanto hai l'ultima volta e il massimale dell'atleta.\n\nQuanto ci metti oggi a scrivere una scheda da zero? 👇"),
 # 1/12
 P("T02_fai_una_domanda", [
   hero("Dentro VigorLink · Analytics", "Chiedilo", "a parole.", "«Chi è fermo da più di 10 giorni?» «Chi ha fatto più record questo mese?»"),
   dev("Fai una domanda", "Scrivi la domanda,", "arriva la risposta.", "Dai dati veri dei tuoi atleti, con il grafico già pronto.", laptop="showcase-pt-ask"),
   lst("Senza fare l'analista", "I tuoi dati,", "in chiaro.", [("Domande in italiano", "niente filtri da imparare"), ("La risposta resta in Home", "se vuoi, la tieni come riquadro"), ("Anche per l'atleta", "sui suoi allenamenti e progressi")]),
   cta()],
   "«Chi è fermo da più di 10 giorni?» Chiedilo a parole. 💬\nIn VigorLink scrivi la domanda in italiano e la risposta arriva dai dati veri dei tuoi atleti, con il grafico già pronto.\n\nQual è la prima domanda che faresti ai tuoi dati? 👇"),
 # 8/12
 P("T03_volume", [
   hero("Dentro VigorLink · il volume", "Quante serie", "per i quadricipiti?", "Lo sai a memoria o lo conti con le dita mentre scrivi la scheda?"),
   dev("Mentre programmi", "Il volume,", "muscolo per muscolo.", "Si aggiorna a ogni esercizio che aggiungi. Sul corpo, non in una tabella.", laptop="showcase-pt-volume"),
   lst("Programmare con criterio", "Vedi subito", "cosa manca.", [("Serie settimanali per gruppo", "contate da sole"), ("Squilibri a colpo d'occhio", "troppo petto, pochi dorsali"), ("Settimana per settimana", "se la scheda cambia nel tempo")]),
   cta()],
   "Quante serie a settimana per i quadricipiti? 🦵\nIn VigorLink il volume si conta da solo mentre scrivi la scheda, muscolo per muscolo, disegnato sul corpo. Gli squilibri li vedi subito.\n\nConti il volume settimanale o vai a occhio? 👇"),
 # 15/12
 P("T04_stampa_pdf", [
   hero("Dentro VigorLink · la stampa", "C'è chi la scheda", "la vuole su carta.", "E va bene così. Ma che sia bella, e con il tuo nome sopra."),
   dev("Stampa e invia", "Sei modelli.", "Il tuo logo.", "Dalla scheda essenziale al registro dei carichi da compilare a penna.", laptop="m-pt-print-modal"),
   lst("In due clic", "Carta o telefono,", "decide il cliente.", [("PDF con il tuo logo", "e i tuoi colori"), ("Lo scarichi o lo mandi in chat", "senza uscire dalla scheda"), ("E nell'app resta tutto", "chi usa il telefono registra le serie come sempre")]),
   cta()],
   "C'è chi la scheda la vuole su carta. E va bene così. 🖨️\nIn VigorLink la stampi in sei modelli, con il tuo logo: dalla scheda essenziale al registro dei carichi da compilare a penna.\n\nQuanti dei tuoi clienti vogliono ancora il foglio? 👇"),
 # 22/12
 P("T05_calendario", [
   hero("Dentro VigorLink · l'agenda", "La settimana,", "in un colpo d'occhio.", "Sedute, lezioni di gruppo, impegni tuoi. Non in tre calendari diversi."),
   dev("Calendario", "Tutto il lavoro", "in un'agenda.", "Appuntamenti con i tuoi atleti, corsi che si ripetono, le tue cose da fare.", laptop="showcase-pt-calendar"),
   lst("E per i tuoi atleti", "Sanno sempre", "quando vi vedete.", [("L'appuntamento è nella loro app", "con ora e luogo"), ("Ferie e disponibilità", "le imposti una volta"), ("Le sedute svolte", "restano nello storico dell'atleta")]),
   cta()],
   "La tua settimana in un colpo d'occhio. 🗓️\nSedute, lezioni di gruppo, impegni tuoi: in VigorLink stanno in un'agenda sola, e ogni atleta vede i suoi appuntamenti nell'app.\n\nDove segni oggi gli appuntamenti con i clienti? 👇"),
 # 29/12
 P("T06_il_tuo_anno", [
   hero("Dentro VigorLink · fine anno", "Un anno", "di allenamenti.", "Quanti chili ha sollevato il tuo atleta nel 2026? Lui non lo sa. L'app sì."),
   dev("Il tuo anno in numeri", "Il suo anno,", "in una schermata.", "Allenamenti, serie, volume, l'esercizio in cui è cresciuto di più.", phone="showcase-athlete-progress"),
   lst("Un regalo che fa da solo", "Lui è fiero.", "Tu sei il suo coach.", [("Un'immagine pronta da condividere", "con i numeri dell'anno"), ("C'è il tuo nome", "accanto ai suoi risultati"), ("Niente dati di salute", "solo allenamenti e progressi")]),
   cta()],
   "Quanti chili ha sollevato il tuo atleta nel 2026? 🏆\nLui non lo sa, l'app sì: «Il tuo anno in numeri» riassume allenamenti, serie e progressi in un'immagine pronta da condividere. Con il tuo nome accanto ai suoi risultati.\n\nQual è stato il progresso più bello di un tuo cliente quest'anno? 👇"),
 # 5/1
 P("T07_progressi", [
   hero("Dentro VigorLink · i progressi", "«Sto migliorando?»", "Fagli vedere di sì.", "A gennaio la motivazione è alta. A marzo servono i numeri."),
   dev("Progressi dell'atleta", "I suoi numeri,", "sempre in tasca.", "Carico di lavoro, serie a settimana, intensità media: aggiornati a ogni allenamento.", phone="showcase-athlete-progress"),
   lst("Quello che lo fa restare", "Vedere", "che funziona.", [("Carichi esercizio per esercizio", "con l'andamento nel tempo"), ("I record", "segnati da soli nel Player"), ("Peso e misure", "se decide di tenerne traccia")]),
   cta()],
   "«Sto migliorando?» Fagli vedere di sì. 📈\nIn VigorLink l'atleta ha i suoi numeri sempre in tasca: carico di lavoro, serie a settimana, record. Aggiornati a ogni allenamento.\n\nCome mostri oggi i progressi ai tuoi clienti? 👇"),
 # 12/1
 P("T08_home_su_misura", [
   hero("Dentro VigorLink · la Home", "Ognuno lavora", "a modo suo.", "C'è chi guarda prima i conti, chi gli allenamenti, chi i messaggi."),
   dev("Personalizza", "La Home", "la costruisci tu.", "Fatta di riquadri: tieni quelli che ti servono, nell'ordine che vuoi.", laptop="m-pt-home-customize"),
   lst("Tua, davvero", "Sposti, allarghi,", "nascondi.", [("Vale anche per Analytics e Finance", "stessi riquadri, stesse regole"), ("Ti segue su ogni schermo", "computer, tablet e telefono"), ("O parti da un modello", "pronto per il tuo modo di lavorare")]),
   cta()],
   "C'è chi guarda prima i conti, chi gli allenamenti, chi i messaggi. 🧩\nIn VigorLink la Home la costruisci tu: riquadri che sposti, allarghi o nascondi. E la tua disposizione ti segue su computer, tablet e telefono.\n\nQual è la prima cosa che vuoi vedere al mattino? 👇"),
 # 19/1
 P("T09_copilota", [
   hero("Dentro VigorLink · il Copilota", "Lunedì mattina:", "chi sento per primo?", "Venti clienti, cento cose. E qualcuno resta sempre indietro."),
   dev("Copilota della settimana", "Una lista.", "Con il motivo.", "Chi riagganciare, chi ha un pagamento scaduto, chi merita un «bravo».", laptop="m-copilot"),
   lst("L'IA propone, tu decidi", "Niente parte", "da solo.", [("Una bozza di messaggio", "scritta per quell'atleta"), ("La rileggi e la cambi", "con le tue parole"), ("Parte solo quando premi Invia", "sempre a tuo nome")]),
   cta()],
   "Lunedì mattina: chi sento per primo? ☕\nIl Copilota di VigorLink ti prepara la lista della settimana, con il motivo: chi riagganciare, chi ha un pagamento scaduto, chi merita un «bravo». L'IA scrive una bozza, ma il messaggio parte solo quando premi Invia.\n\nCome decidi oggi a chi scrivere? 👇"),
 # 26/1
 P("T10_il_tuo_marchio", [
   hero("Dentro VigorLink · il tuo marchio", "I tuoi clienti", "vedono te.", "Hai costruito un nome. Deve stare sull'app che usano ogni giorno."),
   dev("Aspetto e marchio", "Il tuo logo.", "Il tuo colore.", "Su tutta l'app dei tuoi atleti e sui PDF che consegni.", laptop="m-settings-brand"),
   lst("Professionale, senza grafico", "Lo imposti", "una volta.", [("Logo e colore del tuo studio", "con il contrasto controllato, così si legge sempre"), ("Nell'app dell'atleta", "dalla Home al Player"), ("Sulle schede stampate", "e sui report")]),
   cta()],
   "I tuoi clienti vedono te, non noi. 🎨\nIn VigorLink metti il tuo logo e il tuo colore: compaiono su tutta l'app dei tuoi atleti e sui PDF che consegni.\n\nHai già un logo tuo o lavori con il tuo nome? 👇"),
 # 2/2
 P("T11_team", [
   hero("Dentro VigorLink · lo studio", "Non lavori", "più da solo?", "Un collega, una segreteria, un coach in più. E i dati di tutti in giro."),
   dev("Team", "Ognuno vede", "solo il suo.", "Aggiungi collaboratori e scegli tu i permessi, uno per uno.", laptop="m-settings-team"),
   lst("Per lavorare insieme", "Permessi chiari,", "niente pasticci.", [("Il coach segue i suoi atleti", "quelli che gli assegni tu"), ("Chi gestisce l'agenda", "non vede i dati di salute"), ("I conti li condividi", "solo se vuoi")]),
   cta()],
   "Non lavori più da solo? 👥\nIn VigorLink aggiungi collaboratori e scegli i permessi uno per uno: il coach segue gli atleti che gli assegni, chi gestisce l'agenda non vede i dati di salute, i conti li condividi solo se vuoi.\n\nLavori da solo o in squadra? 👇"),
 # 9/2
 P("T12_fisioterapisti", [
   hero("Dentro VigorLink · fisioterapisti", "Anche per chi", "cura, non solo allena.", "Stessa app, un'altra lingua: pazienti, sedute, valutazioni."),
   dev("Lato fisioterapista", "Il paziente,", "dalla valutazione in poi.", "Valutazioni, esercizi a casa, diario delle sedute e documenti in un posto.", laptop="showcase-physio-patient"),
   dev("Lato paziente", "Il dolore,", "serie per serie.", "Da 0 a 10, senza giudizi automatici: lo leggi tu e decidi tu.", phone="showcase-patient-pain"),
   cta()],
   "VigorLink non è solo per chi allena. 🩺\nPer i fisioterapisti l'app parla di pazienti e sedute: valutazioni, esercizi a casa, diario, consenso al trattamento. Il paziente segna il dolore da 0 a 10 serie per serie, senza giudizi automatici: decide sempre il professionista.\n\nConosci un fisioterapista a cui girarlo? 👇"),
]
