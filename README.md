# Miniconda3-3.16
Python programlama dili ortamı.

## İndirme ve Yükleme
Yerel kullanıcıda:
```bash
wget https://repo.continuum.io/miniconda/Miniconda3-3.16.0-Linux-x86_64.sh
bash Miniconda3-3.16.0-Linux-x86_64.sh
```
Yüklemenin ardından *.bashrc* dosyasına yolu eklemesine onaylanması gerek. Ardından oturumu kapatıp tekrardan giriş yapılır.

## Paketler
```bash
conda config --add channels conda-forge
conda update conda
```
Diğer tüm paketler *conda install <paket-adı>* komutu kullanılarak yüklenebilir.
### jupyter, jupyter_contrib_nbextensions
### numpy
### pymongo

## JupyterNB
Öncelikle kullnılacak olan port için güvenlik duvarından izin açılır.
ˋˋˋbash
sudo ufw allow 8888
ˋˋˋ
Ardından *jupyter_notebook_config.py* doyası oluşturulup aşağıdaki satırlar eklenir
```python
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
```
### <span style=color:red>Jupyter Notebook Eklentileri</span>
Eklentilerin bulunduğu klasör belirlenir.
```python
from IPython.html.services.config import ConfigManager
ip = get_ipython()
cm = ConfigManager(parent=ip, profile_dir=ip.profile_dir.location)
```
#### Eklentileri Aktifleştirme:
```python
cm.update('notebook',{"load_extensions":{"/home/fenrihen/Uygulamalar/Miniconda3-3.16/share/jupyter/nbextensions/runtools/main":True}})
```
#### Eklenti Devre Dışı Bırakma:
```python
cm.update('notebook',{"load_extensions":{"/home/fenrihen/Uygulamalar/Miniconda3-3.16/share/jupyter/nbextensions/runtools/main":None}})
```
İşlem tamamlandıktan sonra tarayıcı yenilenir.
