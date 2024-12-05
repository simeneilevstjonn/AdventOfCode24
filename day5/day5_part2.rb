r,d=`dd`.split("

").map{_1.split("
").map{|i|i.split(/\||,/).map &:to_i}}

rules = r
data = d

v=->(l,i){r.map{l[i]==_2&&l[i+1..].include?(_1)}.any?}

I=d.filter{|l|(0...l.size).any?{v.(l,_1)}}

p I.sum{|line|
  ac = false
  while !ac
    ac = true
    i = 0
    while i < line.size - 1 do
      if v.(line,i)
        temp = line[i + 1]
        line[i + 1] = line[i]
        line[i] = temp
        ac = false
      end

      i += 1
    end
  end

  line[line.size / 2]
}
