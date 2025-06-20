from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen = True)
class Pilota:
    driverId: int
    driverRef: str
    number: Optional[int]
    code: Optional[str]
    forename: str
    surname: str
    dob: date
    nationality: str
    url: str

    def __hash__(self):
        # Hash basato su identificativo univoco
        return hash(self.driverId)

    def __eq__(self, other):
        if not isinstance(other, Pilota):
            return NotImplemented
        return self.driverId == other.driverId

    def __repr__(self):
        return (f"Pilota(driverId={self.driverId}, driverRef='{self.driverRef}', number={self.number}, "
                f"code='{self.code}', forename='{self.forename}', surname='{self.surname}', "
                f"dob={self.dob}, nationality='{self.nationality}', url='{self.url}')")

    def __str__(self):
        return f"{self.forename} {self.surname} ({self.nationality}) - nato il {self.dob.strftime('%Y-%m-%d')}"
