s=-1
n=[]
A=->(i,j,c,y,x,d,m){e=i+m*(y-i);f=j+m*(x-j);c!=d||e>s||f>s||f<0||e<0?1:(n.push [e,f];0)}
$<.flat_map{|r|s+=1;g=-1;r.chomp.chars.filter_map{g+=1;[s,g,_1]if _1!=?.}}.combination(2).map{|a,b|(0..).map{break if A.(*a,*b,_1)+A.(*a,*b,-_1)>1}}
p n.uniq.size
