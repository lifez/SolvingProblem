x = gets.chomp()
y = gets.chomp()
x = x.upcase()
y = y.upcase()
if x>y
	puts 1
elsif x==y
	puts 0
else
	puts -1
end