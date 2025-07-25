import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(levelname)s: %(message)s:')


# Below is the template for the project structure.
# project_name = "my_project"

# list_of_files = [
#     ".github/workflows/.gitkeep",
#     f"src/{project_name}/__init__.py",
#     f"src/{project_name}/components/__init__.py",
#     f"src/{project_name}/utils/__init__.py",
#     f"src/{project_name}/utils/common.py",
#     f"src/{project_name}/config/__init__.py",
#     f"src/{project_name}/config/configuration.py",
#     "backend/model.py",
#     "static/app.js",
#     "app.py",
#     "Dockerfile",
#     "README.md",
#     "requirements.txt",
#     "template/index.html",
# ]




list_of_files = [
    ".github/workflows/.gitkeep",
    "backend/ingest_data.py",
    "backend/model.py",
    "static/app.js",
    "static/style.css",
    "app.py",
    ".env",
    "Dockerfile",
    "README.md",
    "requirements.txt",
    "template/index.html",
]

def create_project_structure(project_name: str):
    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                logging.info(f"Creating empty file: {filepath}")
        else :
            logging.info(f"File already exists: {filepath}, skipping creation.")

if __name__ == "__main__":
    project_name = "my_project"
    create_project_structure(project_name)
    logging.info(f"Project structure for '{project_name}' created successfully.")