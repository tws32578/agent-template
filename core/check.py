"""결과 검사 = 검증. 어떤 버전의 결과든 같은 기준으로 잰다.
- violations: 필수 규칙 위반 목록 (문장 하나 = 위반 1건). 비어 있어야 쓸 수 있는 결과
- metrics: 핵심 지표 {이름: 값}. 세 관점을 다 넣는다 → 한쪽만 보면 다른 쪽이 망가진다
    이용자 관점 (대기·소요시간, 불편…) / 운영자 관점 (비용, 자원 수…) / 효율 (활용률…)
"""


def check(data, result, rules):
    violations = []
    metrics = {}
    # TODO: 필수 규칙마다 검사해서 위반이면 violations.append("무엇이 얼마나 틀렸나")
    # TODO: metrics["이름"] = 값
    return {"violations": violations, "metrics": metrics}
