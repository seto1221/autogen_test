# autogen_test

AutoGen を使った Rust をビルドする Docker コンテナを実行する AI エージェントの試作品です。

## 概要
AI の要求で Rust プロジェクトをビルドする Docker コンテナが実行されます。

## 実行手順

### Linux
```
git clone https://github.com/seto1221/autogen_test /work/autogen_test
cd /work/autogen_test
docker build -t rustc .
python -m venv .venv
.venv/bin/activate
pip install --upgrade pip
pip install uvicorn fastapi autogen-agentchat autogen-ext[openai]
export BUILD_RUNNER_LOGDIR=/work/autogen_test/log
export BUILD_RUNNER_WORKDIR=/work/autogen_test/proj
nohup uvicorn fake_llm_server:app --port 8000 > ${BUILD_RUNNER_LOGDIR}/fake_llm.log 2>&1 &
python main.py
kill -INT `pgrep -f [f]ake_llm_server`
deactivate
rm -rf ${BUILD_RUNNER_LOGDIR}
rm -rf venv
rm -rf __pycache__
docker run --rm -t -v "${BUILD_RUNNER_WORKDIR}:/work" rustc clean
```

### Windows
```
Set-Location C:\work\autogen_test
docker build -t rustc .
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install uvicorn fastapi autogen-agentchat autogen-ext[openai]
$env:BUILD_RUNNER_LOGDIR="C:\work\autogen_test\build_runner_log"
$env:BUILD_RUNNER_WORKDIR="C:\work\autogen_test\proj"
$proc = Start-Process -PassThru 'uvicorn' 'fake_llm_server:app','--port','8000'
python main.py
$proc | Stop-Process
deactivate
Remove-Item -Recurse $env:BUILD_RUNNER_LOGDIR
Remove-Item -Recurse .\.venv\
Remove-Item -Recurse .\__pycache__\
docker run --rm -t -v "${env:BUILD_RUNNER_WORKDIR}:/work" rustc clean
```
