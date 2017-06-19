# -*- coding: utf-8 -*-
import slate
import sys

with open(sys.argv[1]) as f:
    doc = slate.PDF(f)

check = False
f=open(sys.argv[1].split(".")[0] + ".txt", "wt")
for s in doc:
    ss = s.split("\n")
    for sss in ss:
        #f.write("%s\t%d\n" % (sss, sss=="교회를 섬기는 분들"))
        if sss=="교회를 섬기는 분들": check = True; continue
        if sss=="주일 대예배": check = False; break
        if check: 
            sss = sss.strip()
            if sss != "" and sss[-1] != "/":
                for name in sss.split(" "):
                    if name == "" or name[-1] == ":" or name[-1] == "/": continue
                    f.write(name+"\n")
