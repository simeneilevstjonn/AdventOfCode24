g=$<.map{_1.chomp.chars}
D=->(y, x, d, stopf){
    while  y >= 0 && x >= 0 && y < g.size && x < g[0].size && stopf.(y,x,d) do
        (0..3).map{
            ny,nx=[[y-1,x],[y,x+1],[y+1,x],[y,x-1]][d]
            if ny >= 0 && nx >= 0 && ny < g.size && nx < g[0].size && g[ny][nx] == ?#
                d += 1
                d %= 4
            else
                y,x=ny,nx
                break
            end
        }
    end}
t=[]
D.(*g.map.with_index{[_2,_1.index(?^)]}.find{_2},0,->(y,x,d){t.push([y,x,d]);true})
p (1...t.size).map{|i|y,x,d=t[i];g[y][x]=?#;l=0;v=g.map{_1.map{[false]*4}};D.(*t[0],->(y,x,d){v[y][x][d]?(l=1;false):(v[y][x][d]=true)});g[y][x]=?.;l>0?[y,x]:0}.uniq.size-1