import importlib
import sys

sys.path.append('assignment_two')
in_script_name: str = sys.argv[1]
out_script_name = sys.argv[2]

module = importlib.import_module(in_script_name.removesuffix('.py'))
print(module.__name__)
print()
# print(f'{in_script_name}')
# print(f'{out_script_name}')
# print()
