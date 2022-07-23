import shokupy as sp


def main():
    word = "春雨"

    menus = sp.get_all_menus()
    results = sp.search(menus, word)

    sp.menu_description(results)


def play():
    j_data = sp.get_json(sp.Endpoint.joke)
    data = sp.dict2menu(j_data)

    print(data)


if __name__ == '__main__':
    # main()
    play()
