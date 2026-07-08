from models.score_breakdown import ScoreBreakdown


def test_create_score_breakdown():
    breakdown = ScoreBreakdown(
        criterion="Mileage",
        points=15,
        max_points=20,
        reason="Mileage below 100000 km",
    )

    assert breakdown.criterion == "Mileage"
    assert breakdown.points == 15
    assert breakdown.max_points == 20
    assert breakdown.reason == "Mileage below 100000 km"