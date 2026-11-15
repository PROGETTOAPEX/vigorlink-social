"""Helpers for the 3-month plan (17/11/2026 – 13/02/2027). Slides follow engine.html."""
def T(a, b): return [[a, "w"], [b, "g"]]
def hero(k, a, b, body, chips=None, size=None, bg=None):
    s = {"type": "hero", "kicker": k, "title": T(a, b), "body": body}
    if chips: s["chips"] = chips
    if size: s["size"] = size
    if bg: s["bg"] = bg
    return s
def dev(k, a, b, body, phone=None, laptop=None):
    s = {"type": "device", "kicker": k, "title": T(a, b), "body": body}
    if phone: s["phone"] = phone
    if laptop: s["laptop"] = laptop
    return s
def lst(k, a, b, items, icons=None, note=None, bg=None):
    s = {"type": "list", "kicker": k, "title": T(a, b), "items": [list(i) for i in items]}
    if icons: s["icons"] = icons
    if note: s["note"] = note
    if bg: s["bg"] = bg
    return s
def stat(k, value, label, body, note=None, bg=None, vsize=None):
    s = {"type": "stat", "kicker": k, "value": value, "label": label, "body": body}
    if note: s["note"] = note
    if bg: s["bg"] = bg
    if vsize: s["vsize"] = vsize
    return s
def split(k, a, b, left, right, note=None):
    s = {"type": "split", "kicker": k, "title": T(a, b), "left": left, "right": right}
    if note: s["note"] = note
    return s
def chip(text, sub, k="msg", x=120, y=0.70, i=None):
    c = {"k": k, "text": text, "sub": sub, "x": x, "y": y}
    if i: c["i"] = i
    return c
def cta(bg=None):
    s = {"type": "cta", "kicker": "In arrivo nel primo trimestre 2027", "title": T("Mettiti in lista.", "Diventa Fondatore."),
         "body": "I primi 25 personal trainer che si abbonano al lancio: fino a −30% per 6 mesi.",
         "buttons": [["Lista Fondatori · link in bio", "o"]], "foot": "Entrare in lista è gratis e non ti impegna a nulla."}
    if bg: s["bg"] = bg
    return s
CLOSE_P = "In arrivo nel primo trimestre 2027 · lista Fondatori nel link in bio."
CLOSE_E = "VigorLink, l'app italiana per personal trainer, arriva nel primo trimestre 2027 · lista Fondatori nel link in bio."
TAGS = {
 "prod": "#personaltrainer #personaltraineritalia #coachingonline #fitnessitalia #schedeallenamento",
 "biz": "#personaltrainer #fitnessbusiness #partitaiva #personaltraineritalia #coachingonline",
 "quiz": "#personaltrainer #mitidelfitness #allenamento #palestra #fitnessitalia",
 "list": "#personaltrainer #personaltraineritalia #coachingonline #clienti #fitnessbusiness",
}
def P(pid, slides, cap, kind="prod", reel=True):
    close = CLOSE_P if kind == "prod" else CLOSE_E
    p = {"id": pid, "slides": slides, "caption": cap.strip() + "\n" + close + "\n" + TAGS[kind], "kind": kind}
    if reel: p["reel"] = "auto"
    return p
