# ub-paste

A handy tool helping you paste your file content to [ubuntu pastebin](pastebin.ubuntu.com)

# Installation

Installation via `pip`

```
pip install ub-paste
```

# Uasge

Just specify a file

```
ub-paste [filepath]
```

Examples:

```
ub-paste test.py
```

```
ub-paste /tmp/Main.java
```

![](https://s11.postimg.org/p47f1breb/ub-paste-demo.gif)

`ub-paste` will paste their contents to [ubuntu pastebin](pastebin.ubuntu.com) and then automatically open the web page in the browser.

Additionally, `ub-paste` can automatically detect the language by the filename extension. If it encounters an unknown filename extension, it will handle the file as a normal text file.

# Available Options

`-a` or `--author` The author name shown on the post (defaults to your username on your computer)

`-n` or `--no-browser` Disallow the program to open the browser after pasting (defaults to 'False')
