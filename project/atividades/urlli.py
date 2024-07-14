import urllib.request

pag_open=urllib.request.urlopen("https://gbnymos.github.io/Project-one_piece/")
text=pag_open.read().decode("utf8")
print(text[0:200])