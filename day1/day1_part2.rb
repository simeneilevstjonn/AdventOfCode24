dta=$<.map{_1.split.map &:to_i}
a = dta.map{_1[0]}
b = dta.map{_1[1]}
p a.sum{_1 * b.count(_1)}
