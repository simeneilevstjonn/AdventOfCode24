t= `dd`
l=t.split("\n")[0].size-1
p [["M.M","S.S"],["S.S","M.M"],["M.S","M.S"],["S.M","S.M"]].sum{t.scan(/(?=#{_1}(?:.|\n){#{l}}A(?:.|\n){#{l}}#{_2})/).count}