from PyInstaller import __main__ as pyi

params = [
    '-F',
    '--clean',
    '--noconfirm',
    'main.py'
]

pyi.run(params)