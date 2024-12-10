g=$<.map{[0]+_1.bytes}
s=g[0].size
g=[[0]*s,*g,[0]*s]
D=->(h,y,x){h>56?1:[[y-1,x],[y,x-1],[y+1,x],[y,x+1]].sum{g[_1][_2]==h+1?D.(h+1,_1,_2):0}}
s=0
g.map.with_index{|r,i|r.map.with_index{s+=_1==48?D.(48,i,_2):0}}
p s
