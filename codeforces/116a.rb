stations = gets.strip.to_i
unit = 0
maxcap = 0
(1..stations).each { |x|
  exits,enters = gets.chomp.split(" ").map{ |x| x.to_i}
  unit += enters
  unit -= exits
  if maxcap < unit
    maxcap = unit
  end
}
puts maxcap
