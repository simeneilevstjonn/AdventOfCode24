t=`dd`
l=t.split("\n")[0].size-1
p [%w(M.M S.S),%w(S.S M.M),%w(M.S M.S),%w(S.M S.M)].sum{t.scan(/(?=#{_1}(?:.|\n){#{l}}A(?:.|\n){#{l}}#{_2})/).count}