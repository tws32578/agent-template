"""결과를 화면용 표로 바꾼다. 계산하지 않고 '보여줄 모양'만 만든다.
반환: {"columns": [열 이름…], "rows": [[값…], …]}
"""


def show(data, result):
    # TODO: 사람이 결과를 한눈에 확인할 표 (무엇이 어디에/언제/누구에게)
    return {"columns": ["결과"], "rows": [[str(result)]]}
