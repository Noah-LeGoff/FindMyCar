from models.enums import FuelType, GearboxType

from services.ranking.ranking_service import RankingService
from services.scoring.scoring_engine import ScoringEngine

from tests.factories import make_listing, make_search


def test_pipeline_can_score_single_listing():
    engine = ScoringEngine()

    result = engine.compute(
        make_search(),
        make_listing(),
    )

    assert 0 <= result.total <= 100


def test_pipeline_can_score_multiple_listings():
    engine = ScoringEngine()

    listings = [
        make_listing(),
        make_listing(price=8_000),
        make_listing(price=12_000),
    ]

    results = engine.compute_all(
        make_search(),
        listings,
    )

    assert len(results) == 3


def test_ranking_returns_descending_scores():
    engine = ScoringEngine()
    ranking = RankingService()

    scored = engine.compute_all(
        make_search(),
        [
            make_listing(price=5_000),
            make_listing(price=10_000),
            make_listing(price=15_000),
        ],
    )

    ranked = ranking.rank(scored)

    assert all(
        ranked[i].score.total >= ranked[i + 1].score.total
        for i in range(len(ranked) - 1)
    )


def test_breakdowns_are_preserved():
    engine = ScoringEngine()

    score = engine.compute(
        make_search(),
        make_listing(),
    )

    assert score.compatibility_breakdowns
    assert score.opportunity_breakdowns


def test_listing_matching_fuel_scores_higher():
    engine = ScoringEngine()

    search = make_search(
        fuel=FuelType.GASOLINE,
    )

    gasoline = engine.compute(
        search,
        make_listing(
            fuel=FuelType.GASOLINE,
        ),
    )

    diesel = engine.compute(
        search,
        make_listing(
            fuel=FuelType.DIESEL,
        ),
    )

    assert gasoline.total > diesel.total


def test_listing_matching_gearbox_scores_higher():
    engine = ScoringEngine()

    search = make_search(
        gearbox=GearboxType.MANUAL,
    )

    manual = engine.compute(
        search,
        make_listing(
            gearbox=GearboxType.MANUAL,
        ),
    )

    automatic = engine.compute(
        search,
        make_listing(
            gearbox=GearboxType.AUTOMATIC,
        ),
    )

    assert manual.total > automatic.total


def test_listing_under_budget_scores_higher():
    engine = ScoringEngine()

    search = make_search(
        max_price=10_000,
    )

    cheap = engine.compute(
        search,
        make_listing(
            price=9_000,
        ),
    )

    expensive = engine.compute(
        search,
        make_listing(
            price=15_000,
        ),
    )

    assert cheap.total > expensive.total


def test_listing_matching_year_scores_higher():
    engine = ScoringEngine()

    search = make_search(
        min_year=2018,
    )

    recent = engine.compute(
        search,
        make_listing(
            year=2020,
        ),
    )

    old = engine.compute(
        search,
        make_listing(
            year=2012,
        ),
    )

    assert recent.total > old.total


def test_listing_matching_mileage_scores_higher():
    engine = ScoringEngine()

    search = make_search(
        max_mileage=100_000,
    )

    low_mileage = engine.compute(
        search,
        make_listing(
            mileage=80_000,
        ),
    )

    high_mileage = engine.compute(
        search,
        make_listing(
            mileage=180_000,
        ),
    )

    assert low_mileage.total > high_mileage.total


def test_ranking_keeps_best_listing_first():
    engine = ScoringEngine()
    ranking = RankingService()

    search = make_search(
        fuel=FuelType.GASOLINE,
        gearbox=GearboxType.MANUAL,
        max_price=10_000,
    )

    best_listing = make_listing(
        fuel=FuelType.GASOLINE,
        gearbox=GearboxType.MANUAL,
        price=9_000,
    )

    worst_listing = make_listing(
        fuel=FuelType.DIESEL,
        gearbox=GearboxType.AUTOMATIC,
        price=20_000,
    )

    ranked = ranking.rank(
        engine.compute_all(
            search,
            [
                worst_listing,
                best_listing,
            ],
        )
    )

    assert ranked[0].listing == best_listing


def test_all_scores_remain_between_zero_and_one_hundred():
    engine = ScoringEngine()

    results = engine.compute_all(
        make_search(),
        [
            make_listing(price=5_000),
            make_listing(price=8_000),
            make_listing(price=12_000),
            make_listing(price=18_000),
            make_listing(price=25_000),
        ],
    )

    assert all(
        0 <= scored.score.total <= 100
        for scored in results
    )