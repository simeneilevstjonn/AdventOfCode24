p `dd`.scan(/(?<=mul\()\d+,\d+(?=\))/).sum{eval _1.tr(?,,?*)}
