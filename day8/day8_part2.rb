grid=$<.map{_1.chomp.chars}
tx=grid.flat_map.with_index{|r,i|r.filter_map.with_index{|c,j|[i,j,c]if c!=?.}}
an=[]
A=->(i,j,c,y,x,d,m){e=i+m*(y-i);f=j+m*(x-j);c!=d||e>=grid.size||f>=grid[0].size||f<0||e<0?1:(an.push([e,f]);0)}
tx.combination(2).map{|a,b|(0..).map{break if A.(*a,*b,_1)+A.(*a,*b,-_1)>1}}
p an.uniq.size
