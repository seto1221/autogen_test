# main.py
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool
from tools import run_build, get_build_log

# ツール定義
run_build_tool = FunctionTool(
    name="run_build",
    description="ビルドを実行する",
    func=run_build,
)

get_build_log_tool = FunctionTool(
    name="get_build_log",
    description="ビルドログを取得する",
    func=get_build_log,
)

# モデルクライアント
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key="dummy",
    base_url="http://localhost:8000/v1",
)

# AssistantAgent を定義
assistant = AssistantAgent(
    name="build_assistant",
    model_client=model_client,
    system_message="""
あなたはソフトウェア開発支援エージェントです。
ビルドが必要な場合のみ run_build を呼びます
""",
    tools=[
        run_build_tool,
        get_build_log_tool,
    ],
)

async def main():
    result = await assistant.run(
        task="試しにビルドを実行してください。"
    )
    # ToolCallSummaryMessage から content を抽出して表示
    for msg in result.messages:
        print(msg.content)

if __name__ == "__main__":
    asyncio.run(main())
