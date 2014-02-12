ans = 0
gets.to_i.times.map {
  gets.strip.map { |x|
    if x.include("++")
      ans +=1
    else
      ans -=1
    end
  }
}
puts ans
