fileid = 0
file = true
idx = 0
files = []
gaps = []

disk = gets.chomp.chars.map{
  s = _1.to_i

  if file
    files.push [idx, fileid, s]
    fileid += 1
  else
    gaps.push [idx, s]
  end
  file = !file
  idx += s
}

i = files.size - 1
while i >= 0 do
  idx, fileid, fs = files[i]
  j = 0
  while j < gaps.size do
    gap = gaps[j]
    if gap[0] < idx && gap[1] >= fs
      files[i][0] = gap[0]

      gaps[j][1] -= fs
      gaps[j][0] += fs

      break
    end
    j += 1
  end

  i -= 1
end

p files.sum{|idx, fileid, s|
(idx...idx+s).sum{
  |i| i * fileid
}
}
