x = gets.to_i()
cap = 0
maxcap =0
while x>0
	passen = gets.chomp.split()
	cap-=passen[0].to_i
	cap+=passen[1].to_i
	if cap>maxcap
		maxcap=cap
	end
	x-=1
end
puts maxcap