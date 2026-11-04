"""[고정] 웹과 핵심 전략을 잇는 유일한 통로. 웹은 이 파일의 versions(), run()만 부른다.
run(버전): 데이터 읽기 → 전략 실행(시간 측정) → 검사 → 표 → 하나의 dict
전략이 에러로 죽어도 서버는 죽지 않는다: 에러 메시지를 결과에 담아 돌려준다.
"""
import importlib
import re
import time
import traceback
from pathlib import Path

from core.check import check
from core.data import load
from core.rules import RULES
from core.show import show

CORE_DIR = Path(__file__).resolve().parent


def versions():
    """core/의 v1.py, v2.py … 를 찾아 번호 순으로. 파일을 추가하면 화면에 자동으로 나타난다."""
    names = [p.stem for p in CORE_DIR.glob("v*.py") if re.fullmatch(r"v\d+", p.stem)]
    names.sort(key=lambda n: int(n[1:]))
    return [{"name": n, "note": getattr(importlib.import_module(f"core.{n}"), "NOTE", "")} for n in names]


def run(name):
    if not re.fullmatch(r"v\d+", name) or not (CORE_DIR / f"{name}.py").exists():
        raise KeyError(f"없는 버전: {name}")
    module = importlib.import_module(f"core.{name}")
    out = {"name": name, "note": getattr(module, "NOTE", ""), "error": None, "ms": 0,
           "violations": [], "metrics": {}, "table": {"columns": [], "rows": []}}
    try:
        data = load()
        start = time.perf_counter()
        result = module.solve(data, RULES)
        out["ms"] = round((time.perf_counter() - start) * 1000, 1)
        out.update(check(data, result, RULES))
        out["table"] = show(data, result)
    except Exception as e:  # 화면에 에러를 보여주기 위해 모두 잡는다
        out["error"] = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}"
    return out


def compare():
    """모든 버전을 같은 데이터로 실행. 위반이 적은 순 → 버전 번호 순."""
    results = [run(v["name"]) for v in versions()]
    return sorted(results, key=lambda r: (r["error"] is not None, len(r["violations"])))
