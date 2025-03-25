module Circle

  PI = 3.141592653589793
  
  def Circle.area(radius)
    PI * radius**2
  end
  
  def Circle.circumference(radius)
    2 * PI * radius
  end
end

puts "Enter the radius of the circle:"
radius = gets.chomp.to_f

puts "The area of the circle is: #{Circle.area(radius)}"
puts "The circumference of the circle is: #{Circle.circumference(radius)}"
