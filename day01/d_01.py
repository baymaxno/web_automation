from selenium import webdriver


# 启动谷歌浏览器哦   版本chromdriver要与谷歌版本一样，且要放到python与谷歌对于的目录下
driver = webdriver.Chrome()
dri = driver.get("http://localhost:63342/python13-api-test/day01/dabai_html.html?_ijt=71in36058h4idmdqa57kvf5enr")
