x = gets.chomp().split("")
n ="NO"
for i in x
	if i=='H' or i=="Q" or i=="9"
		n = "YES"
	end
end
puts n