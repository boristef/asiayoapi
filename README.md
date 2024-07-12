# Order Processing API

這是一個使用 Flask 框架開發的訂單處理 API，負責接收訂單資料並進行驗證和轉換。

## 功能特色

- **訂單驗證：** 使用 `OrderValidator` 類別進行訂單資料的驗證，包括名稱、價格和貨幣格式的檢查。
- **資料轉換：** 透過 `OrderService` 類別將訂單資料格式化為標準格式，並進行匯率轉換（如果適用）。
- **錯誤處理：** 在驗證和轉換過程中，若有任何錯誤，將返回相應的 HTTP 錯誤碼和錯誤訊息。

## SOLID 原則應用

- **單一職責原則（Single Responsibility Principle, SRP）：** 每個類別都專注於一個特定的工作：`OrderValidator` 負責驗證，`OrderService` 負責轉換。
- **開放封閉原則（Open Closed Principle, OCP）：** 透過相依性注入和接口抽象，使得程式碼容易擴展，例如新增其他類型的訂單處理功能。
- **里氏替換原則（Liskov Substitution Principle, LSP）：** 每個類別的方法和行為都符合其base-class（如 `object`）的預期，提供一致的介面。

## 設計模式

- **策略模式：** 在 `OrderService` 中使用了策略模式，根據不同的貨幣類型進行不同的轉換操作。
- **觀察者模式：** 使用 Flask 的 logger 功能，觀察和記錄每次 API 請求的資料流動情況。

## 使用方式

1. 安裝requirements：
   ```bash
   pip install -r requirements.txt

2. 使用 Docker 容器化應用程式：

    建立 Docker 映像：
    ```bash
    docker build -t order-processing-api
    ```
    啟動 Docker 容器：

    ```bash
    docker run -p 5000:5000 order-processing-api
    ```
 3. 發送 POST 請求至 /api/orders 來處理訂單。

範例

    {
    "name": "Product A",
    "price": 50,
    "currency": "USD"
    }

## 使用 Pytest 執行測試

執行所有測試：
```bash
pytest
```

## 錯誤處理
若驗證或轉換過程中出現錯誤，將返回適當的錯誤訊息和 HTTP 狀態碼。