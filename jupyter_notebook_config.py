
# Set the Access-Control-Allow-Origin header
# 
# Use '*' to allow any origin to access your server.
# 
# Takes precedence over allow_origin_pat.
c.NotebookApp.allow_origin = '*'

# The IP address the notebook server will listen on.
c.NotebookApp.ip = '*'

# The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = '/home/fenrihen/Uygulamalar/Miniconda3-3.16/Defterler'

# Whether to open in a browser after starting. The specific browser used is
# platform dependent and determined by the python standard library `webbrowser`
# module, unless it is overridden using the --browser (NotebookApp.browser)
# configuration option.
c.NotebookApp.open_browser = False

# Hashed password to use for web authentication.
# 
# To generate, type in a python/IPython shell:
# 
#   from notebook.auth import passwd; passwd()
# 
# The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = u'sha1:091efb0015f0:09f13f39981cc1ae85f73919bc2b85abd80e7aaa'

# The port the notebook server will listen on.
c.NotebookApp.port = 8888

# extra paths to look for Javascript notebook extensions
# c.NotebookApp.extra_nbextensions_path = ["home/fenrihen/Uygulamalar/Miniconda3-3.16/share/jupyter/nbextensions"]

