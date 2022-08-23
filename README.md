# Python_Webcrawler_LINEBOT
專案介紹
-
本專案需先創立一個LINE的官方帳號，並連結Ngrok。
當使用者透過LINE發送訊息時，LINE Platform將會進行接收，並且傳遞至LINE Bot執行邏輯運算後
，將透過LINE所提供的Messaging API回應訊息給LINE Platform，最後再將訊息傳遞給使用者。

前置作業
-
**0.To install django:** <br>
```pip install django```

**1.To Create Project:**
```
cd.. your_file_location
django-admin startproject YourProjectName

cd project_location
py manage.py runserver
```
**2.To Create App:**
```
py manage.py startapp appName
```

執行畫面
-
<img width="268" alt="Screenshot 2022-08-23 151455" src="https://user-images.githubusercontent.com/96730369/186095167-540a44fa-6cc4-4535-98fd-c1c59428c0b5.png">
