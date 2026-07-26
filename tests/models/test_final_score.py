from models.final_score import FinalScore
from models.enums import Recommendation


def make_score(total: float):
    return FinalScore(
        total=total,
        compatibility=0,
        opportunity=0,
        compatibility_breakdowns=[],
        opportunity_breakdowns=[],
    )


def test_exceptional_choice():
    assert make_score(95).recommendation == Recommendation.EXCEPTIONAL


def test_excellent_choice():
    assert make_score(85).recommendation == Recommendation.EXCELLENT


def test_very_interesting():
    assert make_score(70).recommendation == Recommendation.VERY_INTERESTING


def test_worth_considering():
    assert make_score(55).recommendation == Recommendation.WORTH_CONSIDERING


def test_low_interest():
    assert make_score(40).recommendation == Recommendation.LOW_INTEREST


def test_avoid():
    assert make_score(39).recommendation == Recommendation.AVOID