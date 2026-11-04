"""core 테스트. 문제가 정해지면 skip 표시를 지우고 채운다. (채우지 않고 지우면 실패한다)
1) 손계산 테스트: 사람이 답을 아는 아주 작은 입력 → 정확한 기대값 (기대값은 내가 직접 계산)
2) 검사 테스트: 일부러 틀린 결과를 넣으면 check()가 위반을 잡는가
   (check가 항상 []를 돌려주면 모든 버전이 '통과'로 보인다 → 가장 위험한 버그)
"""
import pytest

pytestmark = pytest.mark.skip(reason="TODO: 문제 정의 후 작성")


def test_hand_calc():
    pytest.fail("TODO: 작은 입력과 내가 계산한 기대값")


def test_check_catches_bad_result():
    pytest.fail("TODO: 일부러 규칙을 어긴 결과 → violations가 1건 이상")


def test_check_passes_good_result():
    pytest.fail("TODO: 올바른 결과 → violations가 비어 있음")
