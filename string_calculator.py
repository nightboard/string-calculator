import re

def add(numbers: str):
  if numbers == '':
    return 0

  delstr_s = None
  if numbers[:2] == '//':
    numbers = numbers[2:]
    delstr_s = [ token for token in re.split('\[|\]', re.split('\n', numbers)[0]) if token != '']
    numbers = re.split('\n', numbers, 1)[1]

  pattern = ',|\n'
  if delstr_s is not None:
    for delstr in delstr_s:
      formatted_del = ''
      for del_ in delstr:
        formatted_del += f'\{del_}'
      pattern += f'|{formatted_del}'
  nums = [ int(_) for _ in re.split(pattern, numbers) ]

  # check for negatives
  for num in nums:
    if num < 0:
      raise ValueError(f'negatives not allowed. found {num}')

  # ignore numbers bigger than 1000
  total = 0
  for num in nums:
    if num <= 1000:
      total += num
  return total