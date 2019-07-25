# ImageOrganizingProgram
### 画像整理用プログラム
### Version1.0.0(正式公開版)
-----
### 使用言語
-python3.7
### 動作環境
windows 10 home
### 使用ライブラリ
- codecs
- datetime
- json
- os
- shutil
- matplotlib
- numpy

### 説明
プログラムを実行すると特定のフォルダーに入れた画像を検出して別のフォルダーにALLフォルダと日付ごとに分類されたDateフォルダーに移動してくれるプログラムです。
windowsのタスクスケジューラー機能で定期的に実行されることを前提としたコードなので相対パスが使えません。(試したところエラーが出た)
ログ機能付き。
おまけの機能として実行すると実行日から5日分の画像数を取得してグラフにし、pngファイルとして吐き出す機能も備わっています。
![サンプル](https://raw.githubusercontent.com/YuumaOwen/ImageOrganizingProgram-/master/sample.png)
