class CompressString:

  def __init__(self, string):
    self.string = string

  def compress(self):
    return_str = ""
    prev_char = ""
    count = 0

    for val in self.string:
      if val != prev_char:
        if prev_char != "":
          return_str += prev_char
          return_str += str(count)
        count = 0
      count += 1
    if prev_char != "":
      return_str += prev_char
      return_str += str(count)

    if len(return_str) < len(self.string):
      print(return_str)
      return return_str
    else:
      return self.string

compressor = CompressString("a")
print(1 if compressor.compress() == "a1" else 0)
