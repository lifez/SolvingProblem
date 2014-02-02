x,y,z=gets.chomp.split()
x = x.to_i
y = y.to_i
z = z.to_i
point = 0
while true
	if point==0
		z-=x.gcd(z)
		if z<=0
			puts 0
			break
		end
		point+=1
	end
	if point==1
		z-=y.gcd(z)
		if z<=0
			puts 1
			break
		end
		point-=1
	end

end
