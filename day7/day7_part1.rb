p $<.sum{|row|
  s,*n = row.scan(/\d+/).map(&:to_i)

  (0...(1<<(n.size - 1))).any?{|i|
    idx = -1
    n.inject{i&(1<<(idx+=1))>0? _1*_2 : _1+_2}==s
  }?s:0
}
