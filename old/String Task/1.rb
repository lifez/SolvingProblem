x = gets.split("")
x.downcase()
ans=""
for i in x
	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="y"
		ans+=""
	else
		ans+="."+i
	end
end
puts ans