n,limit = gets.chomp().split(" ")
pass = 0
score = gets.chomp.split(" ")
score.each { |x|
  if x.to_i >= score[limit.to_i-1].to_i and x.to_i !=0
      pass = pass+1 
  end
}
if score[0] == "0"
  pass = 0
end
puts pass
