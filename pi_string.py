from pathlib import Path

path = Path('python_txt/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line 

print(pi_string)
print(len(pi_string))

# second type of exercise 

from pathlib import Path

path = Path('python_txt/pi_digits.txt')
contents= path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
