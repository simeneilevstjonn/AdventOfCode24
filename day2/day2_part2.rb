p $<.count{|r|r=r.split.map(&:to_i);(0...r.size).map{|i|a=r[...i]+r[i+1..];n,x=a.each_cons(2).map{(_1-_2).abs}.minmax;(a==a.sort||a==a.sort.reverse)&&n>0&&x<4}.any?}
