t= `dd`.split"
"
l=t.size-2
t=t*""
p [%w(M.M S.S),%w(S.S M.M),%w(M.S M.S),%w(S.M S.M)].sum{t.scan(/(?=#{_1}.{#{l}}A.{#{l}}#{_2})/).count}