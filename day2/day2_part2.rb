p $<.count{|r|r=r.split.map(&:to_i);(0...r.size).map{|i|row=r[...i]+r[i+1..];n,x=row.each_cons(2).map{(_1-_2).abs}.minmax;(row==row.sort||row==row.sort.reverse)&&n>0&&x<4}.any?}
