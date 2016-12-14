from weibo import APIClient

APP_KEY = '3820601225' # app key
APP_SECRET = '55d7c61c1f4d1e64ce4aa9caba51c6d9' # app secret
CALLBACK_URL = 'http://12345.com/callback' # callback url


client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

print url
# TODO: redirect to url


# 获取URL参数code:
code = CALLBACK_URL.get('code')
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
# TODO: 在此可保存access token
client.set_access_token(access_token, expires_in)