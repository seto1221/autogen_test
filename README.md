# autogen_test

AutoGen を使った Rust をビルドする Docker コンテナを実行する AI エージェントの試作品です。

## 概要
AI の要求で Rust プロジェクトをビルドする Docker コンテナが実行されます。

## 実行手順
詳細は以下の記事を参照してください。

[AutoGenを使ってFunction CallingによるRustソースのビルドを試してみた](https://zenn.dev/seto_t/articles/d4ccc2db79bdd4)

### Linux
```
git clone https://github.com/seto1221/autogen_test /work/autogen_test
cd /work/autogen_test
docker build -t build .
python -m venv .venv
.venv/bin/activate
pip install --upgrade pip
pip install uvicorn fastapi autogen-agentchat autogen-ext[openai]
export LOGDIR=/work/autogen_test/log
export PROJDIR=/work/autogen_test/proj
nohup uvicorn fake_llm_server:app --port 8000 > ${LOGDIR}/fake_llm.log 2>&1 &
python main.py
pkill -INT -f [f]ake_llm_server
deactivate
rm -rf ${LOGDIR}
rm -rf __pycache__
rm -rf .venv
docker run --rm -t -v "${PROJDIR}:/work" build clean
docker rmi build
```

### Windows
```
Set-Location C:\work\autogen_test
docker build -t build .
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install uvicorn fastapi autogen-agentchat autogen-ext[openai]
$env:LOGDIR="C:\work\autogen_test\log"
$env:PROJDIR="C:\work\autogen_test\proj"
$proc = Start-Process -PassThru 'uvicorn' 'fake_llm_server:app','--port','8000'
python main.py
$proc | Stop-Process
deactivate
Remove-Item -Recurse ${env:LOGDIR}
Remove-Item -Recurse .\__pycache__
Remove-Item -Recurse .\.venv
docker run --rm -t -v "${env:PROJDIR}:/work" build clean
docker rmi build
```
