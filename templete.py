import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

PROJECT_NAME = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/_init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templetes/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        #logging.info(f"Creating directory; {filedir} for the file: {filename}")
        logging.info("Creating directory; %s for the file: %s", filedir, filename)

    if (not os.path.exists(filename)) or (os.path.getsize(filepath) ==0):
        with open(filepath, "w") as f:
            logging.info("Creating empty file; %s ", filepath)

    else:
        logging.info("%s is already exists", filename)
