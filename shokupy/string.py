import dataclasses


@dataclasses.dataclass
class MenuString:
    ID = "id"
    NAME = "name"
    PRICE = "price"
    CATEGORY = "category"
    DAY_START = "day_start"
    DAY_END = "day_end"
    CAN_WEEKDAY = "can_weekday"
    DESCRIPTION = "description"


@dataclasses.dataclass
class Endpoint:
    BASE = r"https://api.shokujin.jp"
    MENU_ALL = rf"{BASE}/menu/all"
    MENU_TODAY = rf"{BASE}/menu/today"
    JOKE = rf"{BASE}/joke/markov"
