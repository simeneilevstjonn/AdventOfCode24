text = `dd`


lineLen = text.split("\n")[0].size


p normal = text.scan(/XMAS/).size
p rev = text.scan(/SAMX/).size
p dn = text.scan(/(?=X(?:.|\n){#{lineLen}}M(?:.|\n){#{lineLen}}A(?:.|\n){#{lineLen}}S)/).size
p up = text.scan(/(?=S(?:.|\n){#{lineLen}}A(?:.|\n){#{lineLen}}M(?:.|\n){#{lineLen}}X)/).size

di = [-1, 1].sum{|i|
  (p text.scan(/(?=X(?:.|\n){#{lineLen + i}}M(?:.|\n){#{lineLen + i}}A(?:.|\n){#{lineLen + i}}S)/).size) +
  (p text.scan(/(?=S(?:.|\n){#{lineLen + i}}A(?:.|\n){#{lineLen + i}}M(?:.|\n){#{lineLen + i}}X)/).size)
}

p normal + rev + dn + up + di
