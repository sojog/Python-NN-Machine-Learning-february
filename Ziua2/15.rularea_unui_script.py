import subprocess
import os

folder_path = os.getcwd()
print(folder_path)


script = f"ipynb-py-convert {folder_path}/exercitiu_numpy.py {folder_path}/exercitiu_numpy_din_python.ipynb"

subprocess.Popen(script, shell=True)