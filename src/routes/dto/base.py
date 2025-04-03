from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
R = TypeVar('R')

class DTOMapper(ABC, Generic[T, R]):
    @abstractmethod
    def to_response(self, entity: T) -> R:
        """Map entity to response DTO"""
        pass
