dta=$<.map{_1.split.map &:to_i}
a = dta.map{_1[0]}.sort
b = dta.map{_1[1]}.sort
p a.zip(b).sum{(_1-_2).abs}
