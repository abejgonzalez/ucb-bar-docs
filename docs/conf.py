# -*- coding: utf-8 -*-
#
# Chipyard documentation build configuration file, created by
# sphinx-quickstart on Fri Mar  8 11:46:38 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import subprocess
import datetime

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx_search.extension',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'UC Berkeley Architecture Research Project Landing Page'
copyright = str(datetime.now().year) + ', Berkeley Architecture Research'
author = u'Berkeley Architecture Research'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

on_rtd = os.environ.get("READTHEDOCS") == "True"
on_gha = os.environ.get("GITHUB_ACTIONS") == "true"

if on_rtd:
    for item, value in os.environ.items():
        print("[READTHEDOCS] {} = {}".format(item, value))

# Come up with a short version string for the build. This is doing a bunch of lifting:
# - format doc text that self-references its version (see title page). This may be used in an ad-hoc
#   way to produce references to things like ScalaDoc, etc...
# - procedurally generate github URL references using via `gh-file-ref`
if on_rtd:
    rtd_version = os.environ.get("READTHEDOCS_VERSION")
    rtd_project = os.environ.get("READTHEDOCS_PROJECT")
    if rtd_version in ["stable", "latest"]:
        # get the latest git tag (which is what rtd normally builds under "stable")
        # this works since rtd builds things within the repo
        process = subprocess.Popen(["git", "describe", "--exact-match", "--tags"], stdout=subprocess.PIPE)
        output = process.communicate()[0].decode("utf-8").strip()
        if process.returncode == 0:
            version = output
        else:
            version = "v?.?.?" # this should not occur as "stable" is always pointing to tagged version
    else:
        version = rtd_version # name of a branch

    rtd_main_project = rtd_main_project # in this case, this is the main project
    # add two dialogs to search (one of just this project, one of all projects)
    rtd_sphinx_search_filters = {
        "Search UCB BAR Landing Page": f"project:{rtd_project}/{rtd_version}",
        "Search all UCB BAR Projects": f"subprojects:{rtd_main_project}/{rtd_version}",
    }
    # default to searching all projects
    rtd_sphinx_search_default_filter = f"subprojects:{rtd_main_project}/{rtd_version}"
elif on_gha:
    # GitHub actions does a build of the docs to ensure they are free of warnings.
    # Looking up a branch name or tag requires switching on the event type that triggered the workflow
    # so just use the SHA of the commit instead.
    version = os.environ.get("GITHUB_SHA")
    rtd_version = "stable" # default to stable when not on rtd
else:
    # When running locally, try to set version to a branch name that could be
    # used to reference files on GH that could be added or moved. This should match rtd_version when running
    # in a RTD build container
    process = subprocess.Popen(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE)
    output = process.communicate()[0].decode("utf-8").strip()
    if process.returncode == 0:
        version = output
    else:
        raise Exception("git rev-parse --abbrev-ref HEAD returned non-zero")
    rtd_version = "stable" # default to stable when not on rtd

# for now make these match
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
    'logo_only': True,
#    'display_version': True,
#    'navigation_depth': 4,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
        'css/custom.css',
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

# TODO: change
html_logo = '_static/images/chipyard-logo.png'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ucbbardoc'

# -- Misc Options ---------------------------------------------------------

html_context = {
    "version": version
}

# add rst to end of each rst source file
# can put custom strings here that are generated from this file
rst_epilog = f"""
.. |overall_version| replace:: {version}
"""

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ucbbardoc.tex', u'UC Berkeley Architecture Research Landing Page',
     u'Berkeley Architecture Research', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ucbbardoc', u'UC Berkeley Architecture Research Landing Page',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ucbbardoc', u'UC Berkeley Architecture Research Landing Page',
     author, 'ucbbardoc', 'Research landing page.',
     'Miscellaneous'),
]




# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python' : ('https://docs.python.org/', None)}

# resolve label conflict between documents
autosectionlabel_prefix_document = True

extlinks = { }
