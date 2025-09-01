import subprocess
import sys
import shutil

def pip_install(requirements_file="requirements.txt"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])

def check_ollama_runtime(): 
  #ollama installation check
    if shutil.which("ollama") is None:
        print("\n Ollama runtime not found on your system.")
        print("   Please install Ollama manually from https://ollama.com/download")
        print("   or using your package manager (e.g. `brew install ollama`).\n")
    else:
        None

if __name__ == "__main__":
    pip_install()
    check_ollama_runtime()
