import shokupy as sp


def main():
    word = "豚肉ともやしと春雨"

    menus = sp.get_all_menus()
    menus = sp.search(menus, word)

    sp.menu_description(menus)
    # for menu in menus:
    #     print(menu)


if __name__ == '__main__':
    main()
