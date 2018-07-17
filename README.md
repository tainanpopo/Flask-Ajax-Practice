# Flask-Ajax-Practice
利用Flask做為後端框架，練習jquery ajax。

在後端將從前端收到的資料，回傳至前端。

並製作一個簡單的登入頁面。

[Demo](https://flask-00.herokuapp.com/) 免註冊的登入帳號/密碼 : flask/flask

[宅男打籃球](https://www.facebook.com/theunderdogsbb/) 圖片皆為宅男打籃球版權所有，順便推薦一下，超好看的啦!

## 關於此專案
註冊後登入即可看見三張輪播圖片

登入後的網站右上角會出現註冊時的 Username

![alt tag](https://i.imgur.com/NRhNLoT.png)

## 建置資料表
檔案中的 Entity.py

初始化

python Entity.py db init

migrate

python Entity.py db migrate

upgrade

python Entity.py db upgrade

## 部署到Heroku
* Procfile

* requirements.txt

* runtime.txt

## 參考資料
### 好不容易找到的範例，並做內化與修改。

[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

[Pretty Printed](https://github.com/PrettyPrinted/AJAX_Forms_jQuery_Flask)

[W3school](http://www.w3school.com.cn/jquery/jquery_ref_events.asp)

[twtrubiks](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)