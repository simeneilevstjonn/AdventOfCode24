r,d=`dd`.split("

").map{_1.split("
").map{|i|i.split(/\||,/).map &:to_i}}

rules = r
data = d

incorrect = data.filter{|line|
  line.size.times.map{|i|
    rules.map{|dep, el|
      line[i] == el && line[i + 1..].include?(dep)
    }.any?
  }.any?
}

p incorrect.sum{|line|
  ac = false
  while !ac
    ac = true
    i = 0
    while i < line.size - 1 do
      if (rules.map{|dep, el|line[i] == el && line[i + 1..].include?(dep)}.any?)
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
