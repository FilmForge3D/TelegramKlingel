import subprocess, sys
from pathlib import Path

here = Path(__file__).parent
subprocess.run(["git", "pull"], check=True, cwd=here)
subprocess.run([sys.executable, "klingel.py"], check=True, cwd=here)