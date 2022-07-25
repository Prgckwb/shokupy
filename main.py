import shokupy as sp


def main():
    word = "2番"

    menus = sp.get_all_menus()
    results = sp.search(menus, word)

    # sp.menu_description(results)
    for menu in results:
        print(menu)

if __name__ == '__main__':
    main()
