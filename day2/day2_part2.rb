rows = $<.map{_1.split.map(&:to_i)}
p rows.count{|ir|(0...ir.size).map{|i|row=ir[...i]+ir[i + 1..];d=row.each_cons(2).map{(_1-_2).abs};(row==row.sort||row==row.sort.reverse)&&d.min>0&&d.max<4}.any?}
