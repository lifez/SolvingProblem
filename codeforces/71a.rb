limit = gets.chomp.to_i
(1..limit).each { |x|
  s = gets.chomp
  if s.length > 10
    puts s.chars.first+(s.length-2).to_s+s.chars.last
  else
    puts s
  end
}
