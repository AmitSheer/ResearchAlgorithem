import importlib
import sys


# sys.path.append('assignment_two')
# in_script_name: str = sys.argv[1]
# out_script_name = sys.argv[2]


def to_html():
    def getContent(loaded_module):
        content = f"<h1>Module {loaded_module.__name__}</h1> {loaded_module.__doc__}"
        for f in loaded_module.__dir__()[8:]:
            func = loaded_module.__getattribute__(f)
            content += f"<h1>Function {f}:</h1><wbr>{func.__doc__}<h3>Annotations:</h3>"
            for param in func.__annotations__:
                content += f"{param}<br>"
        return content

    module = importlib.import_module(in_script_name.removesuffix('.py'))
    html = "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"><html><head><meta " \
           "http-equiv=\"Content-Type\" content=\"text/html; " \
           "charset=utf-8\"><style></style></head><body><div>" + \
           getContent(module) + "</div></body></html>"

    with open(out_script_name, 'w') as file:
        file.write(html)


if __name__ == '__main__':
    in_script_name = "module_example"
    out_script_name = "py_to_html.html"
    to_html()
