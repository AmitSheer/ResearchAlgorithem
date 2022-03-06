import importlib
import sys

in_script_name: str = sys.argv[1]
out_script_name = sys.argv[2]

# with open(in_script_name,'r+') as file:
#     content = file.read()
#     module = eval(content)
#     print(module)


print(f'{in_script_name}')
print(f'{out_script_name}')
print(__import__(__name__+'\\'+in_script_name))
