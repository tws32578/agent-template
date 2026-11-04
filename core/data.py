"""입력 데이터 읽기. 문제에서 받은 파일은 data/ 폴더에 그대로 두고(수정 금지) 여기서 읽는다.
이상한 데이터(빈 값, 중복, 음수 등)는 조용히 넘기지 말고 에러로 알린다.
"""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load():
    raise NotImplementedError("TODO: data/의 파일을 읽어서 돌려주세요.")
