s=1
p `dd`.scan(/(?<=mul\()\d+,\d+(?=\))|do./).sum{|l|l[2]==?(?(s=1;0):l[2]==?n?s=0:s*eval(l.tr ?,,?*)}
