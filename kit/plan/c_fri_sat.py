"""Friday (true or false: training myths) and Saturday (lists to save). Carousels, useful without the product.
The quiz answers stay inside what is broadly agreed in exercise science; where the evidence is mixed the verdict says so."""
from lib import *

L = "light"

def quiz(pid, kicker, a, b, verdict, label, why, points, cap, vsize=None):
    return P(pid, [
        hero(kicker, a, b, "Lo senti dire in palestra ogni settimana. Scorri per la risposta."),
        stat("La risposta", verdict, label, why, vsize=vsize),
        lst("Come spiegarlo al cliente", "In tre", "frasi.", points),
        cta()], cap, kind="quiz", reel=False)

FRI = [
 # 20/11
 quiz("F00_muscolo_grasso", "Vero o falso?", "«Se smetti, il muscolo", "diventa grasso.»", "FALSO", "Sono due tessuti diversi.",
      "Un tessuto non si trasforma nell'altro. Se smetti di allenarti il muscolo si riduce; il grasso aumenta solo se mangi più di quanto consumi.",
      [("Il muscolo non «diventa» niente", "senza stimolo, piano piano si riduce"), ("Il grasso dipende dal bilancio", "quanto mangi e quanto ti muovi"), ("Spesso succedono insieme", "per questo sembra una trasformazione")],
      "Vero o falso: «se smetti di allenarti, il muscolo diventa grasso»? 🤔\nScrivi la tua risposta nei commenti, poi scorri.\n\nQual è il mito che senti più spesso in palestra? 👇"),
 # 27/11
 quiz("F01_sudare", "Vero o falso?", "«Più sudi,", "più dimagrisci.»", "FALSO", "Il sudore è acqua, non grasso.",
      "Sudare serve a raffreddare il corpo. Il peso che perdi in una seduta molto sudata torna appena bevi.",
      [("Il sudore regola la temperatura", "dipende da caldo, umidità, vestiti e genetica"), ("La bilancia dopo l'allenamento", "misura l'acqua persa"), ("Allenarsi coperti per sudare di più", "fa solo rendere meno")],
      "Vero o falso: «più sudi, più dimagrisci»? 💦\nRisposta nei commenti, poi scorri.\n\nHai ancora clienti che si allenano con il k-way? 👇"),
 # 4/12
 quiz("F02_localizzato", "Vero o falso?", "«Gli addominali", "sciolgono la pancia.»", "FALSO", "Il dimagrimento localizzato non esiste.",
      "Allenare una zona rinforza quel muscolo, ma il corpo non prende il grasso proprio da lì. Dove cala prima dipende soprattutto dalla genetica.",
      [("Gli addominali si allenano", "ma si vedono quando cala il grasso di tutto il corpo"), ("Il grasso cala in generale", "con alimentazione, movimento e tempo"), ("L'ordine lo decide il corpo", "non l'esercizio")],
      "Vero o falso: «con gli addominali va via la pancia»? 🎯\nRisposta nei commenti, poi scorri.\n\nQuante volte te l'hanno chiesto questo mese? 👇"),
 # 11/12
 quiz("F03_doms", "Vero o falso?", "«Se non hai dolori,", "non ti sei allenato bene.»", "FALSO", "I dolori non misurano la qualità.",
      "L'indolenzimento del giorno dopo arriva soprattutto con stimoli nuovi o insoliti. Chi si allena con regolarità ne ha meno e migliora lo stesso.",
      [("I dolori dicono «era nuovo»", "non «era efficace»"), ("I progressi si misurano", "con carichi, ripetizioni e costanza"), ("Cercare il dolore a ogni seduta", "è il modo più rapido per saltare la successiva")],
      "Vero o falso: «se il giorno dopo non hai dolori, non ti sei allenato bene»? 😖\nRisposta nei commenti, poi scorri.\n\nI tuoi clienti misurano l'allenamento dai dolori? 👇"),
 # 18/12
 quiz("F04_donne_pesi", "Vero o falso?", "«Con i pesi", "le donne diventano grosse.»", "FALSO", "Costruire muscolo è lento per tutti.",
      "Aumentare molto la massa muscolare richiede anni di allenamento mirato e un'alimentazione dedicata. Non succede per caso con due sedute a settimana.",
      [("La forza arriva prima del volume", "nei primi mesi si diventa più forti, non più grossi"), ("Il muscolo occupa meno spazio del grasso", "a parità di peso"), ("I pesi fanno bene anche alle ossa", "a ogni età")],
      "Vero o falso: «con i pesi le donne diventano grosse»? 🏋️‍♀️\nRisposta nei commenti, poi scorri.\n\nÈ una paura che senti ancora tra le tue clienti? 👇"),
 # 8/1
 quiz("F05_stretching", "Vero o falso?", "«Lo stretching prima", "evita gli infortuni.»", "NON È DIMOSTRATO", "Meglio un riscaldamento attivo.",
      "Gli studi non mostrano che lo stretching statico prima dell'allenamento, da solo, riduca gli infortuni. Un riscaldamento progressivo e specifico prepara meglio.",
      [("Prima: muoviti", "mobilità e serie leggere dell'esercizio che farai"), ("Lo stretching statico ha il suo posto", "per la flessibilità, in altri momenti"), ("Gli infortuni dipendono da molte cose", "carico, recupero, tecnica")], vsize=96,
      cap="Vero o falso: «lo stretching prima dell'allenamento evita gli infortuni»? 🧘\nRisposta nei commenti, poi scorri.\n\nCome fai riscaldare i tuoi clienti? 👇"),
 # 15/1
 quiz("F06_piu_e_meglio", "Vero o falso?", "«Più ti alleni,", "più migliori. Sempre.»", "FALSO", "Si migliora nel recupero.",
      "L'allenamento dà lo stimolo; l'adattamento avviene dopo, con riposo, sonno e alimentazione. Oltre un certo punto, aggiungere peggiora.",
      [("Lo stimolo serve", "ma è il recupero che ti fa migliorare"), ("Più volume funziona", "finché riesci a recuperarlo"), ("I segnali del troppo", "carichi che calano, sonno peggiore, voglia zero")],
      "Vero o falso: «più ti alleni, più migliori. Sempre»? 🔁\nRisposta nei commenti, poi scorri.\n\nA gennaio quanti dei tuoi clienti vogliono allenarsi tutti i giorni? 👇"),
 # 22/1
 quiz("F07_confondere_muscolo", "Vero o falso?", "«Bisogna confondere", "il muscolo.»", "FALSO", "Il muscolo non si confonde: si adatta.",
      "Si cresce aumentando lo stimolo nel tempo sugli stessi movimenti. Cambiare esercizi ogni settimana impedisce di capire se stai migliorando.",
      [("Serve progressione", "un po' più di carico o di ripetizioni, con calma"), ("Variare ha senso", "ogni tanto, per un motivo"), ("Se cambi tutto sempre", "non hai più un numero da confrontare")],
      "Vero o falso: «bisogna cambiare esercizi spesso per confondere il muscolo»? 🌀\nRisposta nei commenti, poi scorri.\n\nOgni quanto cambi la scheda ai tuoi clienti? 👇"),
 # 29/1
 quiz("F08_carboidrati_sera", "Vero o falso?", "«I carboidrati la sera", "fanno ingrassare.»", "FALSO", "Conta il totale, non l'orario.",
      "Per il peso conta soprattutto quanto si mangia nell'arco della giornata e della settimana, non l'ora in cui lo si mangia.",
      [("L'orologio conta poco", "conta il totale di giornate e settimane"), ("La sera spesso si mangia di più", "per questo sembra colpa dell'orario"), ("Per un piano alimentare", "c'è il nutrizionista: noi alleniamo")],
      "Vero o falso: «i carboidrati la sera fanno ingrassare»? 🍝\nRisposta nei commenti, poi scorri.\n\nQual è la domanda sull'alimentazione che ti fanno più spesso? 👇"),
 # 5/2
 quiz("F09_squat_profondo", "Vero o falso?", "«Lo squat profondo", "rovina le ginocchia.»", "FALSO", "Per ginocchia sane, con tecnica e carico adatti.",
      "In persone senza problemi articolari lo squat completo, eseguito bene e con carichi progressivi, non risulta dannoso. Con dolore o patologie si valuta caso per caso.",
      [("La profondità si costruisce", "con mobilità, controllo e carichi graduali"), ("Il problema è quasi sempre il come", "fretta, carico eccessivo, tecnica"), ("Se c'è dolore", "ci si ferma e si sente un professionista sanitario")],
      cap="Vero o falso: «lo squat profondo rovina le ginocchia»? 🦵\nRisposta nei commenti, poi scorri.\n\nFai fare lo squat completo ai tuoi clienti? 👇"),
 # 12/2
 quiz("F10_ogni_giorno", "Vero o falso?", "«Per avere risultati", "devi allenarti ogni giorno.»", "FALSO", "Conta la costanza, non il calendario pieno.",
      "Due o tre sedute a settimana fatte bene, per mesi, portano più lontano di sette sedute per tre settimane e poi niente.",
      [("Meglio poco e sempre", "che tanto e per poco"), ("Il piano giusto", "è quello che riesce a seguire davvero"), ("I giorni di riposo", "fanno parte della scheda")],
      "Vero o falso: «per avere risultati devi allenarti ogni giorno»? 📅\nRisposta nei commenti, poi scorri.\n\nQuante sedute a settimana consigli a chi inizia? 👇"),
]

def lista(pid, a, b, body, k1, t1a, t1b, items1, k2, t2a, t2b, items2, cap):
    return P(pid, [
        hero("Da salvare 🔖", a, b, body, bg=L),
        lst(k1, t1a, t1b, items1, bg=L),
        lst(k2, t2a, t2b, items2, bg=L),
        cta(L)], cap, kind="list", reel=False)

SAT = [
 # 21/11
 lista("S00_far_usare_app", "5 modi per far usare", "davvero l'app ai clienti.", "Valgono con qualsiasi app. Il primo giorno conta più di tutti gli altri.",
       "I primi tre", "Il primo", "allenamento.", [("Installatela insieme", "dal vivo, non «ti mando il link»"), ("Fate insieme la prima serie", "così sa dove toccare"), ("Spiega perché ti serve", "«così vedo i tuoi carichi e ti seguo meglio»")],
       "Gli altri due", "Le prime", "due settimane.", [("Commenta quello che registra", "un messaggio sul suo allenamento: capisce che guardi"), ("Niente doppio canale", "se la scheda è nell'app, non mandarla anche in PDF"), ("Bonus: festeggia il primo record", "è il momento in cui l'app diventa sua")],
       "5 modi per far usare davvero l'app ai tuoi clienti. 🔖 Salvalo.\nValgono con qualsiasi app: installatela insieme, fate insieme la prima serie, commenta quello che registra.\n\nQual è il tuo numero 6? 👇"),
 # 28/11
 lista("S01_primo_incontro", "6 domande", "per il primo incontro.", "Oltre a peso, altezza e obiettivo. Quelle che ti dicono se resterà.",
       "Le prime tre", "Capire", "la persona.", [("Cosa hai già provato, e perché hai smesso?", "ti dice cosa non ripetere"), ("Com'è una tua settimana normale?", "orari veri, non quelli ideali"), ("Cosa vuol dire per te «in forma»?", "ognuno ha la sua immagine")],
       "Le altre tre", "Capire", "il percorso.", [("Quante volte riesci ad allenarti davvero?", "meglio due sicure che quattro sperate"), ("C'è qualcosa che ti fa male o ti preoccupa?", "prima di scrivere una sola serie"), ("Tra tre mesi, cosa ti farebbe dire «ne è valsa la pena»?", "è il tuo obiettivo vero")],
       "6 domande per il primo incontro con un cliente. 🔖 Salvalo.\nNon solo peso e obiettivo: cosa ha già provato, com'è la sua settimana vera, cosa gli farebbe dire «ne è valsa la pena».\n\nQual è la domanda che fai sempre tu? 👇"),
 # 5/12
 lista("S02_messaggi_che_tengono", "5 messaggi", "che tengono un cliente.", "Trenta secondi l'uno. Valgono più di una seduta gratis.",
       "I primi tre", "Quando", "va bene.", [("«Ho visto il carico di ieri: bravo»", "dopo un record o una serie in più"), ("«Un mese fa facevi 40, oggi 50»", "il progresso detto con i numeri"), ("«Buon allenamento per domani»", "la sera prima di una seduta dura")],
       "Gli altri due", "Quando", "si ferma.", [("«Tutto bene? Non ti vedo da qualche giorno»", "dopo una settimana, non dopo un mese"), ("«Riparti da qui, senza recuperare»", "toglie il senso di colpa del rientro"), ("Uno solo, poi aspetta", "inseguire fa scappare")],
       "5 messaggi che tengono un cliente. 🔖 Salvalo.\nTrenta secondi l'uno: un «bravo» dopo un record, un progresso detto con i numeri, un «tutto bene?» dopo una settimana di silenzio.\n\nQual è il messaggio che funziona di più con i tuoi? 👇"),
 # 12/12
 lista("S03_checklist_scheda", "Checklist: prima", "di consegnare una scheda.", "Sei controlli in due minuti. Evitano dieci messaggi dopo.",
       "I primi tre", "Si capisce", "da sola?", [("I nomi degli esercizi sono quelli che usa lui", "non il tuo gergo"), ("Ogni esercizio ha serie, ripetizioni e recupero", "niente caselle vuote"), ("C'è una nota dove serve", "tempo di esecuzione, presa, cosa sentire")],
       "Gli altri tre", "Si riesce", "a fare?", [("Sta nel tempo che ha", "contando riscaldamento e recuperi"), ("Gli attrezzi ci sono nella sua palestra", "o c'è un'alternativa scritta"), ("Sa da che carico partire", "anche solo «quello dell'ultima volta»")],
       "Checklist prima di consegnare una scheda. 🔖 Salvalo.\nSei controlli in due minuti: nomi chiari, niente caselle vuote, sta nel tempo che ha, sa da che carico partire.\n\nCosa controlli sempre tu? 👇"),
 # 19/12
 lista("S04_segnali_mollare", "5 segnali che un cliente", "sta per mollare.", "Nessuno sparisce da un giorno all'altro. Prima manda segnali.",
       "I primi tre", "Negli", "allenamenti.", [("Salta la seduta a metà settimana", "poi diventa tutta la settimana"), ("Fa meno serie di quelle scritte", "sempre le ultime"), ("I carichi sono fermi da un mese", "e non ne parla")],
       "Gli altri due", "Nel", "rapporto.", [("Risponde più tardi e più corto", "o smette di fare domande"), ("Sposta gli appuntamenti", "sempre un po' più in là"), ("Cosa fare", "un messaggio personale adesso, non un'offerta tra un mese")],
       "5 segnali che un cliente sta per mollare. 🔖 Salvalo.\nNessuno sparisce da un giorno all'altro: salta a metà settimana, fa meno serie, risponde più corto, sposta gli appuntamenti.\n\nQuale segnale hai imparato a riconoscere? 👇"),
 # 2/1
 lista("S05_prima_di_gennaio", "7 cose da preparare", "prima del pieno di gennaio.", "Da lunedì arrivano tutti insieme. Oggi hai ancora mezz'ora.",
       "Le prime quattro", "Per i", "nuovi.", [("Tre schede modello per chi inizia", "da adattare, non da riscrivere"), ("Il questionario iniziale pronto", "sempre lo stesso, sempre completo"), ("Prezzi e regole scritti", "pacchetti, disdette, scadenze"), ("Gli orari che puoi offrire davvero", "prima che te li chiedano")],
       "Le altre tre", "Per chi", "c'è già.", [("Un messaggio di rientro", "a chi si è fermato a dicembre"), ("La scheda nuova già pronta", "per chi riparte"), ("Un obiettivo a tre mesi per ciascuno", "gennaio passa, marzo no")],
       "7 cose da preparare prima del pieno di gennaio. 🔖 Salvalo.\nSchede modello, questionario, prezzi e regole scritti, orari veri. E un messaggio di rientro per chi si è fermato a dicembre.\n\nSei pronto per lunedì? 👇"),
 # 9/1
 lista("S06_chiedere_recensione", "Come chiedere una recensione", "senza imbarazzo.", "I clienti contenti la lasciano volentieri. Basta chiederla nel momento giusto.",
       "Quando", "Il momento", "giusto.", [("Dopo un risultato", "un record, una taglia, un dolore passato"), ("Quando te lo dice lui", "«mi trovo benissimo» è il segnale"), ("Mai insieme a un rinnovo", "sembra uno scambio")],
       "Come", "Le parole", "giuste.", [("«Mi aiuteresti con due righe?»", "chiedere un favore funziona più di chiedere un voto"), ("Dagli una traccia", "com'eri prima, cosa è cambiato, a chi lo consiglieresti"), ("Rendilo facile", "un link, due minuti, dal telefono")],
       "Come chiedere una recensione senza imbarazzo. 🔖 Salvalo.\nDopo un risultato, mai insieme a un rinnovo. E con una traccia: com'eri prima, cosa è cambiato, a chi lo consiglieresti.\n\nChiedi recensioni ai tuoi clienti? 👇"),
 # 16/1
 lista("S07_errori_principianti", "5 errori nelle schede", "per chi inizia.", "Li abbiamo fatti tutti. Riconoscerli fa restare i clienti di gennaio.",
       "I primi tre", "Troppo,", "troppo presto.", [("Troppi esercizi", "sei fatti bene battono dodici fatti di corsa"), ("Troppe sedute a settimana", "tre che riesce a fare, non cinque che salta"), ("Carichi da subito al limite", "prima impara il movimento")],
       "Gli altri due", "Poco", "chiaro.", [("Nomi che non conosce", "«hip thrust» non dice niente a chi inizia"), ("Nessuna progressione scritta", "se non sa quando salire, non sale"), ("La regola", "deve finire la seduta con voglia di tornare")],
       "5 errori nelle schede per chi inizia. 🔖 Salvalo.\nTroppi esercizi, troppe sedute, carichi subito al limite, nomi incomprensibili, nessuna progressione scritta.\n\nQuale hai fatto anche tu all'inizio? 👇"),
 # 23/1
 lista("S08_note_esercizio", "Cosa scrivere nelle note", "di un esercizio.", "Una riga giusta vale più di un video che non guarderà.",
       "Le prime tre", "Come", "si fa.", [("Il tempo", "«scendi in 3 secondi, sali deciso»"), ("Dove sentirlo", "«devi sentire i glutei, non la schiena»"), ("L'errore tipico", "«non staccare i talloni»")],
       "Le altre tre", "Come", "si regola.", [("Quando salire di carico", "«se fai 10 pulite, la prossima volta +2,5 kg»"), ("Quando fermarsi", "«se la tecnica cambia, la serie è finita»"), ("L'alternativa", "«se la macchina è occupata: manubri»")],
       "Cosa scrivere nelle note di un esercizio. 🔖 Salvalo.\nIl tempo, dove sentirlo, l'errore tipico. E poi: quando salire, quando fermarsi, l'alternativa se l'attrezzo è occupato.\n\nQual è la nota che scrivi più spesso? 👇"),
 # 30/1
 lista("S09_controllo_mensile", "5 idee per il controllo", "di fine mese.", "Dieci minuti con ogni cliente. È il momento in cui decide se rinnova.",
       "Le prime tre", "Guardare", "indietro.", [("Tre numeri che sono migliorati", "carichi, ripetizioni, presenze"), ("Una cosa che ha imparato", "un movimento, un'abitudine"), ("Cosa è stato difficile", "chiedilo, non indovinarlo")],
       "Le altre due", "Guardare", "avanti.", [("Un obiettivo per il mese prossimo", "uno, misurabile"), ("Cosa cambia nella scheda, e perché", "così la sente sua"), ("Chiudi con la data", "il prossimo controllo, già in agenda")],
       "5 idee per il controllo di fine mese. 🔖 Salvalo.\nTre numeri migliorati, una cosa imparata, cosa è stato difficile. Poi un obiettivo e la data del prossimo controllo.\n\nFai un punto fisso con i tuoi clienti? 👇"),
 # 6/2
 lista("S10_presentare_aumento", "Come presentare", "un aumento di prezzo.", "Si può fare senza perdere nessuno. Dipende da come lo dici.",
       "Prima", "Preparalo", "bene.", [("Avvisa un mese prima", "mai a sorpresa, mai a voce di corsa"), ("Scrivilo", "con la data e il nuovo prezzo, chiari"), ("Decidi le eccezioni prima", "non sul momento, per imbarazzo")],
       "Durante", "Dillo", "semplice.", [("Una frase, non una giustificazione", "«dal 1° marzo il percorso costa…»"), ("Ricorda cosa riceve", "non cosa è aumentato per te"), ("Lascia tempo", "chi ha domande te le fa, e va bene così")],
       "Come presentare un aumento di prezzo. 🔖 Salvalo.\nUn mese prima, per iscritto, con una frase sola e senza giustificarti. E le eccezioni decise prima, non per imbarazzo.\n\nCome l'hai comunicato l'ultima volta? 👇"),
 # 13/2
 lista("S11_scegliere_app", "6 domande prima di scegliere", "un'app per PT.", "Valgono per qualsiasi app, anche per la nostra.",
       "Le prime tre", "Per i tuoi", "clienti.", [("È nella loro lingua, tutta?", "anche i messaggi e le email"), ("Funziona dove si allenano?", "con il telefono bloccato, con poco segnale"), ("Vedono subito cosa fare oggi?", "senza cercare tra i menu")],
       "Le altre tre", "Per", "te.", [("Trattiene qualcosa sui tuoi incassi?", "e quanto, scritto dove"), ("Posso portare dentro quello che ho?", "schede, clienti, fatture"), ("Posso andarmene con i miei dati?", "e disdire senza telefonate")],
       "6 domande da fare prima di scegliere un'app per PT. 🔖 Salvalo.\nValgono per qualsiasi app, anche per la nostra: è tutta in italiano? Funziona dove si allenano? Trattiene qualcosa sugli incassi? Posso andarmene con i miei dati?\n\nQual è la domanda che aggiungeresti? 👇"),
]
