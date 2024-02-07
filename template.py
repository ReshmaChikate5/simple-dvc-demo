import os

dir=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    'notebooks',
    'saved_models',
    'src'
]

for dir_ in dir:
    os.makedirs(dir_,exist_ok=True)
    with open(os.path.join(dir_,'.gitkeep'),'w' ) as f:
        pass

files=[
    'dvc.yaml',
    'param.yaml',
    '.gitignore',
    os.path.join("src","__init__.py")
    ]
for file_ in files:
    with open(file_,'w') as f:
        pass
