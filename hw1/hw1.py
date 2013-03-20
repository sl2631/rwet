import sys
for line in sys.stdin:
line = line.strip()
line = line.replace("wood","money")
line = line.replace("chuck","manager")
print line