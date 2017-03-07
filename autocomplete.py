import jedi
source = '''import json; json.l'''
script = jedi.Script(source, 1, 19, '')
script
completions = script.completions()
print(completions)
print('Hello World')
