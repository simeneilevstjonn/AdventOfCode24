s=1
p `dd`.scan(/(?<=mul\()\d+,\d+(?=\))|do(?:(?:n't)?)\(\)/).sum{|l|
  r = 0;
  if l == "do()"
    s = 1
  elsif l == "don't()"
    s = 0
  else
    r = s * eval(l.tr(?,,?*))
  end;
  r
}
