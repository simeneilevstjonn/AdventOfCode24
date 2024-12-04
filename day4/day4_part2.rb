text = `dd`


lineLen = text.split("\n")[0].size


p [["M.M","S.S"],["S.S","M.M"],["M.S","M.S"],["S.M","S.M"]].sum{|a,b|
  text.scan(/(?=#{a}(?:.|\n){#{lineLen - 1}}A(?:.|\n){#{lineLen - 1}}#{b})/).count
}