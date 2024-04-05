import re

def review_code(code):
  """Reviews code and provides feedback on code quality and adherence to best practices.

  Args:
    code: A string containing the code to be reviewed.

  Returns:
    A list of strings containing feedback on the code.
  """

  feedback = []

  # Check for potential bugs.
  for pattern in [r"if \w+ = \w+", r"while \w+ = \w+"]:
    matches = re.findall(pattern, code)
    for match in matches:
      feedback.append("Potential bug: {}. Use == instead of =.".format(match))

  # Check for unused code.
  for pattern in [r"\w+ = \w+;", r"\w+\(\)"]:
    matches = re.findall(pattern, code)
    for match in matches:
      feedback.append("Unused code: {}".format(match))

  # Check for style violations.
  for pattern in [r"\s{2,}", r"\t"]:
    matches = re.findall(pattern, code)
    for match in matches:
      feedback.append("Style violation: {}".format(match))

  return feedback

# Example usage:

code = """
if x = 10:
  print("x is equal to 10")
y = 10
def foo():
  pass
print(y)
"""

feedback = review_code(code)

for item in feedback:
  print(item)
