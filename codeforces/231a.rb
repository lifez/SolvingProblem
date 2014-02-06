problems = gets.strip.to_i
canSolve = 0
(1..problems).each {|x|
  who_can = gets.split(" ").map {|x| x.to_i}
  if who_can.count(1) >= 2
    canSolve += 1
  end
}
puts canSolve
