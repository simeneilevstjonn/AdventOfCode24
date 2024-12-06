g=$<.map{_1.chomp.chars}
V=->(y,x){y>=0&&x>=0&&y<g.size&&x<g[0].size}
D=->(y,x,d,s){(0..).map{V.(y,x)&&s.(y,x,d)?((0..).map{n,m=[[y-1,x],[y,x+1],[y+1,x],[y,x-1]][d];V.(n,m)&&g[n][m]==?#?(d=(d+1)%4):(y,x=n,m;break)}):break}}
t=[]
D.(*g.map.with_index{[_2,_1.index(?^)]}.find{_2},0,->(y,x,d){t.push([y,x,d]);true})
p (1...t.size).map{|i|y,x,d=t[i];g[y][x]=?#;l=0;v=g.map{_1.map{[false]*4}};D.(*t[0],->(y,x,d){v[y][x][d]?(l=1;false):(v[y][x][d]=true)});g[y][x]=?.;l>0?[y,x]:0}.uniq.size-1