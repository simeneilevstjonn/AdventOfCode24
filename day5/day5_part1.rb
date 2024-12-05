rules, data = `dd`.split("\n\n")

rules = rules.split("\n").map{_1.split(?|).map(&:to_i)}

p data.split("\n").sum{|line|
  line = line.split(?,).map(&:to_i);

  line.size.times.map{|i|
    rules.map{|dep, el|
      line[i] == el && line[i + 1..].include?(dep)
    }.any?
  }.any? ? 0 : line[line.size / 2]
}
