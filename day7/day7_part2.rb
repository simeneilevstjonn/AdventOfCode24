p $<.sum{|row|
  s,*n = row.scan(/\d+/).map(&:to_i)

  (0...(3**(n.size - 1))).any?{|i|
    idx = -1
    n.inject{[_1*_2,_1+_2,"#{_1}#{_2}".to_i][(i/(3**(idx+=1)))%3]}==s
  }?s:0
}
