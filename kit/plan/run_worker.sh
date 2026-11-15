#!/bin/bash
# renders the posts of one list, one at a time, in date order (so the nearest dates are ready first)
cd /home/claude/social/kit
for id in $(cat plan/ids_$1.txt); do python3 render.py posts_plan.json $id >> plan/render_$1.log 2>&1 || echo "FAIL $id" >> plan/render_$1.log; done
echo ALLDONE >> plan/render_$1.log
