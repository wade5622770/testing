import requests
response = requests.get("http://www.atguigu.com/images/logo.jpg")
print(type(response))
content = response.content
print(content)
print(type(content))
f = open("logo.jpg","wb")
f.write(content)
f.close()
