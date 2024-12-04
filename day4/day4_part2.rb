t= `dd`.split"
"
p [%w(M.M S.S),%w(S.S M.M),%w(M.S M.S),%w(S.M S.M)].sum{t.join.scan(/(?=#{_1+[".{#{t.size-2}}"]*2*?A+_2})/).count}