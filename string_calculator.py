def add(numbers: str):
  if numbers == '':
    return 0

  splits = numbers.split(',')

  total = 0
  for split in splits:
    nums = [ int(_) for _ in split.split('\n') ]
    for num in nums:
      total += num

  return total
