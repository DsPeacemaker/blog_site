# Приложение ведения блога на Django

В приложении был реализован функционал:
1. Полнотекстового поиска
2. Система комментариев 
3. Система тэгирования постов по темам
4. Рекомендация постов по эл. почте
5. Новостной RSS-ленты

  На домашней странице можно ознакомиться с последними постами, самыми комментируемыми постами, 
  подписаться на рассылку RSS-ленты с новыми постами, найти похожие посты по тэгам, 
  перейти на следующую страницу приложения
  
-----
![home_page](https://sun9-77.userapi.com/impg/d4EfxzcgoSVgp7MSGK-L4Oa5NNQr_n52VtRS1w/Ah4fqNW4cAk.jpg?size=1280x717&quality=96&sign=e5de4dce0746614bb43ae7b3ad0b7cac&type=album "home")

## Страница поста
На странице поста можно оставить комментарии, поделиться постом по электронной почте.

-----
![post](https://sun9-12.userapi.com/impg/yZmXQPWsYagpVcxRD5V5QOo3Gwz2LVWDGWuh3g/iutcZS4yI2Q.jpg?size=1203x1000&quality=96&sign=d3008c65d2e5f3ed0dd68c1fb1c56ba4&type=album "post")

## Рекомендация по эл. почте

Механизм реализован с помощью STMP-сервера Google. Для использования вам необходимо указать в поле ```EMAIL_HOST_USER``` свою учетную запись (в моем случае Gmail)
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = '********'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```
Если вы не можете использовать STMP-сервер, то можно отправлять рекомендательные письма в консоль раскомментировав следующий настроечный параметр:
```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'```


-----
![share](https://sun9-30.userapi.com/impg/Em3q4PLK47gPG9RT9FtTEFkBOFhtpGk4_dGHHQ/yDLnSgbHilM.jpg?size=664x503&quality=96&sign=6e82f16222b79efc7738e88cd969ce87&type=album "share")


-----
![search](https://sun9-57.userapi.com/impg/8RapDMSBLQpONIQqfaWP464Oh09m9_1sJ-x30w/9nTA2ihC-x0.jpg?size=674x382&quality=96&sign=502b140bca822a206b129b9ef7d26848&type=album "search")



-----
![RSS](https://sun9-77.userapi.com/impg/VD4ylRC6J0Gvy4QyG5wNCrMFSU_Dk2sVrBtZMw/R2qewuYdEn8.jpg?size=1198x690&quality=96&sign=a266cd2f9b511474e683a3ed68d44f4a&type=album "RSS")
