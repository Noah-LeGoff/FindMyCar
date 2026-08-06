from models.analysis.analysis_bundle import AnalysisBundle
from models.score.factor_score import FactorScore

from services.scoring.factors.score_factor import ScoreFactor


class ReliabilityFactor(ScoreFactor):
    def compute(
        self,
        analysis: AnalysisBundle,
    ) -> FactorScore:
        return FactorScore(
            name="Reliability",
            score=0.0,
            explanation="Not implemented",
        )