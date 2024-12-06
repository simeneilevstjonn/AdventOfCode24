grid = $<.map{_1.chomp.chars}

y, x = grid.map.with_index{[_2,_1.index(?^)]}.find{_2}
p [y,x]
trace = []

def do_trace(y, x, d, grid, stopf)
    while  y >= 0 && x >= 0 && y < grid.size && x < grid[0].size && stopf.(y,x,d) do
        (0..3).map{
            ny,nx=[[y-1,x],[y,x+1],[y+1,x],[y,x-1]][d]
            # puts "attempting transistion from #{[y,x]} to #{[ny, nx]}"
            if ny >= 0 && nx >= 0 && ny < grid.size && nx < grid[0].size && grid[ny][nx] == ?#
                d += 1
                d %= 4
                # puts "hit target, turning right"
            else
                y,x=ny,nx
                break
            end
        }
    end
end

do_trace(y,x,0,grid, ->(y,x,d){trace.push([y,x,d]);true})


alts = []

(1...trace.size).map{|i|
    y,x,d = trace[i]
    # p i.to_f / trace.size

    grid[y][x] = ?#

    l = false
    vis = grid.map{_1.map{[false] * 4}}
    do_trace(*trace[i - 1], grid, ->(y,x,d){
        vis[y][x][d] ?  (l=true;false) :
        (vis[y][x][d] = true)
    })

    if l
        alts.push([y,x])
    end

    grid[y][x] = ?.
}


p alts.uniq.size
