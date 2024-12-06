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

do_trace(y,x,0,grid, ->(x,y,d){trace.push([x,y,d]);true})


p (1...trace.size).sum{|i|
    y,x,d = trace[i]
    p i.to_f / trace.size

    g = grid.map{_1.dup}
    g[y][x] = ?#

    l = false
    local_trace = []
    do_trace(*trace[i - 1], g, ->(y,x,d){(trace[...(i-1)].include?([y,x,d]) || local_trace.include?([y,x,d]))?(l=true;false):(local_trace.push([y,x,d]);true)})

    l ? 1 : 0
}
