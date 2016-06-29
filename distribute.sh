#!/usr/bin/sh

python3 setup.py bdist_wheel &&\
gpg2 --detach-sign -a dist/ghPublish-$1-py3-none-any.whl &&\
twine upload dist/ghPublish-$1-py3-none-any.whl dist/ghPublish-$1-py3-none-any.whl.asc &&\
mkdir dist/$1 &&\
mv dist/ghPublish-$1-* dist/$1 || "Failed"
