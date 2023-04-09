import os, requests
from typing import List

from Veezum.veezum import Veezum

ids: List[str] = [id for id in os.environ["veezum_ids"].replace(" ", "").split(",")]
times: List[str] = [time for time in os.environ["veezum_times"].replace(" ", "").split(",")]

token = os.environ["veezum_token"]
response = requests.get(f"https://api.telegram.org/bot{token}/getUpdates").json()

chatID = response["result"][0]["message"]["chat"]["id"]

def test_checkOnce_with_approved_working_ids() -> None:

    veezum = Veezum(ids, times, token)

    assert veezum.checkOnce() == True

def test_checkOnce_with_invalid_id() -> None:

    veezum = Veezum(["INVALID"], ["08:00","16:00"], token)

    assert  veezum.checkOnce() == True

def test_checkOnce_with_not_found_id() -> None:

    veezum = Veezum(["ABCD123456789"], ["08:00","16:00"], token)

    assert veezum.checkOnce() == True

