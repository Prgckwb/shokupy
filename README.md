# shokupy

[食神API](https://github.com/shokujinjp/api)の非公式PythonSDK

絶賛開発中なので、仕様が度々変わります。

欲しい機能案がありましたらissueに投げてください。

## 使用例(2022/07/23現在)

### メニュー名から検索

```python
import shokupy as sp

word = "春雨"

menus = sp.get_all_menus()
results = sp.search(menus, word)

sp.menu_description(results)
```

```text
期間指定なし
麻婆春雨定食: 650円

期間指定なし
豚肉と太春雨炒め定食: 780円

2019-01-07 ~ 2019-01-13
豚肉とキャベツと春雨のピリ辛炒め定食: 590円

2019-04-29 ~ 2019-05-05
豚肉ともやしと春雨のピリ辛炒め定食: 590円

(省略)

2022-06-06 ~ 2022-06-12
豚肉とえのきと春雨のピリ辛炒め定食: 650円

2022-06-27 ~ 2022-07-03
豚肉ともやしと春雨のピリ辛炒め定食: 650円
```
### jsonを取得して存在しないメニューを生成
```python
import shokupy as sp

j_data = sp.get_json(sp.Endpoint.joke)
data = sp.dict2menu(j_data)

print(data)
```

## ドキュメント

### hoge
- `Endpoint`クラスにはjsonデータのあるURLが格納
- `ShokujinMenu`クラスはメニューを扱いやすくする便利クラス
