def chk_hit(dod,d,dragon)
	hit = 0
	while d!=0
		if d%dod==0 and dragon[d-1]==1
			hit+=1
			dragon[d-1]=0
		end
		d-=1
	end
	return hit
end
k = gets.to_i()
l = gets.to_i()
m = gets.to_i()
n = gets.to_i()
d = gets.to_i()
dragon = Array.new(d,1)
x = 0
hit = 0
hit+=chk_hit(k,d,dragon)
hit+=chk_hit(l,d,dragon)
hit+=chk_hit(m,d,dragon)
hit+=chk_hit(n,d,dragon)
puts hit