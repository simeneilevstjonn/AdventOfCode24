a,b=$<.map{_1.split.map &:to_i}.transpose
p a.sum{_1*b.count(_1)}
