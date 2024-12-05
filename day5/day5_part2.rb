r,d=`dd`.split("

").map{_1.split("
").map{|i|i.split(/\||,/).map &:to_i}}
v=->(l,i){r.map{l[i]==_2&&l[i+1..].include?(_1)}.any?}
I=d.filter{|l|(0...l.size).any?{v.(l,_1)}}
p I.sum{|l|
  (0...l.size).map{|i|(0..l.size-2).map{|j|v.(l,j)?(l[j],l[j+1]=l[j+1],l[j]):0}}
  l[l.size/2]
}
