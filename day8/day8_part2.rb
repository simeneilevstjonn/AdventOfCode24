grid = $<.map{_1.chomp.chars}
tx = grid.flat_map.with_index{|r,i|r.filter_map.with_index{|c,j|[i,j,c]if c!=?.}}
an = []
tx.combination(2).map{
    i,j,c=_1;
    y,x,d=_2;
    if c==d
        dy=y-i;
        dx=x-j;
        (0..).map{|m|
            ny=i+m*dy;
            nx=j+m*dx;
            nY=i-m*dy;
            nX=j-m*dx;
            e=0
            ny>=grid.size||nx>=grid[0].size||nx<0||ny<0 ?(e+=1):an.push([ny,nx])
            nY>=grid.size||nX>=grid[0].size||nX<0||nY<0 ?(e+=1):an.push([nY,nX])
            break if e>1
        }
    end
}
p an.uniq.size
