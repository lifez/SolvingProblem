x = gets.chomp()
x = x.to_i
if x%2==0
	if x==2
		puts "NO"
	else
		puts "YES"
	end
else
	puts "NO"
end
