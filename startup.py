import subprocess, sys
from pathlib import Path

here = Path(__file__).parent

# Attempt to auto-update from remote, discarding local changes to avoid merge conflicts
try:
    subprocess.run(["git", "fetch", "origin"], check=True, cwd=here, capture_output=True)
    subprocess.run(["git", "reset", "--hard", "origin/main"], check=True, cwd=here, capture_output=True)
except subprocess.CalledProcessError:
    # If update fails, continue anyway - better to run stale code than crash
    pass

# Start the bot - if this fails, the service will restart
subprocess.run([sys.executable, "klingel.py"], check=True, cwd=here)