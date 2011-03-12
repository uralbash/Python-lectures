# coding: utf-8
#В следующем примере программа принимает большой файл и, чтобы пользователь 
#не скучал, пишет процент от выполненной загрузки и предполагаемое 
#оставшееся время:

FILE = 'boost-1.31.0-9.src.rpm'
URL = 'http://download.fedora.redhat.com/pub/fedora/linux/core/3/SRPMS/' + FILE

def download(url, file):
  import urllib, time
  start_t = time.time()

  def progress(bl, blsize, size):
    dldsize = min(bl*blsize, size)
    if size != -1:
      p = float(dldsize) / size
      try:
        elapsed = time.time() - start_t 
        est_t = elapsed / p - elapsed
      except:
        est_t = 0
      print "%6.2f %% %6.0f s %6.0f s %6i / %-6i bytes" % (
          p*100, elapsed, est_t, dldsize, size)
    else:
      print "%6i / %-6i bytes" % (dldsize, size)
  
  urllib.urlretrieve(URL, FILE, progress)

download(URL, FILE)    

