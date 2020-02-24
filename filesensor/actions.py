import os

from .factory import ActionFactory

class PrintValues():
    def run(self, path, file_map, details):
        try:
            print(path, dict(file_map), details, details[1])
        except Exception as identifier:
            print(f"error message:{identifier}")


default_actions = {
    'print' : PrintValues()
}