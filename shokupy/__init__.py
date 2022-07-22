from typing import Union

import requests

from shokupy.menu import ShokujinMenu
from shokupy.utils import URL, MenuString


def get_all_menus(only_available: bool = False) -> list[ShokujinMenu]:
    if only_available:
        json_menus = requests.get(URL.menu_today).json()
    else:
        json_menus = requests.get(URL.menu_all).json()

    menus = []
    for json_menu in json_menus:
        menu = ShokujinMenu(
            menu_id=json_menu[MenuString.ID],
            name=json_menu[MenuString.NAME],
            price=json_menu[MenuString.PRICE],
            category=json_menu[MenuString.CATEGORY],
            day_start=json_menu[MenuString.DAY_START],
            day_end=json_menu[MenuString.DAY_END],
            can_weekday=json_menu[MenuString.CAN_WEEKDAY],
            description=json_menu[MenuString.DESCRIPTION],
        )
        menus.append(menu)
    return menus


def search(target_menus: list[ShokujinMenu],
           menu_name: str,
           min_price: int = 0,
           max_price: int = 99999) -> list[ShokujinMenu]:
    assert min_price <= max_price

    menus = []
    for menu in target_menus:
        in_budget = min_price <= menu.price <= max_price
        if menu.contains(menu_name) and in_budget:
            menus.append(menu)
    return menus


# menuを受け取って整形する
def menu_description(menus: Union[ShokujinMenu, list[ShokujinMenu]]):
    menus_list = []

    if type(menus) is ShokujinMenu:
        menus_list.append(menus)
    elif type(menus) is list:
        menus_list = menus
    else:
        raise ValueError

    for menu in menus_list:
        if menu.day_start == "":
            print("期間指定なし")
        else:
            print(f"{menu.day_start} ~ {menu.day_end}")

        print(f"{menu.name}: {menu.price}円", end="\n\n")


if __name__ == '__main__':
    pass
