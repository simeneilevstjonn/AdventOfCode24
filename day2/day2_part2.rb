p $<.map{_1.split.map &:to_i}.count{|ir|(0...ir.size).map{|i|row=ir[...i]+ir[i+1..];n,x=row.each_cons(2).map{(_1-_2).abs}.minmax;(row==row.sort||row==row.sort.reverse)&&n>0&&x<4}.any?}
