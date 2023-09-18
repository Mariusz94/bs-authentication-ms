# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os,sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
sys.path.append(r'../app/grpc_file')

project = 'python'
copyright = '2023, Dream team'
author = 'Dream team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo','sphinx.ext.viewcode','sphinx.ext.autodoc','sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
latex_elements = {
    'papersize': 'a4paper',         # Format papieru (np. a4paper, letterpaper)
    'classoptions': ',oneside',    # Opcje klasy dokumentu, 'oneside' to jednostronny dokument
    'preamble': r'''
      \usepackage[columns=1]{idxlayout}
    ''' # 1 kolumna w index
}

latex_documents = [('index', 'doc.tex', project, author, 'manual')]
