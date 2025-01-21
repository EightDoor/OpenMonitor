from PyInstaller import __main__ as pyi

params = [
    '-F',
    '--clean',
    '--noconfirm',
    # '--debug=all',
    '--noupx',
    '--name',
    'OpenMonitor',
    'main.py'
]

pyi.run(params)