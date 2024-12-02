p $<.count{|r|r=r.split.map &:to_i;(0...r.size).map{|i|a=r[...i]+r[i+1..];n,x=(b=a.sort).each_cons(2).map{_2-_1}.minmax;(a==b||a==b.reverse)&&n>0&&x<4}.any?}
