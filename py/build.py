from PyInstaller import __main__ as pyi

params = [
    '-F',
    '--clean',
    '--noconfirm',
    # '--debug=all',
    '--noupx',
    'main.py'
]

pyi.run(params)