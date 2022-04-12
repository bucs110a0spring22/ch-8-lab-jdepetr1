class StringUtility:
  VOWELS = "aeiouAEIOU"
  ALPHABET_COUNT = 26
  
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string
    
  def vowels(self):
    count = 0
    for letter in range(len(self.string)):
      if self.string[letter] in StringUtility.VOWELS:
        count+=1
    if count >= 5:
      return "many"
    return str(count)

  def bothEnds(self):
    if len(self.string) <= 2:
      return ''    
    return str(self.string[0]+self.string[1]+self.string[-2]+self.string[-1])

  def fixStart(self):
    if len(self.string) <= 1:
      return self.string

    first_char = self.string[0]
    out = first_char
    for letter in range(1, len(self.string)):
      if self.string[letter] == first_char:
        out +="*"
      else:
        out += self.string[letter]
    return out

  def asciiSum(self):
    sum = 0
    for letter in range(len(self.string)):
      sum += ord(self.string[letter])
    return sum

  def cipher(self):
    length = len(self.string)
    out = ""
    for letter in range(length):
      num = ord(self.string[letter])
      if num <= ord('Z') and num >= ord('A'):
        num += length % StringUtility.ALPHABET_COUNT
        if num > ord('Z'):
          num -= StringUtility.ALPHABET_COUNT
        out += chr(int(num))
      elif num <= ord('z') and num >= ord('a'):
        num += length % StringUtility.ALPHABET_COUNT
        if num > ord('z'):
          num -= StringUtility.ALPHABET_COUNT
        out += chr(int(num))
      else:
        out += self.string[letter]
    return out