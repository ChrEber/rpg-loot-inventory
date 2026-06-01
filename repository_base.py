from abc import ABC, abstractmethod

class LootRepository(ABC):
  @abstractmethod
  def get_all_items(self) -> list[dict]:
    pass
