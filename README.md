# FlatCAM2KitMill
Gcode translation

# Features
- KitMill のための初期化コード追加
- 終了コマンド(M30)の追加
- ncファイルの結合
[!NOTE]
対応するncファイルは，FlatCAMで生成されたGcodeのみ

# How to using
## ncファイルを指定する
```bash
$ python flatcam2kitmill.py -f cutout.nc isolate.nc drill.nc
```
