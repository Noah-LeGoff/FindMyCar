"""
Application-wide custom exceptions.
"""


class FindMyCarError(Exception):
    """
    Base exception for all FindMyCar specific errors.
    """


class ProviderError(FindMyCarError):
    """
    Raised when a listing provider cannot retrieve listings.
    """


class InvalidListingError(FindMyCarError):
    """
    Raised when a listing cannot be normalized into a valid Listing.
    """


class AIProviderError(FindMyCarError):
    """
    Raised when an AI provider fails to analyze a listing.
    """


class MarketAnalysisError(FindMyCarError):
    """
    Raised when market analysis cannot be performed.
    """