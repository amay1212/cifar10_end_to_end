import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = 'cifar10Project'
#print(f"this is the project {project_name}")
lst_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for file_path in lst_files:
    filePath = Path(file_path)
    filedir, file_name = os.path.split(filePath)
    print(filedir, file_name)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file {file_name}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open (filePath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filePath}")
    else:
        logging.info(f"File already exists!!")