def add(numbers: str):
  if numbers == '':
    return 0
  nums = [ int(_) for _ in numbers.split(",") ]
  return sum(nums)
