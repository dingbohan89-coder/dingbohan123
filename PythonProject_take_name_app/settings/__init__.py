from datetime import timedelta


DB_URI = "mysql+aiomysql://root:200601@127.0.0.1:3306/sqlalchemy_demo?charset=utf8mb4"


# 邮箱相关配置
MAIL_USERNAME="1537955880@qq.com"
MAIL_PASSWORD="aygniyulczecjihf"
MAIL_FROM="1537955880@qq.com"
MAIL_PORT=587
MAIL_SERVER="smtp.qq.com"
MAIL_FROM_NAME="丁博涵发送的验证码"
MAIL_STARTTLS=True
MAIL_SSL_TLS=False


JWT_SECRET_KEY = "sfsadadafsjw"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

