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

``` bash
git add . && git commit -m 'update Readme.md'
```

``` bash
git remote add origin https://github.com/ReshmaChikate5/simple-dvc-demo.git
```

``` bash
git branch -M main
 ```

``` bash  
git push -u origin main
```


