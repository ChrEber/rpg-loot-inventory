from abc import ABC, abstraktmethod

class LootRepository(ABC):
  @abstractmethod
  def get_all_items(self) -> list:
    pass
