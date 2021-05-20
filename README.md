# 가상환경 생성 후 runserver 방법/순서

**1. 폴더 순서**
```
+-- DegreeProject
    +-- SWM_api
        +-- 가상환경
        +-- Study_with_Me (이 폴더 안에 clone받는다)
    +-- SWM_android
```
상위 폴더를 하나 만들고 그 안에 clone받을 폴더를 하나 더 만든다.

**2. SWM_api폴더 안에서 가상환경 생성**
![가상환경](https://user-images.githubusercontent.com/62804036/118931468-05da1f00-b982-11eb-8d63-b4433726435e.JPG)
- python -m venv myvenv (myvenv라는 이름으로 가상환경 생성)
- dir (myvenv라는 폴더가 생긴것 확인 가능)
- cd myvenv/Scripts (가상환경 폴더 안으로 이동)
- activate  (가상환경 활성화)

**2. 런서버**
![image](https://user-images.githubusercontent.com/62804036/118932014-89940b80-b982-11eb-9ac2-a754d8735fac.png)
<br>귀찮지만 runserver는 manage.py가 있는 폴더 선상에서 구동하므로 cd 명령어로 폴더 이동을 해줘야함.
