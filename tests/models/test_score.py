from models.score import Score
from models.score_breakdown import ScoreBreakdown


def test_create_empty_score():
    score = Score()

    assert score.compatibility == 0
    assert score.opportunity == 0
    assert score.total == 0
    assert score.breakdown == []


def test_score_contains_breakdown():
    breakdown = ScoreBreakdown(
        criterion="Mileage",
        points=15,
        max_points=20,
        reason="Mileage below 100000 km",
    )

    score = Score(
        compatibility=90,
        opportunity=80,
        total=87,
        breakdown=[breakdown],
    )

    assert len(score.breakdown) == 1
    assert score.breakdown[0] is breakdown
    assert score.breakdown[0].criterion == "Mileage"