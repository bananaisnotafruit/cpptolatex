from os import listdir

arr = sorted(listdir("."))

arr = [x for x in arr if x.endswith(".cpp")]

out = open("testfile.tex", 'w')

out.write("\\documentclass{report}\n")
out.write("\\begin{document}\n")

for i in arr:
    out.write("\\section{}\n")
    temp = open(i)
    str = temp.read()

    str = str.replace("#","\#")
    str = str.replace("{","\{")
    str = str.replace("}","\}")
    str = str.replace("\n","\\\*")
    str = str.replace(">","$>$")
    str = str.replace("<","$<$")
    str = str.replace("%","\\%")
    out.write(str)
  
    temp.close()
    #out.write()


out.write("\\end{document}")
