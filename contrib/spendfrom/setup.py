from distutils.core import setup
setup(name='dmospendfrom',
      version='1.0',
      description='Command-line utility for dmomint "coin control"',
      author='Gavin Andresen',
      author_email='gavin@dmomintfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
