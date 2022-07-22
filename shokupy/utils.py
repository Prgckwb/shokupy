import dataclasses


@dataclasses.dataclass
class URL:
    base = r"https://api.shokujin.jp"
    menu_all = rf"{base}/menu/all"
    menu_today = rf"{base}/menu/today"
    joke = rf"{base}/joke/markov"


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
