World's Best Volume Control UI
------

Inspired by HN article: https://readhacker.news/s/4QqYJ

Requirements
------

- Python 3.7
- PyQt5
- `pulsectl` PyPI package

You can install these by running:

```
pip3 install -r requirements.txt
```

Or you would prefer to install them manually:

```
pip3 install PyQt5 pulsectl
```

Running
-----

```
./main.py
```

Converting UI file
-----

You may modify the UI file using Qt Creator, and after modification you should convert them to a Python file.

To convert the UI file, simply run:

```
cd ui
pyuic5 mainwindow.ui > mainWindow.py 
```

In case of missing `pyuic5`, you may add `~/.local/bin` or `/usr/local/bin` to your PATH.

License
------

WTFPL
