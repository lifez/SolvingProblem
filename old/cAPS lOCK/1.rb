def chk(word)
	word=word.split("")
	n=0
	for i in word
		if i==i.downcase()
			n+=1
		end
	end
	return n
end
x = gets.chomp
if x[0]==x[0].downcase and chk(x)>1
	puts x
elsif x[0]==x[0].downcase and chk(x)<=1
	puts x.capitalize!
elsif x==x.upcase()
	puts x.downcase()
else
	puts x
end