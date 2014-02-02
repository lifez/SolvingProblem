Name =  ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
x = gets.to_i()
y = 5
while true
	if x<=y
		y/=5
		puts Name[(x-1)/y]
		break
	else
		x-=y
		y*=2
	end
end

