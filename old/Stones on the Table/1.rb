def all_equal(array)
	return array.max == array.min
end
x = gets.to_i
instone = gets.chomp().split("")
count =0
i = 0 
while i<x
	if instone[i]==instone[i+1]
		count+=1
	end
	i+=1
end
if all_equal(instone)
	count = x-1
end
puts count
