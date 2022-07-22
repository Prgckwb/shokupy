import shokupy as sp


def main():
    word = "2番"

    menus = sp.get_all_menus()
    results = sp.search(menus, word)

    uma_ni = results[0]
    print(uma_ni)

    print(uma_ni.is_available())


if __name__ == '__main__':
    main()
