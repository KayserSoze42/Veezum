import os, requests
from typing import List

from Veezum.veezum import Veezum

ids: List[str] = [id for id in os.environ["veezum_ids"].replace(" ", "").split(",")]
times: List[str] = [time for time in os.environ["veezum_times"].replace(" ", "").split(",")]

token: str = os.environ["veezum_token"]

print(token)

veezum = Veezum(ids, times, token)

veezum.checkOnce()

veezum.scheduleBot()

veezum.keepChecking()
