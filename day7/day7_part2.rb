p $<.sum{s,*n=_1.scan(/\d+/).map &:to_i;(0...3**(n.size-1)).any?{|i|i*=3;n.inject{|a,b|[a*b,a+b,"#{a}#{b}".to_i][(i/=3)%3]}==s}?s:0}
