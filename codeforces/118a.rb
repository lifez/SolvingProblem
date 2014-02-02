string = gets.chomp
string = string.downcase
vowels = "aeiouy"
string.each_char {|s|
  if vowels.include?(s)
    print ""
  else
    print "."+s
  end
}
puts 
