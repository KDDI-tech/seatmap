# seatmap-work2

座席の登録と登録されている人の検索が行えるアプリです。

![](https://github.com/KDDI-tech/seatmap-work2/blob/main/doc/image/image.png?raw=true)

## 概要

本システムは2つのアプリで構成されます。

- 座席登録アプリ : サーバーに座席を登録するアプリです。
- 座席検索アプリ : 登録されている人の検索をするアプリです。

## デプロイ方法

### 1. 本repoをcloneする

```
git clone git@github.com:KDDI-tech/seatmap-work2.git
```

### 2. サーバーを立てる

まずAPIサーバーを起動します
repoのディレクトリをカレントにして、下記コマンドを入力してください。

```
cd server
python3 fapi.py
```

### 3. デプロイする

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

[MITライセンス](https://github.com/KDDI-tech/seatmap-work2/blob/main/LICENSE)です。


