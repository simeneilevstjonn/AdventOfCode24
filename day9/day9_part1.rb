fileid = 0
file = true
idx = 0
data = []

disk = gets.chomp.chars.map{
  s = _1.to_i

  if file
    data += [fileid] * s
    fileid += 1
  else
    data += [-1] * s
  end
  file = !file
}

nb = true
while nb do
  # puts "here"
  # puts data.size
  # puts data*","
  i = data.size - 1
  while i >= 0 do
    # puts "i is #{i}, current data is #{data[i]}"
    if data[i] < 0
      i -= 1
      next
    end

    fe = data.index(-1)
    # puts "first empty is #{fe}"


    if fe > i
      nb = false
      break
    end

    data[i], data[fe] = data[fe], data[i]

    i -= 1

    # puts "i is #{i}"
  end
end

p data.map.with_index{|fileid, idx| fileid > 0 ? fileid * idx : 0}.sum
