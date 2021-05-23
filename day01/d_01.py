from selenium import webdriver
from time import sleep


# 启动谷歌浏览器哦   版本chromdriver要与谷歌版本一样，且要放到python与谷歌对于的目录下
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

ele = driver.find_element_by_id("kw")

print(ele)

ele.send_keys("腾讯视频")
# get_attribute  获取指定属性值
print(ele.get_attribute("name"))

sleep(3)


driver.quit()
