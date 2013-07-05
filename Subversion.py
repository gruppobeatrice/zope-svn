#
# Subversion.py: funzioni base per l'accesso
# svn via web
#
# Richiede il modulo pysvn per funzionare
# http://pysvn.tigris.org
# (debian package: python-svn)
#
# info, commenti e insulti: Leonardo

from pysvn import Client, depth, node_kind
from StringIO import StringIO

def svn_list(url="svn://localhost/", subpath=""):
    """
        Ritorna una lista di dizionari contenente
        il contenuto della directory corrente
    """

    client = Client()
    items = []
    for i in client.list(url + subpath, depth=depth.immediates):
        d = {}
        for k, v in i[0].items():
           if k == "kind" and v == node_kind.dir:
              d[k] = "dir"
           elif k == "kind" and v == node_kind.file:
              d[k] = "file"
           else:
              d[k] = v
        items.append(d)

    return items

def svn_export(url="svn://localhost/", subpath=""):
    """
        Ritorna un buffer di memoria contenente
        il file richiesto.

        Attualmente non viene fatta distinzione tra
        file binary e file di testo.
    """

    client = Client()
    data = StringIO()

    data.write(client.cat(url + subpath))
    data.seek(0)
    return data
