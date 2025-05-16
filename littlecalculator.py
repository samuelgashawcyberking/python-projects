#user guide line
calhelp = '''user guide: choose the letter for calculation:
- For addition, input A
- For subtraction, input B
- For multiplication, input M
- For division, input D'''
print(calhelp)

#opreation choice and input number
letter=input("input the opration letter  ")
correct_lett= letter.capitalize()
x=int(input("x= "))
y=int(input("y= "))

#self built opreation
def add(a,b):
  ad=a+b
  return ad
def sub(a,b):
  su=a-b
  return su
def mult(a,b):
  M=a*b
  return M
def div(a,b):
  Di=a/b
  return Di

#condition
if correct_lett=='A' :
  solution=add(x,y)
  print(f'solution {solution}')
elif correct_lett== "B":
  solution=sub(x,y)
  print(f'solution  is {solution}')
elif correct_lett== "M":
  solution=mult(x,y)
  print(f'solution  is {solution}')
elif correct_lett== "D":
  solution=div(x,y)
  print(f'solution  is {solution}')
else:
  print(" no solution")

