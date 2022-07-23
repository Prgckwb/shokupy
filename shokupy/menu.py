import datetime
import re
import textwrap

from shokupy.string import MenuString


class ShokujinMenu:
    def __init__(self, menu_id, name, price, category, day_start, day_end, can_weekday, description):
        self.id: str = menu_id
        self.name: str = name
        self.price: int = int(price)
        self.category: str = category
        self.day_start: str = day_start
        self.day_end: str = day_end
        self.can_weekday: str = can_weekday
        self.description: str = description

    def __str__(self):
        text = f"""\
        [ShokujinMenu]
        {MenuString.ID}: {self.id}
        {MenuString.NAME}: {self.name}
        {MenuString.PRICE}: {self.price}
        {MenuString.CATEGORY}: {self.category}
        {MenuString.DAY_START}: {self.day_start}
        {MenuString.DAY_END}: {self.day_end}
        {MenuString.CAN_WEEKDAY}: {self.can_weekday}
        {MenuString.DESCRIPTION}: {self.description}
        """.replace("\t", "")
        return textwrap.dedent(text)

    # メニュー名、説明に指定した文字列を含むかどうか
    # TODO: 正規表現検索を修正
    def contains(self, word: str, is_regex) -> bool:
        if is_regex:
            r = re.compile(word)
            is_name = bool(re.search(r, self.name))
            is_description = bool(re.search(r, self.name))
        else:
            is_name = word in self.name
            is_description = word in self.description

        return is_name or is_description

    # 現在注文可能かどうか
    def is_available(self) -> bool:
        if self.day_start == "" and self.day_end == "":
            return True

        if self.day_end != "":
            today = datetime.date.today()
            end_time = datetime.datetime.strptime(self.day_end, "%Y-%m-%d")
            menu_end_date = datetime.date(end_time.year, end_time.month, end_time.day)

            if today <= menu_end_date:
                return True

        return False


if __name__ == '__main__':
    pass
