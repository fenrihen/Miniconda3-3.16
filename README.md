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
