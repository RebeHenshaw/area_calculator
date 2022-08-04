class Rectangle:

  def __init__(self, width, height):
    self.height = height
    self.width = width


  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


  def set_height(self, height):
    """Set height of rectangle or side of square."""
    self.height = height
    if isinstance(self, Square): 
        self.width = height


  def set_width(self, width):
    """Set width of rectangle or side of square."""
    self.width = width
    if isinstance(self, Square): 
        self.height = width


  def get_area(self):
    """Retrieve area."""
    return self.width * self.height


  def get_perimeter(self):
    """Retrieve perimeter."""
    return (self.width * 2) + (self.height * 2)


  def get_diagonal(self):
    """Retreive diagonal."""
    return ((self.width ** 2 + self.height ** 2) ** .5)


  def get_picture(self):
    """Retreive visual representation of object."""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    line = ''
    for each in range(self.height):
      line += '*' * self.width + '\n'
    return line


  def get_amount_inside(self, other):
    """Retreive number of times one object fits inside the other object without rotating."""
    if self.height < other.height or self.width < other.width:
      return 0
    bigarea = self.get_area()
    smallarea = other.get_area()
    return bigarea // smallarea


class Square(Rectangle):

  def __init__(self, side):
    self.height = side
    self.width = side


  def __str__(self):
    return f"Square(side={self.width})"

  
  def set_side(self, side):
    """Assign side length to a square. Can also use set_height() or set_width() inherited from Rectangle class."""
    self.height = side
    self.width = side
