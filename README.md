# seatmap

座席の登録と登録されている人の検索が行えるアプリです。

![](https://github.com/KDDI-tech/seatmap-work2/blob/main/doc/img/image.png?raw=true)

## 概要

本システムは2つのデモアプリで構成されます。

- 座席登録アプリ : サーバーに座席を登録するアプリです。
- 座席検索アプリ : 登録されている人の検索をするアプリです。

## デプロイ方法

### 1. 本repoをcloneする

```
git clone git@github.com:KDDI-tech/seatmap.git
```

### 2. データの追加及び削除

本システムではサーバーにあらかじめ学生の情報を登録する必要があります。

データの追加及び削除は以下のファイルを変更します。

- /server/fapi.py

21行目からを以下のようにします。

全て同じ要素数に設定してください。

```
df = pd.DataFrame(data={
    "studentID": ["1人目の学籍番号", "2人目の学籍番号", "3人目の学籍番号",..."n人目の学籍番号"],
    "name": ["1人目の名前", "2人目の名前", "3人目の名前",..."n人目の名前"],
    "seatID": ["", "", "",...""]})
```

削除の場合は任意の要素を削除してください。

### 画像データの追加

画像データを登録するには以下のファイルの追加、変更を行います

- /viewer/img/
- /viewer/index.html

#### /viewer/img/

このフォルダの中に登録したい人物の画像を追加します。

"名前1".png

"名前2".png

.

.

.

"名前n".png

#### /viewer/index.html

119行目からのコードを以下のように変更してください。

```
switch(name){
        case "1人目の名前":
          $img.src = './img/"名前1".png';
          break;
        case "2人目の名前":
          $img.src = './img/"名前2".png';
          break;
        case "3人目の名前":
          $img.src = './img/"名前3".png';
          break;
          .
          .
          .
        case "n人目の名前":
          $img.src = './img/"名前n".png';
          break;
        } 
```

### 3. サーバーを立てる

まずAPIサーバーを起動します
repoのディレクトリをカレントにして、下記コマンドを入力してください。

```
cd server
python3 fapi.py
```

### 4. デプロイする

repoのディレクトリをカレントにして下記コマンドを入力してください。

```
cd app
npm i
npm start
```

上記でサーバーが起動します。
ブラウザから下記にアクセスしてみてください。

- http://localhost:3000/register → 座席登録アプリ
- http://localhost:3000/viewer → 座席検索アプリ

## License

[MITライセンス](https://github.com/KDDI-tech/seatmap/blob/main/LICENSE)です。