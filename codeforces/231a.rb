canSolve = 0
gets.to_i.times.map {
  who_can = gets.split(" ").map {|x| x.to_i}
  if who_can.count(1) >=2
    canSolve +=1
  end
}
puts canSolve
