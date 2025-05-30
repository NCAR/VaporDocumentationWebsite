# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import os
import sys
#import sphinx_rtd_theme
import subprocess
import pkgutil

# Ensure sphinxcontrib.googleanalytics and sphinx_copybutton are installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "sphinxcontrib.googleanalytics"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "sphinx_copybutton"])


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# Add vapor_utils to path and vapor_wrf modules for python engine documentation
sys.path.insert(0, os.path.abspath('vaporApplicationReference/otherTools'))
sys.path.insert(0, os.path.abspath('/home/docs/checkouts/readthedocs.org/user_builds/vapor/conda/pythonapi2/lib/python3.9/site-packages/vapor'))
sys.path.insert(0, os.path.abspath('/home/docs/checkouts/readthedocs.org/user_builds/vapordocumentationwebsite/conda/latest'))

# -- Project information -----------------------------------------------------

project = ' '
copyright = '2023 University Corporation for Atmospheric Research'
author = ''

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '3.10.1'

from pathlib import Path
home = str(Path.home())

# Sphinx will not recognize images that are not included as raw html references.
# This creates a file called silent_image_includes.txt that is included in index.rst,
# so the raw html references will be registered.
import textwrap
# get directories
confdir = Path(__file__).parent        # docs/source
src_imgdir = Path(confdir, '_images')  # docs/source/_images
# get image paths & make .rst text
img_exts = ('.png', '.svg')
txt = ""
for file in src_imgdir.iterdir():
    if file.suffix in img_exts:
        txt += """
               .. image:: _images/{}
                 :height: 0px
                 :width: 0px
               """.format(file.name)
# unindent multiline string
txt = textwrap.dedent(txt)
# make a .txt to be `.. include`-ed
with open('silent_image_includes.txt', 'w') as f:
    f.write(txt)

# Breathe was last tried on 9/25/2024.  It was problematic because it would ingest Doxygen's XML output
# as one single file that was thousands of lines long and hard to comprehend on a website.  Doxygen's
# html generator automatically categorizes VAPOR's modules, classes, and namespaces.  Rather than write
# a new script that does this for XML, I've chosen to just re-use the html that is automatically organized
# by Doxygen. -Scott
#breathe_projects = { "VAPOR": home+"/VAPOR/build/doc/xml" }
#breathe_default_project = "VAPOR"

extensions = [
    'sphinx.ext.imgmath', 
    'sphinx.ext.todo', 
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_gallery.gen_gallery',
    'sphinxcontrib.googleanalytics',
    'sphinx_copybutton'
    # 'sphinx_pushfeedback'
    #'breathe'
    #'jupyter_sphinx.execute'
    #'wheel'
]

# pushfeedback_hide_email = True
# pushfeedback_hide_screenshot_button = True
# pushfeedback_button_position = "bottom"

googleanalytics_id = "G-VY29EEZ393"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_static_path = ["_static"]
html_css_files = ["custom.css"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

html_scaled_image_link = False
html_logo = "_images/vaporLogoBlack.png"
html_favicon = "_images/vaporVLogo.png"
html_theme = "sphinx_book_theme"
html_theme_options = dict(
    # analytics_id=''  this is configured in rtfd.io
    # canonical_url="",
    repository_url="https://github.com/NCAR/VAPOR",
    repository_branch="main",
    path_to_docs="doc",
    use_edit_page_button=True,
    use_repository_button=True,
    use_issues_button=True,
    home_page_in_toc=False,
    extra_navbar="",
    navbar_footer_text="",
    extra_footer=""
)

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Vapordoc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Vapor.tex', 'Vapor Documentation',
     'John Clyne, Scott Pearse, Samuel Li, Stanislaw Jaroszynski', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'vapor', 'Vapor Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Vapor', 'Vapor Documentation',
     author, 'Vapor', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

###
### Configure Sphinx-gallery
###

# Download example data 
import requests
simpleNC = home + "/simple.nc"
dataFile = "https://github.com/NCAR/VAPOR-Data/raw/main/netCDF/simple.nc"
response = requests.get(dataFile, stream=True)
with open(simpleNC, "wb") as file:
  for chunk in response.iter_content(chunk_size=1024):
    if chunk:
      file.write(chunk)

# Set plotly renderer to capture _repr_html_ for sphinx-gallery
try:
    import plotly.io as pio
    pio.renderers.default = 'sphinx_gallery'
except ImportError:
    pass

# suppress warnings
import warnings

# filter Matplotlib 'agg' warnings
warnings.filterwarnings("ignore",
                        category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                        ' non-GUI backend, so cannot show the figure.')

# filter seaborn warnings
warnings.filterwarnings("ignore",
                        category=UserWarning,
                        message='As seaborn no longer sets a default style on'
                        ' import, the seaborn.apionly module is'
                        ' deprecated. It will be removed in a future'
                        ' version.')

# Configure sphinx-gallery plugin
from sphinx_gallery.sorting import ExampleTitleSortKey

sphinx_gallery_conf = {
    'examples_dirs': ['dataFormatRequirements/netCDF', 'vaporApplicationReference/imageRenderer'],  # path to your example scripts
    'gallery_dirs': ['dataFormatRequirements/netCDF/examples', 'vaporApplicationReference/imageRenderer'],  # path to where to save gallery generated output
    'within_subsection_order': ExampleTitleSortKey,
    'matplotlib_animations': True,
}

#
# Create Python API Reference materials
#

userModules = [
    'renderer',
    'animation',
    'annotations',
    'camera',
    'dataset',
    'session',
    'transferfunction',
    'transform'
]

devModules = [
    'cmake',
    'common',
    'config',
    'cppyyDoxygenWrapper',
    'link',
    'params',
    'smartwrapper'
]

condaPrefix = str(os.environ.get('CONDA_PREFIX'))
pwd = str(os.path.dirname(os.path.realpath(__file__)))

devModulesCommand = "sphinx-apidoc -f --separate --output-dir " + pwd + "/pythonAPIReference/devModules " + condaPrefix + "/lib/python3.9/site-packages/vapor "
for module in userModules:
    devModulesCommand += condaPrefix + "/lib/python3.9/site-packages/vapor/" + module + ".py "
print("devModulesCommand " + devModulesCommand)
ret = subprocess.run(devModulesCommand, capture_output=True, shell=True)

# Replace sphinx-apidoc default header name
with open(pwd + "/pythonAPIReference/devModules/vapor.rst", 'r+') as f:
    content = f.read().splitlines(True)
    content[0] = "Developer Modules\n"
    content[1] = "=================\n"
with open(pwd + "/pythonAPIReference/devModules/vapor.rst", 'w') as f:
    f.writelines(content)

userModulesCommand = "sphinx-apidoc -f --separate --output-dir " + pwd + "/pythonAPIReference/userModules " + condaPrefix + "/lib/python3.9/site-packages/vapor "
for module in devModules:
    userModulesCommand += condaPrefix + "/lib/python3.9/site-packages/vapor/" + module + ".py "
print("userModulesCommand " + userModulesCommand)
ret = subprocess.run(userModulesCommand, capture_output=True, shell=True)
print("userModulesResult " + str(ret.stdout.decode()))

# Replace sphinx-apidoc default header name
with open(pwd + "/pythonAPIReference/userModules/vapor.rst", 'r+') as f:
    content = f.read().splitlines(True)
    content[0] = "User Modules\n"
    content[1] = "============\n"
with open(pwd + "/pythonAPIReference/userModules/vapor.rst", 'w') as f:
    f.writelines(content)
