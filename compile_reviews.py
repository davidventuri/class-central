import urllib
url = "https://www.class-central.com/mooc/614/edx-stat2-1x-introduction-to-statistics-descriptive-statistics"
f = urllib.urlopen(url)
html = f.read()