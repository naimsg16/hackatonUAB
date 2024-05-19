from setuptools import setup, find_packages

setup(
    name='pypitranslatorpackage',
    version= '0.0.1'
    description= "package that translate ur code to ur preference idiom"
    author= "Naim", "Lluc", "Nataly"
    install_requires = ['re', 'deep_translator', 'GoogleTranslator']
)