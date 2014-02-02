limit =gets.chomp()
limit = limit.to_i
while limit>0
	word = gets.chomp()
	if word.length>10
		print word[0],word.length-2,word[-1]
		print "\n"
	else
		puts word
	end
	limit-=1
end