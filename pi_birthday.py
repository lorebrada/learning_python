from pathlib import Path

path = Path('python_txt/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form of ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first 30 digits of pi!")
else:
    print("Your birthday does not appear in the first 30 digits of pi!")
