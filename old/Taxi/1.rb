limit = gets.to_i
x = gets.split(" ").map{|x| x.to_i}
x =x.sort.reverse
i=0
j=limit-1
ans =0
while i<=j
	ans+=1
	four = 4-x[i]
	while x[j]<=four and j>=i
		four-=x[j]
		j-=1
	end
	i+=1
end
puts ans


