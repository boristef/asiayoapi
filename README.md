# Order Processing API

這是一個使用 Flask 框架開發的訂單處理 API，負責接收訂單資料並進行驗證和轉換。

## 功能特色

- **訂單驗證：** 使用 `OrderValidator` 類別進行訂單資料的驗證，包括名稱、價格和貨幣格式的檢查。
- **資料轉換：** 透過 `OrderService` 類別將訂單資料格式化為標準格式，並進行匯率轉換（如果適用）。
- **錯誤處理：** 在驗證和轉換過程中，若有任何錯誤，將返回相應的 HTTP 錯誤碼和錯誤訊息。

## SOLID 原則應用

- **單一職責原則（Single Responsibility Principle, SRP）：**
  - **`NameValidator`** 負責驗證訂單名稱是否僅包含英文字符且首字母大寫。
  - **`PriceValidator`** 負責驗證訂單價格是否為數字且不超過限制。
  - **`CurrencyValidator`** 負責驗證訂單貨幣是否為允許的格式。
  - **`CurrencyTransformer`** 負責將價格從美元轉換為台幣。
  - **`OrderProcessor`** 負責調用所有驗證器和轉換器，並返回最終結果。

- **開放封閉原則（Open Closed Principle, OCP）：**
  - 透過使用抽象和相依性注入，可以輕鬆擴展系統的功能。例如，可以添加新的驗證器或轉換器而不修改現有的代碼。
  - 在 `OrderProcessor` 中使用列表來管理多個驗證器和轉換器，使其可以動態添加或移除處理邏輯。

- **里氏替換原則（Liskov Substitution Principle, LSP）：**
  - 所有的驗證器（如 `NameValidator`、`PriceValidator`、`CurrencyValidator`）和轉換器（如 `CurrencyTransformer`）都實現了相同的方法簽名，因此它們可以互相替換而不會影響 `OrderProcessor` 的行為。
  - 每個驗證器和轉換器都符合其基類（如 `object`）的預期行為，並且提供一致的接口。

- **介面隔離原則（Interface Segregation Principle, ISP）：**
  - 每個驗證器和轉換器都專注於各自的職責，提供了簡單明瞭的接口，避免了不必要的依賴。
  - `OrderProcessor` 只依賴於驗證器和轉換器的必要方法，而不需要關注它們的具體實現。

- **相依反轉原則（Dependency Inversion Principle, DIP）：**
  - 高層模組（如 `OrderProcessor`）不依賴於低層模組的具體實現，而是依賴於抽象（例如，驗證器和轉換器的接口）。
  - 可以通過相依性注入的方式將具體的驗證器和轉換器傳遞給 `OrderProcessor`，從而提高系統的靈活性和可測試性。


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