# fake_llm_server.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()


class ChatRequest(BaseModel):
    messages: List[Dict[str, Any]]
    tools: List[Dict[str, Any]] | None = None


@app.post("/v1/chat/completions")
async def chat(req: ChatRequest):
    return {
        "id": "dummy",
        "object": "chat.completion",
        "model": "gpt-4o-mini-2024-07-18",
        "choices": [
            {
                "index": 0,
                "finish_reason": "tool_calls",
                "message": {
                    "role": "assistant",
                    "content": "",
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "type": "function",
                            "function": {
                                "name": "run_build",
                                "arguments": "{}"
                            }
                        }
                    ]
                }
            }
        ]
    }
