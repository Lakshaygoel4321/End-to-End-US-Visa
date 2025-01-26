from pathlib import Path
import os

Project_name = "US_VISA"

file_list = [

    f"{Project_name}/components/__init__.py",
    f"{Project_name}/components/data_ingestion.py",
    f"{Project_name}/components/data_validation.py",
    f"{Project_name}/components/data_transformation.py",
    f"{Project_name}/components/model_trainer.py",
    f"{Project_name}/components/model_evaluation.py",
    f"{Project_name}/components/model_pusher.py"

    f"{Project_name}/configuration/__init__.py"

    f"{Project_name}/constant/__init__.py",

    f"{Project_name}/entity/__init__.py",
    f"{Project_name}/entity/config_entity.py",
    f"{Project_name}/entity/artifact_entity.py",

    f"{Project_name}/exception/__init__.py"

    f"{Project_name}/logger/__init__.py",
    
    f"{Project_name}/pipeline/__init__.py",
    f"{Project_name}/pipeline/training_pipeline.py",
    f"{Project_name}/pipeline/prediction_pipeline.py",

    f"{Project_name}/utils/__init__.py",
    f"{Project_name}/utils/main_utils.py",

    "demo.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",

]

for file in file_list:
    filepath = Path(file)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass

    else:
        print(f"file is laready present at:{filepath}")

