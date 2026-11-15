#!/bin/bash
# packs what is rendered, pushes it, prints the Metricool payloads of the posts packed in this run
cd /home/claude/social/kit && IDS=$(python3 plan/package.py | cut -d' ' -f2-)
cd /home/claude/vigorlink-social && git add plan && git commit -qm "media: 3-month plan, batch

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HTDV22PcJUL5AncSijzSD9" && git push -q origin main
H=$(git log -1 --format=%H)
python3 - "$H" $IDS <<'PY'
import json,sys
H=sys.argv[1]; ids=sys.argv[2:]
cal={p['id']:p for p in json.load(open('/home/claude/social/kit/plan/calendar.json'))}
base=f'https://raw.githubusercontent.com/PROGETTOAPEX/vigorlink-social/{H}/plan/'
print('SHA',H[:7])
for i in sorted(ids,key=lambda x:cal[x]['date']):
    p=cal[i]
    print(p['date'],p['format'],p['slides'],i)
    print(json.dumps(p['caption'],ensure_ascii=False))
PY
