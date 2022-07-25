import json
from typing import Union

import requests

from shokupy.menu import ShokujinMenu
from shokupy.string import MenuString, Endpoint


def dict2menu(json_menu: dict):
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
    return menu


def get_all_menus(only_available: bool = False) -> list[ShokujinMenu]:
    if only_available:
        json_menus = requests.get(Endpoint.menu_today).json()
    else:
        json_menus = requests.get(Endpoint.menu_all).json()

    menus = []
    for json_menu in json_menus:
        menu = dict2menu(json_menu)
        menus.append(menu)
    return menus


def get_json(url):
    return requests.get(url).json()


def get_json_str(url, is_formatted=False, indent=4, ensure_ascii=False):
    data = requests.get(url).json()

    if is_formatted:
        data = json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)
    else:
        data = json.dumps(data, ensure_ascii=ensure_ascii)

    return data


# TODO: 正規表現検索がうまくいってない
# TODO: exclude引数を実装 (リストで渡して、検索結果から除外)
def search(target_menus: list[ShokujinMenu],
           menu_name: str,
           min_price: int = 0,
           max_price: int = 99999,
           exclude: list[str] = None,
           is_regex: bool = False) -> list[ShokujinMenu]:
    assert min_price <= max_price

    menus = []
    for menu in target_menus:
        # 指定した金額の範囲内かチェック
        in_budget = min_price <= menu.price <= max_price
        if menu.contains(menu_name, is_regex) and in_budget:
            menus.append(menu)

    # TODO: exclude処理

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
