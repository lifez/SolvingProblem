#one line puts  (gets.strip.downcase.chars - 'aeiouy'.chars).map { |x| '.' + x }.join
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
