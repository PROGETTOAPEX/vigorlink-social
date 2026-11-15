"""Wednesday (the numbers of the job: carousels, useful without the product) and Thursday (before / after: reels).
The Wednesday sums are worked examples, always presented as examples, never as statistics."""
from lib import *

L = "light"

WED = [
 # 18/11
 P("W00_ora_vera", [
   hero("I conti del PT", "Quanto vale davvero", "una tua ora?", "Il prezzo della seduta non è quello che guadagni all'ora. Facciamo il conto.", bg=L),
   lst("Un esempio", "Seduta da 40 €.", "Ma non dura un'ora.", [("60 minuti in sala", "quelli che il cliente vede e paga"), ("+ 20 minuti che non vede", "scheda, messaggi, spostamenti, incassi"), ("= 80 minuti di lavoro", "per gli stessi 40 €")], bg=L),
   stat("Il conto", "30 €", "all'ora, non 40.", "Un quarto del tuo tempo è lavoro che nessuno paga. Con 20 minuti in meno a cliente, torni a 40.", note="Esempio con numeri tondi: rifallo con i tuoi.", bg=L),
   lst("Dove si recupera", "Tre posti", "da cui partire.", [("Le schede", "modelli da adattare, non fogli bianchi"), ("I messaggi", "risposte pronte per le domande di sempre"), ("Gli incassi", "richieste che partono da sole, non rincorse a mano")], bg=L),
   cta(L)],
   "Quanto vale davvero una tua ora? ⏱️\nSeduta da 40 €, ma per ogni ora in sala ci sono circa 20 minuti che il cliente non vede: scheda, messaggi, spostamenti, incassi. Fanno 30 € l'ora, non 40.\n(È un esempio con numeri tondi: rifallo con i tuoi.)\n\nQuanti minuti «invisibili» hai per ogni cliente? 👇", kind="biz", reel=False),
 # 25/11
 P("W01_cliente_che_resta", [
   hero("I conti del PT", "Un cliente che resta", "vale doppio.", "Prima di cercarne di nuovi, guarda quanto valgono quelli che hai.", bg=L),
   lst("Un esempio", "120 € al mese.", "Due storie diverse.", [("Resta 6 mesi", "720 € in tutto"), ("Resta 12 mesi", "1.440 € in tutto"), ("Stesso cliente, stessa fatica per trovarlo", "cambia solo quanto resta")], bg=L),
   stat("La differenza", "+720 €", "senza un solo cliente nuovo.", "Tenere un cliente sei mesi in più vale quanto trovarne un altro. E costa molto meno tempo.", note="Esempio con numeri tondi.", bg=L),
   lst("Cosa lo fa restare", "Tre cose", "semplici.", [("Vede i suoi progressi", "numeri, non sensazioni"), ("Si sente seguito", "un messaggio quando salta, non dopo un mese"), ("Sa sempre cosa fare", "la scheda aggiornata, in tasca")], bg=L),
   cta(L)],
   "Un cliente che resta vale doppio. 📌\n120 € al mese: se resta 6 mesi sono 720 €, se resta 12 sono 1.440 €. Stesso cliente, stessa fatica per trovarlo.\n\nQuanto restano in media i tuoi clienti? 👇", kind="biz", reel=False),
 # 2/12
 P("W02_alzare_i_prezzi", [
   hero("I conti del PT", "Alzi i prezzi.", "Quanti clienti puoi perdere?", "La paura è perderli tutti. Il conto dice un'altra cosa.", bg=L),
   lst("Un esempio", "20 clienti", "a 100 € al mese.", [("Oggi incassi 2.000 €", "20 × 100"), ("Passi a 110 € e ne perdi uno", "19 × 110 = 2.090 €: guadagni di più, lavorando meno"), ("Ne perdi due", "18 × 110 = 1.980 €: sei quasi pari, con due clienti in meno da seguire")], bg=L),
   stat("La regola", "1 su 11", "con un aumento del 10%.", "È la quota di clienti che puoi perdere restando allo stesso incasso. Con il 20% diventa 1 su 6.", note="Vale a parità di prezzo per tutti: con listini diversi il conto cambia.", bg=L),
   lst("Come dirlo", "Con anticipo,", "senza scuse.", [("Avvisa un mese prima", "per iscritto, con la data"), ("Spiega cosa ricevono", "non cosa ti costa"), ("Tieni il vecchio prezzo a chi vuoi premiare", "ma decidilo tu, non per paura")], bg=L),
   cta(L)],
   "Alzi i prezzi del 10%: quanti clienti puoi permetterti di perdere? 📈\nCon 20 clienti a 100 € incassi 2.000 €. A 110 €, se ne perdi uno incassi 2.090 €. Se ne perdi due, 1.980 €: quasi pari, con due persone in meno da seguire.\n\nQuando hai aggiornato i prezzi l'ultima volta? 👇", kind="biz", reel=False),
 # 9/12
 P("W03_pacchetto_o_mensile", [
   hero("I conti del PT", "Pacchetto", "o abbonamento mensile?", "Non c'è una risposta giusta. Ci sono conseguenze diverse.", bg=L),
   lst("Il pacchetto di sedute", "Chiaro,", "ma a strappi.", [("Pro: incassi prima", "e il cliente sa cosa compra"), ("Contro: ogni fine pacchetto è una trattativa", "e un'occasione per smettere"), ("Attenzione alle scadenze", "decidi prima entro quando va usato")], bg=L),
   lst("L'abbonamento mensile", "Regolare,", "ma va spiegato.", [("Pro: entrate prevedibili", "sai a inizio mese quanto incassi"), ("Contro: «questo mese ho fatto meno»", "serve una regola chiara sulle sedute saltate"), ("Funziona se il valore è continuo", "scheda, chat, controllo: non solo l'ora in sala")], bg=L),
   lst("In pratica", "Molti", "li usano insieme.", [("Mensile per chi segui con continuità", "in presenza o online"), ("Pacchetto per chi viene ogni tanto", "o per provare"), ("In tutti e due i casi", "la data di fine deve saperla anche il cliente")], bg=L),
   cta(L)],
   "Pacchetto di sedute o abbonamento mensile? 🤝\nIl pacchetto è chiaro ma ogni rinnovo è una trattativa. Il mensile è regolare ma serve una regola sulle sedute saltate. Molti li usano insieme.\n\nTu come vendi oggi? 👇", kind="biz", reel=False),
 # 16/12
 P("W04_feste", [
   hero("I conti del PT", "Dicembre:", "tutti spariscono.", "Cene, viaggi, influenza. Poi a gennaio qualcuno non torna.", bg=L),
   lst("Prima delle feste", "Tre mosse", "da fare adesso.", [("Una scheda breve per le vacanze", "20 minuti, a corpo libero, da fare ovunque"), ("L'appuntamento di gennaio già fissato", "chi ha una data torna"), ("Un messaggio personale", "due righe sui suoi progressi dell'anno")], bg=L),
   lst("Durante", "Lasciali", "respirare.", [("Niente sensi di colpa", "una pausa non cancella un anno"), ("Un solo promemoria", "non uno al giorno"), ("Rispondi se scrivono", "ma non inseguire")], bg=L),
   stat("Il punto", "1 data", "vale più di dieci messaggi.", "Chi esce dalla tua palestra a dicembre con il prossimo appuntamento in agenda ha già deciso di tornare.", bg=L, vsize=200),
   cta(L)],
   "Dicembre: tutti spariscono. E a gennaio qualcuno non torna. 🎄\nTre mosse da fare adesso: una scheda breve per le vacanze, l'appuntamento di gennaio già fissato, due righe personali sui progressi dell'anno.\n\nCome gestisci le settimane di festa con i tuoi clienti? 👇", kind="biz", reel=False),
 # 23/12
 P("W05_cinque_numeri_anno", [
   hero("I conti del PT", "Il tuo 2026", "in cinque numeri.", "Prima dei buoni propositi, guarda com'è andata davvero.", bg=L),
   lst("I primi tre", "Quanto", "e da chi.", [("Incassato dell'anno", "non il fatturato: quello che è entrato"), ("Clienti attivi a dicembre", "confrontati con gennaio"), ("Incasso medio per cliente", "ti dice se lavori tanto o lavori bene")], bg=L),
   lst("Gli altri due", "Quanto restano,", "quanto costano.", [("Permanenza media", "dal primo all'ultimo mese pagato"), ("Uscite dell'anno", "affitto sala, attrezzi, corsi, software, assicurazione"), ("E poi il risultato", "incassi meno uscite, prima delle tasse")], bg=L),
   stat("Il consiglio", "30 min", "prima di Capodanno.", "Mezz'ora con questi cinque numeri vale più di qualsiasi lista di propositi.", bg=L, vsize=190),
   cta(L)],
   "Il tuo 2026 in cinque numeri. 🧮\nIncassato, clienti attivi, incasso medio per cliente, permanenza media, uscite. Mezz'ora prima di Capodanno con questi numeri vale più di qualsiasi lista di propositi.\n\nQuale di questi cinque conosci già a memoria? 👇", kind="biz", reel=False),
 # 30/12
 P("W06_obiettivi_2027", [
   hero("I conti del PT", "2027:", "tre obiettivi, non trenta.", "«Crescere» non è un obiettivo. Un numero e una data sì.", bg=L),
   lst("Scegline tre", "Uno per", "ogni domanda.", [("Quanto voglio incassare al mese?", "un numero, entro una data"), ("Quanti clienti voglio seguire?", "non il massimo: quelli che segui bene"), ("Quante ore voglio lavorare?", "è il numero che dimentichiamo tutti")], bg=L),
   lst("Poi fai il conto", "I tre numeri", "devono stare insieme.", [("Incasso ÷ clienti", "è il prezzo medio che ti serve"), ("Clienti × tempo per ciascuno", "sono le ore che ti servono"), ("Se non torna", "cambi il prezzo, non le ore di sonno")], bg=L),
   cta(L)],
   "2027: tre obiettivi, non trenta. 🎯\nQuanto vuoi incassare al mese, quanti clienti vuoi seguire, quante ore vuoi lavorare. Poi fai il conto: i tre numeri devono stare insieme.\n\nQual è il tuo numero per il 2027? 👇", kind="biz", reel=False),
 # 6/1
 P("W07_gennaio_marzo", [
   hero("I conti del PT", "Gennaio pieno.", "Marzo vuoto?", "I clienti di gennaio non si perdono a marzo. Si perdono nelle prime tre settimane.", bg=L),
   lst("Le prime tre settimane", "Dove si decide", "tutto.", [("Settimana 1: una vittoria facile", "una scheda che riesce a finire"), ("Settimana 2: un controllo", "«com'è andata?» prima che lo chieda lui"), ("Settimana 3: un numero", "un carico salito, una serie in più: fagli vedere che funziona")], bg=L),
   lst("I segnali", "Chi sta", "per mollare.", [("Salta la seconda settimana", "non la decima"), ("Risponde a monosillabi", "o non risponde"), ("Sposta gli appuntamenti", "sempre più in là")], bg=L),
   stat("Il punto", "21 giorni", "per farlo diventare un'abitudine tua.", "Non sua: tua. Tre contatti nelle prime tre settimane, con ogni cliente nuovo.", bg=L, vsize=170),
   cta(L)],
   "Gennaio pieno. Marzo vuoto? 📉\nI clienti di gennaio non si perdono a marzo: si perdono nelle prime tre settimane. Una vittoria facile, un controllo, un numero che sale.\n\nQuanti dei tuoi clienti di gennaio scorso sono ancora con te? 👇", kind="biz", reel=False),
 # 13/1
 P("W08_quanti_clienti", [
   hero("I conti del PT", "Quanti clienti", "ti servono davvero?", "Di solito meno di quelli che pensi. Dipende da un solo numero.", bg=L),
   lst("Un esempio", "Obiettivo:", "2.500 € al mese.", [("A 100 € a cliente", "ne servono 25"), ("A 150 € a cliente", "ne servono 17"), ("A 200 € a cliente", "ne servono 13")], bg=L),
   stat("La differenza", "12", "clienti in meno, stesso incasso.", "Tra 100 e 200 € a cliente c'è metà del lavoro. Il prezzo medio conta più del numero di clienti.", note="Incassi lordi, prima di tasse e spese.", bg=L),
   lst("Come si alza il prezzo medio", "Non solo", "aumentando.", [("Percorsi, non sedute singole", "tre mesi con un obiettivo"), ("Online accanto alla presenza", "scheda e controllo per chi non può venire"), ("Meno sconti «per simpatia»", "contali: a fine anno sono un cliente intero")], bg=L),
   cta(L)],
   "Quanti clienti ti servono davvero? 🔢\nPer 2.500 € al mese: 25 clienti a 100 €, 17 a 150 €, 13 a 200 €. Il prezzo medio conta più del numero di clienti.\n\nQual è oggi il tuo incasso medio per cliente? 👇", kind="biz", reel=False),
 # 20/1
 P("W09_costo_di_una_disdetta", [
   hero("I conti del PT", "Quanto ti costa", "un cliente che disdice?", "Non solo il mese dopo. Fai il conto su un anno.", bg=L),
   lst("Un esempio", "Cliente", "da 120 € al mese.", [("Quello che non incassi", "1.440 € in un anno"), ("Il tempo per sostituirlo", "prove gratuite, messaggi, primo colloquio"), ("Quello che non vedi", "il passaparola che non farà")], bg=L),
   lst("Perché se ne vanno", "Quasi mai", "per il prezzo.", [("Non vedono risultati", "o non glieli hai mostrati"), ("Si sentono uno dei tanti", "stessa scheda, nessun messaggio"), ("La vita cambia", "lavoro, trasloco, infortunio: lì puoi solo lasciare la porta aperta")], bg=L),
   stat("Il punto", "1 messaggio", "al momento giusto.", "Costa due minuti. Scrivere a chi ha saltato una settimana è il lavoro più redditizio che fai.", bg=L, vsize=150),
   cta(L)],
   "Quanto ti costa un cliente che disdice? 💸\n120 € al mese sono 1.440 € in un anno, più il tempo per trovarne un altro. E quasi mai se ne vanno per il prezzo.\n\nQual è il motivo che senti più spesso quando un cliente smette? 👇", kind="biz", reel=False),
 # 27/1
 P("W10_lezione_saltata", [
   hero("I conti del PT", "«Scusa, oggi", "non riesco a venire.»", "Alle 17:40, per la seduta delle 18. Chi la paga?", bg=L),
   lst("Serve una regola", "Scritta,", "prima che serva.", [("Disdetta entro 24 ore", "la seduta si recupera"), ("Dopo le 24 ore", "la seduta è persa, salvo emergenze vere"), ("Una eccezione all'anno", "la decidi tu, e la dici")], bg=L),
   lst("Come farla rispettare", "Senza fare", "il cattivo.", [("Falla leggere all'inizio", "non la prima volta che succede"), ("Uguale per tutti", "anche per il cliente simpatico"), ("Il promemoria il giorno prima", "toglie metà delle disdette")], bg=L),
   stat("Il conto", "1 a settimana", "sono più di 50 sedute l'anno.", "Una seduta saltata e non pagata ogni settimana: a 40 € sono oltre 2.000 € in un anno.", note="Esempio con numeri tondi.", bg=L, vsize=120),
   cta(L)],
   "«Scusa, oggi non riesco a venire.» Alle 17:40, per le 18. 🙄\nServe una regola scritta prima che serva: disdetta entro 24 ore si recupera, dopo è persa. Uguale per tutti.\n\nTu ce l'hai una regola sulle disdette? 👇", kind="biz", reel=False),
 # 3/2
 P("W11_online_presenza", [
   hero("I conti del PT", "In presenza,", "online o tutti e due?", "Non è una questione di moda. È una questione di ore.", bg=L),
   lst("In presenza", "Vale di più,", "ma ha un tetto.", [("Prezzo più alto a seduta", "il cliente paga la tua attenzione"), ("Il tetto sono le tue ore", "più di tante non ne hai"), ("Spostamenti e sala", "sono costi, contali")], bg=L),
   lst("Online", "Vale meno,", "ma non ha orari.", [("Prezzo più basso", "ma niente sala e niente viaggi"), ("Funziona se il controllo è vero", "scheda aggiornata, risposte, numeri guardati"), ("Il rischio", "che diventi un PDF mandato una volta al mese")], bg=L),
   lst("Tutti e due", "Per molti", "è la risposta.", [("Presenza per chi inizia", "tecnica e fiducia"), ("Online per chi è autonomo", "o si trasferisce: così non lo perdi"), ("Una seduta al mese in presenza", "tiene vivo anche il percorso online")], bg=L),
   cta(L)],
   "In presenza, online o tutti e due? 🖥️\nLa presenza vale di più ma il tetto sono le tue ore. L'online vale meno ma non ha orari, se il controllo è vero. Per molti la risposta è tutti e due.\n\nTu come lavori oggi? 👇", kind="biz", reel=False),
 # 10/2
 P("W12_tempo_per_scheda", [
   hero("I conti del PT", "Quanto tempo", "ti costa ogni scheda?", "Mezz'ora sembra poco. Moltiplicala.", bg=L),
   lst("Un esempio", "20 clienti.", "Scheda nuova ogni 6 settimane.", [("30 minuti a scheda", "10 ore per ogni giro"), ("Quasi 9 giri in un anno", "52 settimane ÷ 6"), ("Totale", "quasi 90 ore l'anno")], bg=L),
   stat("Il conto", "90 ore", "più di due settimane di lavoro.", "Ogni anno, solo per scrivere schede. Dimezzare il tempo a scheda vuol dire riprendersi una settimana.", note="Esempio con numeri tondi: rifallo con i tuoi.", bg=L),
   lst("Dove si dimezza", "Non scrivendo", "più in fretta.", [("Modelli per obiettivo", "si adatta, non si riscrive"), ("I numeri dell'atleta davanti", "l'ultima volta, i massimali"), ("Blocchi da riusare", "riscaldamenti, circuiti, finali")], bg=L),
   cta(L)],
   "Quanto tempo ti costa ogni scheda? ⏳\n20 clienti, scheda nuova ogni 6 settimane, 30 minuti l'una: quasi 90 ore l'anno. Più di due settimane di lavoro.\n\nQuanto ci metti tu per una scheda? 👇", kind="biz", reel=False),
]

THU = [
 # 19/11
 P("H00_scheda_pdf_vs_app", [
   hero("Prima e dopo", "La scheda.", "PDF o app?", "Stessa programmazione, due vite molto diverse."),
   split("La scheda", "Senza", "e con.", ["PDF su WhatsApp, perso tra i messaggi", "I carichi scritti a penna, se va bene", "Tu non sai se l'ha aperta"], ["Sempre in tasca, aggiornata", "Carico consigliato e record automatici", "Vedi ogni serie registrata"]),
   dev("Lato atleta", "La apre", "e si allena.", "La giornata di oggi, le serie da fare, il recupero che parte da solo.", phone="showcase-athlete-workout"),
   cta()],
   "La scheda: PDF su WhatsApp o app? 📄→📱\nStessa programmazione, due vite diverse. Nel PDF i carichi sono a penna e tu non sai se l'ha aperta. Nell'app la scheda è sempre aggiornata, con carico consigliato, record automatici e ogni serie registrata.\n\nDa che parte sei oggi? 👇"),
 # 26/11
 P("H01_pagamenti", [
   hero("Prima e dopo", "Farsi pagare.", "Senza imbarazzo.", "Il momento più scomodo del mestiere non deve esserlo."),
   split("I pagamenti", "Senza", "e con.", ["«Ti ricordi il bonifico?» in chat", "Un foglio per segnare chi ha pagato", "Il cliente non sa cosa ha pagato"], ["La richiesta arriva nell'app", "Pagati e scaduti in una lista", "Il cliente vede tutto dal telefono"], note="VigorLink non trattiene nulla: restano solo le commissioni del metodo che usi."),
   dev("Lato atleta", "Paga", "dal telefono.", "Con il metodo che hai scelto tu: carta, bonifico, PayPal, Satispay, SumUp.", phone="m-athlete-payments"),
   cta()],
   "Farsi pagare senza imbarazzo. 💳\nPrima: «ti ricordi il bonifico?» in chat. Dopo: la richiesta arriva nell'app, il cliente paga dal telefono con il metodo che scegli tu, e tu vedi pagati e scaduti in una lista.\n\nQual è la parte più scomoda del farsi pagare? 👇"),
 # 3/12
 P("H02_nuovo_cliente", [
   hero("Prima e dopo", "Arriva", "un cliente nuovo.", "Il primo giorno decide come andranno i prossimi sei mesi."),
   split("Il primo giorno", "Senza", "e con.", ["Moduli di carta da firmare e conservare", "Anamnesi su un foglio, poi chissà dove", "«Ti mando la scheda appena riesco»"], ["Lo inviti con un link, sceglie la password", "Consensi e questionario compilati nell'app", "La scheda è sul suo telefono"]),
   lst("E per te", "Tutto", "al suo posto.", [("I consensi sono registrati", "con la data, senza cartelline"), ("Le risposte del questionario", "nella scheda dell'atleta"), ("Niente da installare dagli store", "si apre dal browser e si aggiunge alla Home")]),
   cta()],
   "Arriva un cliente nuovo. 🙌\nPrima: moduli di carta, anamnesi su un foglio, «ti mando la scheda appena riesco». Dopo: lo inviti con un link, consensi e questionario li compila nell'app, la scheda è già sul suo telefono.\n\nQuanto dura oggi il tuo «primo giorno» con un cliente? 👇"),
 # 10/12
 P("H03_lunedi_mattina", [
   hero("Prima e dopo", "Lunedì,", "ore 8:00.", "La settimana comincia. Da dove?"),
   split("Il lunedì mattina", "Senza", "e con.", ["WhatsApp, Excel, agenda, banca, note", "Scorri le chat per capire chi è fermo", "Ti ricordi di qualcuno giovedì"], ["Una Home con quello che conta oggi", "«Hanno bisogno di te», con il motivo", "Appuntamenti e cose da fare nello stesso posto"]),
   dev("Lato PT", "Apri", "e sai cosa fare.", "Chi si allena, chi si è fermato, chi ti aspetta.", laptop="showcase-pt-athletes"),
   cta()],
   "Lunedì, ore 8:00. Da dove cominci? ☕\nPrima: WhatsApp, Excel, agenda, banca, note. Dopo: una Home con quello che conta oggi e la lista «Hanno bisogno di te».\n\nQuante app apri il lunedì mattina prima di iniziare? 👇"),
 # 17/12
 P("H04_programmare_settimane", [
   hero("Prima e dopo", "Programmare", "otto settimane.", "Progressioni, scarichi, variazioni. In Excel è un lavoro a parte."),
   split("Un blocco di più settimane", "Senza", "e con.", ["Copia e incolla di otto fogli", "Una modifica da ripetere otto volte", "Il cliente guarda il foglio sbagliato"], ["Un piano a settimane nella stessa scheda", "Cambi una settimana, le altre restano", "L'atleta vede solo la settimana giusta"]),
   dev("Lato PT", "Settimana", "per settimana.", "Serie, ripetizioni e intensità che cambiano nel tempo, in una sola scheda.", laptop="m-pt-editor-weeks"),
   cta()],
   "Programmare otto settimane. 📆\nPrima: otto fogli Excel e una modifica da ripetere otto volte. Dopo: un piano a settimane nella stessa scheda, e l'atleta vede solo la settimana giusta.\n\nProgrammi a blocchi o settimana per settimana? 👇"),
 # 24/12
 P("H05_buone_feste", [
   hero("24 dicembre", "Oggi", "si recupera.", "Anche il recupero è allenamento. Vale per i tuoi clienti, vale per te."),
   hero("Da VigorLink", "Buone feste,", "coach.", "Grazie a chi ci ha scritto, seguito e messo alla prova in questi mesi. Ci vediamo nel 2027."),
   cta()],
   "Oggi si recupera. 🎄\nAnche il recupero è allenamento: vale per i tuoi clienti, vale per te. Buone feste da VigorLink, e grazie a chi ci ha scritto, seguito e messo alla prova in questi mesi.\n\nCome passi le feste: riposo vero o allenamento lo stesso? 👇"),
 # 31/12
 P("H06_ultimo_giorno", [
   hero("31 dicembre", "L'anno prossimo", "meno carta.", "Un solo proposito, facile da mantenere."),
   split("Il lavoro del PT", "Nel 2026", "e nel 2027.", ["Schede in PDF e carichi a penna", "Pagamenti rincorsi in chat", "Conti a fine mese, a memoria"], ["Schede nell'app, serie registrate", "Richieste di pagamento dal telefono", "Incassi e scadenze in un posto"]),
   hero("Da VigorLink", "Buon anno,", "coach.", "Nel 2027 arriviamo anche noi. Chi è in lista lo saprà per primo."),
   cta()],
   "L'anno prossimo meno carta. 🥂\nUn solo proposito per il 2027: schede nell'app, pagamenti dal telefono, conti in un posto. Buon anno da VigorLink.\n\nQual è il tuo proposito di lavoro per il 2027? 👇"),
 # 7/1
 P("H07_fine_mese", [
   hero("Prima e dopo", "Fine mese:", "si fanno i conti.", "O meglio: si dovrebbero fare."),
   split("I conti del mese", "Senza", "e con.", ["Estratto conto, fatture e appunti da incrociare", "Scopri a fine mese com'è andata", "Le spese fisse le sai «più o meno»"], ["Incassi e uscite già al loro posto", "L'andamento lo vedi durante il mese", "Le spese che si ripetono si segnano da sole"], note="Finance serve per capire e decidere: la contabilità ufficiale resta al commercialista."),
   dev("Finance", "Com'è andata,", "senza aspettare.", "Incassato, da incassare, risultato degli ultimi dodici mesi.", laptop="showcase-pt-finance-1511"),
   cta()],
   "Fine mese: si fanno i conti. O si dovrebbero. 🧾\nPrima: estratto conto, fatture e appunti da incrociare. Dopo: incassi e uscite già al loro posto, e l'andamento lo vedi durante il mese.\n\nOgni quanto guardi davvero i tuoi conti? 👇", kind="biz"),
 # 14/1
 P("H08_messaggi", [
   hero("Prima e dopo", "I messaggi", "dei clienti.", "Ore 22:30, WhatsApp: «Coach una domanda veloce…»"),
   split("La chat con i clienti", "Senza", "e con.", ["Clienti, amici e famiglia nella stessa app", "Il tuo numero personale a tutti", "La domanda di martedì persa tra le foto"], ["Una chat solo per il lavoro", "Scrivono dall'app, non al tuo numero", "Messaggi e allenamenti dello stesso atleta insieme"]),
   dev("Lato atleta", "Ti scrive", "da dove si allena.", "La chat con il coach è nella sua app, accanto alla scheda.", phone="showcase-athlete-chat"),
   cta()],
   "Ore 22:30, WhatsApp: «Coach una domanda veloce…» 📲\nPrima: clienti, amici e famiglia nella stessa app, con il tuo numero personale. Dopo: una chat solo per il lavoro, accanto alle schede.\n\nI tuoi clienti hanno il tuo numero personale? 👇"),
 # 21/1
 P("H09_come_e_andata", [
   hero("Prima e dopo", "«Com'è andato", "l'allenamento?»", "«Bene.» Fine della conversazione."),
   split("Sapere com'è andata", "Senza", "e con.", ["Ti fidi di un «bene»", "I carichi li sa solo lui, forse", "Te ne accorgi al prossimo incontro"], ["Durata, serie, volume, fatica percepita", "Ogni serie con kg e ripetizioni", "La nota che ha lasciato a fine allenamento"]),
   dev("Lato PT", "L'allenamento,", "serie per serie.", "Apri la sessione e vedi cosa ha fatto davvero.", laptop="m-pt-session-detail"),
   cta()],
   "«Com'è andato l'allenamento?» «Bene.» 😶\nPrima: ti fidi di un «bene». Dopo: apri la sessione e vedi durata, serie, kg, ripetizioni, fatica percepita e la nota che ha lasciato.\n\nQuanto sai davvero degli allenamenti che i tuoi clienti fanno da soli? 👇"),
 # 28/1
 P("H10_pausa", [
   hero("Prima e dopo", "Il cliente", "va in vacanza.", "O si fa male, o ha un mese impossibile al lavoro. Capita."),
   split("Una pausa", "Senza", "e con.", ["Promemoria che arrivano lo stesso", "Risulta «fermo» anche se è d'accordo con te", "Al rientro non sai da dove ripartire"], ["Mette l'app in pausa per quel periodo", "Niente promemoria finché è via", "Scheda e storico lo aspettano"]),
   lst("E quando torna", "Si riparte", "da dove era.", [("I carichi dell'ultima volta", "sono ancora lì"), ("I progressi non si azzerano", "lo storico resta"), ("Tu sai quando rientra", "e puoi preparare la scheda")]),
   cta()],
   "Il cliente va in vacanza. O ha un mese impossibile. 🏖️\nPrima: promemoria che arrivano lo stesso e nessuna idea di dove ripartire. Dopo: mette l'app in pausa, niente promemoria, e scheda e storico lo aspettano.\n\nCome gestisci oggi le pause dei tuoi clienti? 👇"),
 # 4/2
 P("H11_collaboratori", [
   hero("Prima e dopo", "Lo studio", "cresce.", "Arriva un collaboratore. E con lui i conti di fine mese."),
   split("Lavorare in squadra", "Senza", "e con.", ["Tutti vedono tutto, o nessuno vede niente", "Sedute contate a mano a fine mese", "Schede e clienti in file diversi"], ["Permessi scelti persona per persona", "Compensi calcolati dalle sedute svolte", "Atleti assegnati a ciascun coach"]),
   lst("Con giudizio", "Ognuno", "il suo.", [("Il coach vede i suoi atleti", "non i conti dello studio"), ("La segreteria gestisce l'agenda", "senza vedere i dati di salute"), ("Tu vedi l'insieme", "e decidi cosa condividere")]),
   cta()],
   "Lo studio cresce: arriva un collaboratore. 👥\nPrima: tutti vedono tutto, e le sedute si contano a mano a fine mese. Dopo: permessi scelti persona per persona, atleti assegnati a ciascun coach, compensi calcolati dalle sedute svolte.\n\nLavori da solo o con qualcuno? 👇"),
 # 11/2
 P("H12_cinque_strumenti", [
   hero("Prima e dopo", "Cinque strumenti.", "O uno.", "Fai il conto di quante app apri per seguire un solo cliente."),
   split("Il tuo banco di lavoro", "Senza", "e con.", ["Excel o PDF per le schede", "WhatsApp per i messaggi", "Agenda, banca e foglio dei conti"], ["Schede, con le serie registrate", "Chat, agenda e pagamenti", "Incassi e scadenze, nello stesso posto"]),
   lst("Per chi", "Un'app,", "tre persone.", [("Per te", "atleti, schede, agenda, messaggi e conti"), ("Per il tuo atleta", "l'allenamento del giorno sul telefono"), ("Per il tuo team", "ognuno con i suoi permessi")]),
   cta()],
   "Cinque strumenti. O uno. 🧰\nExcel per le schede, WhatsApp per i messaggi, agenda, banca, foglio dei conti. Con VigorLink atleti, schede, agenda, messaggi e conti stanno in un posto solo.\n\nQuante app usi oggi per seguire un cliente? 👇"),
]
