# tools.py
from build_runner_client import BuildRunnerClient

_runner = BuildRunnerClient()

def run_build() -> dict:
    """
    ビルドを実行する。
    戻り値: { "build_id": str }
    """
    return _runner.run_build()

def get_build_log(build_id: str) -> dict:
    """
    指定されたビルドのログを取得する。
    """
    return _runner.get_build_log(build_id)
