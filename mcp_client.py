# mcp_client.py
import subprocess
import json

class BuildRunnerClient:
    def __init__(self):
        self.proc = subprocess.Popen(
            ["python", "build_runner_stdio.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )

    def _call(self, payload):
        self.proc.stdin.write(json.dumps(payload) + "\n")
        self.proc.stdin.flush()
        return json.loads(self.proc.stdout.readline())

    def run_build(self):
        return self._call({"method": "run_build"})

    def get_build_log(self, build_id):
        return self._call({"method": "get_build_log", "build_id": build_id})
