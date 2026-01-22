
import glob

def add_newlines(filename):
    with open(filename, 'r') as f:
        content = f.read()
    formatted = content.replace('><', '>\n<')
    with open(filename, 'w') as f:
        f.write(formatted)

add_newlines('PORTFOLIO SINGLE.php')
print("Formatted PORTFOLIO SINGLE.php")
