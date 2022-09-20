# 概要

各種APIの仕様をまとめたもの

## 席ロックAPI

**パラメータ定義**
```
PUT　－　席ロックAPI
  クエリ：学籍番号(studentID), 席番号(seatID)
```

**レスポンス定義**
```
Responses　
　Content type：application/json
　
　Code
   200 Success

  Response Content {
             席番号(seatID): string,
             "status": boolean,
             "result": "ok"
  }
```

## 空席確認API

**パラメータ定義**
```
GET　－　空席確認
```

**レスポンス定義**
```
Responses　
　Content type：application/json
　
　Code
   200 Success

　Response Content {
              {"seatNumber": string, "status" boolean},
              {"seatNumber": string, "status" boolean},
              {"seatNumber": string, "status" boolean},
              :
              {"seatNumber": string, "status" boolean},
    }
```

"status": True -> 空席
"status": False -> 使用中

## ID照合API

**パラメータ定義**
```
GET　－　ID照合
　クエリ：カードID(cID)
```

**レスポンス定義**
```
Responses　
　Content type：application/json
　
　Code
   200 Success

　Response Content {
             名前(name)：string,
             学籍番号(studentID): string
    }
　
```

```
Responses　
　Content type：application/json
　
　Code
   401 Unauthorized

　Response Content {
             カードID(cardID): string,
             "massage"："不正なカードID"
    }

```

## 検索API

**パラメータ定義**
```
GET　－　検索
　クエリ：名前(name)
```

**レスポンス定義**
```
Responses　
　Content type：application/json
　
　Code
   200 Success

　Response Content {
             名前(name): string,
             座席ID(seatID)：string
    }
```

```
Responses　
　Content type：application/json
　
　Code
   401 Unauthorized

　Response Content {
             "massage"："その名前の学生は現在出社していません"
    }

```

## 個人情報取得API

**パラメータ定義**
```
GET　－　個人情報取得
　クエリ：座席ID(seatID)
```

**レスポンス定義**
```
Responses　
　Content type：application/json
　
　Code
   200 Success

　Response Content {
             学籍番号(studentID)：string,
             座席ID(seatID)：string,
    }
　
```
