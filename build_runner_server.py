# build_runner_server.py
import os
import sys
import json
import subprocess
import uuid
from pathlib import Path

LOGDIR = os.environ["LOGDIR"]
PROJDIR = os.environ["PROJDIR"]
IMAGE = "build"

def run_build():
    build_id = str(uuid.uuid4())
    log_dir = Path(LOGDIR)
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / f"build_{build_id}.log"

    with log_file.open("w") as f:
        subprocess.run(
            [
                "docker", "run", "--rm",
                "--network=none",
                "-v", f"{PROJDIR}:/work",
                IMAGE
            ],
            stdout=f,
            stderr=subprocess.STDOUT
        )

    return {"build_id": build_id}

def get_build_log(build_id):
    log_file = Path(LOGDIR) / f"build_{build_id}.log"
    return {"log": log_file.read_text() if log_file.exists() else ""}

def main():
    for line in sys.stdin:
        req = json.loads(line)
        method = req.get("method")

        if method == "run_build":
            res = run_build()
        elif method == "get_build_log":
            res = get_build_log(req.get("build_id"))
        else:
            res = {"error": "unknown method"}

        print(json.dumps(res), flush=True)

if __name__ == "__main__":
    main()
