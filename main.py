import shokupy as sp


def main():
    word = "春雨"

    menus = sp.get_all_menus()
    results = sp.search(menus, word)

    sp.menu_description(results)


if __name__ == '__main__':
    main()
