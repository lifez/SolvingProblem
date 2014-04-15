def locateelement(array)
  col = (array.count.to_f/2).ceil
  row = (array[col].count.to_f/2).ceil
  return col ,row
end

array = [[1,2],[1,2],[1,2]]

