from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import click


@dataclass
class Filter(ABC):
    """
    Abstract base class for all filters
    """

    @staticmethod
    @abstractmethod
    def get_params() -> List[click.Parameter]:
        """
        Return a list of Click parameters that this filter accepts.
        """
        pass

    @abstractmethod
    def apply(self, data: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Apply the filter to the given data.
        """
        pass


@dataclass
class ExcludeFilter(Filter):
    """
    Filter that excludes certain keys from the data
    """

    exclude: Optional[List[str]] = field(default=list)

    @staticmethod
    def get_params() -> List[click.Parameter]:
        return [
            click.Option(["--exclude", "-e"], multiple=True, help="Columns to exclude"),
        ]

    def __post_init__(self):
        if len(self.exclude) == 1:
            self.exclude = self.exclude[0].split(",")
        self.exclude = [e.lower() for e in self.exclude]

    def apply(self, data: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Exclude keys based on the given list
        """
        if not self.exclude:
            return data
        return [
            {k: v for k, v in d.items() if k.lower() not in self.exclude} for d in data
        ]
