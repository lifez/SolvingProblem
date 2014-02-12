def chk(words)
  n = 0
  words.each_char {|x|
    if x == x.downcase
      n += 1
    end
  }
  n
end
input = gets.strip
if input[0] == input[0].downcase and chk(input) > 1
  puts input
elsif input[0] == input[0].downcase and chk(input) <= 1
  puts input.capitalize
elsif input == input.upcase()
  puts input.downcase
else
  puts input
end
