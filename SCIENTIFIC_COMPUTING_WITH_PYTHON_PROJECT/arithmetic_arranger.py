#https://replit.com/@mahmoudhussei20/LegitimateNovelKernel#arithmetic_arranger.py
def arithmetic_arranger(problems, show_answers=False):
  # Check if there are too many problems
  if len(problems) > 5:
      return "Error: Too many problems"

  # Check for valid operators
  valid_operators = {'+', '-'}
  for problem in problems:
      operator = problem.split()[1]
      if operator not in valid_operators:
          return "Error: Operator must be '+' or '-'"

  # Check for valid operands
  for problem in problems:
      operands = problem.split()[::2]  # Get all the operands
      for operand in operands:
          if not operand.isdigit():
              return "Error: Numbers must only contain digits"
          if len(operand) > 4:
              return "Error: Numbers cannot be more than four digits"

  # Arrange problems
  arranged_problems = []
  for problem in problems:
      operand1, operator, operand2 = problem.split()
      width = max(len(operand1), len(operand2)) + 2  # Add 2 for the operator and space
      arranged_problems.append(f"{operand1.rjust(width)}")
      arranged_problems.append(f"{operator} {operand2.rjust(width - 2)}")
      arranged_problems.append("-" * width)

  # Show answers if required
  if show_answers:
      answers = []
      for problem in problems:
          answer = str(eval(problem))
          answers.append(answer.rjust(width))
      arranged_problems.extend(answers)

  # Return the result
  return "\n".join(arranged_problems)  # Join the lines with a newline
