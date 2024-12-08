g=$<.map{_1.chomp.chars}
n=[]
A=->(i,j,c,y,x,d,m){e=i+m*(y-i);f=j+m*(x-j);c!=d||e>=g.size||f>=g[0].size||f<0||e<0?1:(n.push([e,f]);0)}
g.flat_map.with_index{|r,i|r.filter_map.with_index{|c,j|[i,j,c]if c!=?.}}.combination(2).map{|a,b|(0..).map{break if A.(*a,*b,_1)+A.(*a,*b,-_1)>1}}
p n.uniq.size
