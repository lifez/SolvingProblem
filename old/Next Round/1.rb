limit,Smax = gets.chomp.split()
scores = gets.chomp.split()
ssum = 0
for score in scores
	score = score.to_i
	if score>0 and score>=scores[Smax.to_i-1].to_i
		ssum +=1
	end
end
puts ssum
