Create environment
   ``` command prompt
   python -m venv envpath
   ```

   ``` bash
   conda create -n envname python=3.10.11
   ```

activate environment
   ``` bash
   conda activate envname
   ```

created a requirement.txt file
    ``` bash
    touch requirement.txt
    ```

install the required libraries
``` bash
    pip install -r requirement.txt
```

download the data

https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

``` bash 
git init
```

``` bash
dvc init
```

``` bash
dvc add data_given/winequality.csv
```
``` bash 
git add .
```

``` bash
git commit -m 'first commit'
```
one liner update for readme

``` bash
git add . && git commit -m 'update Readme.md'
```

``` bash
git remote add origin https://github.com/ReshmaChikate5/simple-dvc-demo.git
git branch -M main
git push -u origin main
```

tox command -
```bash
tox
```

for rebuilding -
```bash
tox -r
```

pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

build your own package commands-
```bash
python setup.py sdist bdist_wheel

```
