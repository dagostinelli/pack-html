[![Build Status](https://travis-ci.org/dagostinelli/pack-html.png?branch=master)](https://travis-ci.org/dagostinelli/pack-html)

# pack-html

A cool Python program that can turn a web page with all its dependencies into a single file.

# Usage

```
$ pack-html index.html > index_packed.html
```

It also accepts pipes

```
$ cat index.html | pack-html - > index_packed.html
```
