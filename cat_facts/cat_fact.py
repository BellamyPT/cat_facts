from dataclasses import dataclass

@dataclass
class CatFact:
    """Class that describes a cat fact."""
    fact: str
    length: int

    def __repr__(self):
        return self.fact