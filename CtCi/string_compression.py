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
        prev_char = val
        count = 0
      count += 1
    if prev_char != "":
      return_str += prev_char
      return_str += str(count)

    if len(return_str) < len(self.string):

      return return_str
    else:
      return self.string

compressor = CompressString("aaaabb")
print(compressor.compress())
print(1 if compressor.compress() == "a3" else 0)
