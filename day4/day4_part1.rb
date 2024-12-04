text = `dd`


lineLen = text.split("\n")[0].size


normal = text.count("XMAS")
rev = text.count("SAMX")
dn = text.scan(/X(?:.|\n){#{lineLen}}M(?:.|\n){#{lineLen}}A(?:.|\n){#{lineLen}}S/).size
up = text.scan(/S(?:.|\n){#{lineLen}}A(?:.|\n){#{lineLen}}M(?:.|\n){#{lineLen}}X/).size

di = [-1, 1].sum{|i|
  text.scan(/X(?:.|\n){#{lineLen + i}}M(?:.|\n){#{lineLen + i}}A(?:.|\n){#{lineLen + i}}S/).size +
  text.scan(/S(?:.|\n){#{lineLen + i}}A(?:.|\n){#{lineLen + i}}M(?:.|\n){#{lineLen + i}}X/).size
}

p normal + rev + dn + up + di
