import re
word_sep = re.compile(r"\s+\|\s+")

newdoc = []

infi = "/Volumes/data/Mind/lucidchart_schema.out"
skip = 2
count = 0
read_count = 0

with open(infi, 'r') as doc:
    for line in doc:
        count += 1
        if count <= skip:    
            continue
        read_count += 1
        words = word_sep.split(line)
        newdoc.append(";".join(['"%s"' % w.strip() for w in words]))


outfi = "/Volumes/data/Mind/lucidchart_schema.mod"
with open(outfi, 'w+') as fi:
    fi.write("\n".join(newdoc))
