<div align="center">
  <img alt="Logo" src="./frontend/src/assets/logo.png">
  <h1>Vue3 + Django</h1>
  <span>中文 | <a href="README-EN.md">English</a></span>
</div>

## 簡介

這是一個基於 `Vue3` 和 `Django` 開發的專案，目的是實際體驗並展示 Vue3 和 Django 所帶來的開發便利性。這是我自畢業以來首次採用前後端分離的開發模式，跳脫紙本知識真正體會到何謂 CORS 和 CSRF ，以及使用 Django 的 ORM 取代較熟悉的 SQL 語法，規避 SQL injection 所帶來的風險。

## 功能

#### 後端

###### CRUD

-   **查詢**： 查詢單一資料表全部資料，或者用欄位篩選後的資料
-   **新增**： 新增一筆資料
-   **修改**： 修改一筆現有資料
-   **刪除**： 依照 id 刪除現有資料

###### CheckKPI

-   **查詢總銷量**： 查詢總銷量排行榜前10名
-   **查詢總銷售額**： 查詢總銷售額排行榜前10名

#### 前端

-   **新增客戶、商品、門市**： 新增資料
-   **編輯資料**： 修改客戶或商品或門市的資料
-   **查看績效**： 查看總銷量和銷售額

## 專案版本號

#### 後端

-   **Python**： 3.11.7
-   **Pip**： 23.3.1
-   **Django**： 5.0.3
-   **Django-cors-headers**： 4.3.1
-   **Mssql-django**： 1.4
-   **Pyodbc**： 5.1.0

#### 前端

-   **Node.js**： 20.11.0
-   **Npm**： 10.2.4
-   **Vue3**： 3.2.13
-   **Bootstrap**： 5.3.2
-   **Axios**： 1.6.7
-   **Font Awesome**： 6.5.1

## 資料夾說明

```plaintext
├─ backend              - 後端
│  ├─ DjangoAPI         - 後端Project
│  ├─ CRUD              - 新增、查詢、修改、刪除的APP
│  │  └─ models.py      - 所有APP共用的model
│  └─ CheckKPI          - 較複雜查詢的APP
│
└─ frontend             - 前端
   ├─ public            - 公共資源
   └─ src               - 源代碼
      ├─ assets         - 靜態資源存放處
      ├─ components     - 可重用的Vue組件存放處
      ├─ views          - 主要的應用程式頁面組件
      └─ utils          - 通用的JS工具庫

```

## 安裝開發環境

```bash
# clone專案
git clone https://github.com/chonken/Vue3-Django.git

# 進入專案目錄
cd Vue3-Django
```

#### 啟動後端

```bash
# 進入後端
cd backend

# 還原開發環境
pip install -r requirements.txt

# 啟動
python manage.py runserver
```

#### 啟動前端

```bash
# 進入前端
cd frontend

# 還原開發環境
npm install

# 啟動
npm run serve
```
