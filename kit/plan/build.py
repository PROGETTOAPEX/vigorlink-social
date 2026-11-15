"""Assembles the 3-month calendar: dates + posts → ../posts_plan.json and ../plan/calendar.json."""
import json, datetime as dt
from c_mon_tue import MON, TUE
from c_wed_thu import WED, THU
from c_fri_sat import FRI, SAT
SKIP = {dt.date(2026, 12, 25), dt.date(2026, 12, 26), dt.date(2027, 1, 1)}
START = {"TUE": dt.date(2026, 11, 17), "WED": dt.date(2026, 11, 18), "THU": dt.date(2026, 11, 19),
         "FRI": dt.date(2026, 11, 20), "SAT": dt.date(2026, 11, 21), "MON": dt.date(2026, 11, 23)}
END = dt.date(2027, 2, 13)
cal = []
for name, posts in (("MON", MON), ("TUE", TUE), ("WED", WED), ("THU", THU), ("FRI", FRI), ("SAT", SAT)):
    d = START[name]; i = 0
    while d <= END:
        if d not in SKIP:
            assert i < len(posts), (name, d)
            p = dict(posts[i]); p["date"] = d.isoformat(); cal.append(p); i += 1
        d += dt.timedelta(days=7)
    assert i == len(posts), (name, i, len(posts))
cal.sort(key=lambda p: p["date"])
ids = [p["id"] for p in cal]; assert len(set(ids)) == len(ids)
json.dump([{k: v for k, v in p.items() if k in ("id", "slides", "reel")} for p in cal], open("../posts_plan.json", "w"), ensure_ascii=False, indent=1)
json.dump([{"date": p["date"], "id": p["id"], "format": "reel" if p.get("reel") else "carousel", "kind": p["kind"], "caption": p["caption"], "slides": len(p["slides"])} for p in cal], open("calendar.json", "w"), ensure_ascii=False, indent=1)
print(len(cal), sum(1 for p in cal if p.get("reel")), "reels")
for p in cal: 
    assert len(p["caption"]) < 2200
print(cal[0]["date"], cal[0]["id"], "…", cal[-1]["date"], cal[-1]["id"])
