hello-sip-pyqt5
======

An example of building a Qt-based GUI app with both Python and C++ interfaces of Qt (PyQt5 and Qt5).
The connection between C++ and Python is based on the SIP tool which is used to make Python bindings for C/C++ code.

Dependencies
------
1. Qt5 v5.9.1: https://www.qt.io/download/
2. SIP 4.19.3: https://www.riverbankcomputing.com/software/sip/download
3. PyQt5 v5.9: https://www.riverbankcomputing.com/software/pyqt/download5

Quick start
------

```bash
$ git clone git@github.com:zanton/hello-sip-pyqt5.git
$ cd hello-sip-pyqt5
$ make
$ python runme.py
```

Quick tips
------

- Ensure PyQt5 modules are included in system's Python path:
  ```bash
  $ export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH
  ```

- src/hello.pro: ensure Qt5's include directory is included in system's include path,
  otherwise add it to INCLUDEPATH variable in src/hello.pro:
  ```bash
  INCLUDEPATH += /opt/Qt5.9.1/5.9.1/gcc_64/include
  ```

- sip/configure.py: ensure PyQt5's SIP include directory and Qt5's include directory are included in system's include path,
  otherwise change to correct paths in sip/configure.py:
  ```bash
  sip_inc_dir = "/usr/local/share/sip/PyQt5"
  qt_inc_dir = "/opt/Qt5.9.1/5.9.1/gcc_64/include"
  ```
