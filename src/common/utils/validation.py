import re

GAMBLING_KEYWORDS = [
    "bet", "casino", "poker", "wager", "gambling", "sportsbook", "slots", "jackpot"
]
GAMBLING_MERCHANTS = [
    "bet365", "william hill", "ladbrokes", "coral", "paddy power", "sky bet", 
    "betfair", "888sport", "unibet", "virgin bet", "boylesports", "sportingbet",
    "888casino", "888poker", "grosvenor", "partypoker", "pokerstars", "casumo", 
    "leovegas", "mr green", "rizk", "betway", "jackpotjoy", "bwin"
]

def contains_gambling_activity(descriptions: list[str]) -> bool:
    pattern = "|".join(GAMBLING_KEYWORDS + GAMBLING_MERCHANTS)
    return any(re.search(pattern, desc, re.IGNORECASE) for desc in descriptions)
