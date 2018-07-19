# Flask-Ajax-Practice
利用Flask做為後端框架，練習jquery ajax。

在後端將從前端收到的資料，回傳至前端。

## 關於此專案
打開後會進入一個簡單的登入頁面，帳號/密碼:abc/abc

![alt tag](https://i.imgur.com/7QjntCz.png)

登入成功之後，會看到如下圖的畫面

名稱跟信箱可以任意輸入，接著按 submit，即可成功

![alt tag](https://i.imgur.com/A2naAsh.png)

可以看到使用者按下 submit 後，

以非同步的方式呼叫後端服務器進行資料傳遞，

在此即將輸入的表單資料後方加上 success 並回傳。

而在 ajax 呼叫完畢後，顯示一個 alert，代表成功。

若表單輸入不完整，則回傳 missing data

![alt tag](https://i.imgur.com/yvw6wXg.png)

## 參考資料
### 好不容易找到的範例，並做內化與修改。

[Flask-Login](https://flask-login.readthedocs.io/en/latest/)

[W3school](http://www.w3school.com.cn/jquery/jquery_ref_events.asp)

[Pretty Printed](https://github.com/PrettyPrinted/AJAX_Forms_jQuery_Flask)