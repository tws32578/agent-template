"""[고정] 웹 서버. 핵심 전략 내용을 전혀 모르고, core/run.py의 결과를 JSON으로 돌려줄 뿐이다.
실행: python web/app.py   →  http://localhost:8000  (0.0.0.0 바인딩)

[용어]
- 엔드포인트: 서버가 응답하는 주소 (예: GET /api/run/v1)
- JSON: 서버와 브라우저가 주고받는 텍스트 데이터 형식
- 상태코드: 200 성공 / 404 없는 대상
- 0.0.0.0: 이 컴퓨터의 모든 네트워크 주소에서 접속을 받음 (127.0.0.1은 자기 자신만)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))          # core 폴더를 import할 수 있게

from fastapi import FastAPI, HTTPException  # noqa: E402
from fastapi.responses import FileResponse  # noqa: E402

from core import run as core  # noqa: E402
from core.rules import RULES  # noqa: E402

app = FastAPI()


@app.get("/")
def index():
    return FileResponse(Path(__file__).parent / "index.html")


@app.get("/api/info")
def info():
    return {"versions": core.versions(), "rules": RULES}


@app.get("/api/run/{name}")
def run_one(name: str):
    try:
        return core.run(name)
    except KeyError as e:
        raise HTTPException(404, str(e))


@app.get("/api/compare")
def compare():
    return core.compare()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
