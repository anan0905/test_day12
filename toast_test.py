"""
对文件管理器进行返回操作, 获取toast提示信息
获取思路: 通过显示文本内容定位目标元素, 再获取其 text 属性值
"""
# 导包
import time

from appium import webdriver

# 实例化驱动对象
from selenium.webdriver.support.wait import WebDriverWait

capabilities = {
    "platformName": "Android",  # 设备类型(Android / iOS)
    "platformVersion": "5.1.1",  # 系统版本
    "deviceName": "模拟器",  # 设备名称
    "appPackage": "com.cyanogenmod.filemanager",  # 待测应用的包名
    "appActivity": ".activities.NavigationActivity",  # 待测应用的启动名
    # 解决中文无法输入问题
    'resetKeyboard': True,
    'unicodeKeyboard': True,
    # 获取toast控件信息(toast控件的获取方法由Uiautomator2提供支持)
    "automationName": "Uiautomator2"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

# com.cyanogenmod.filemanager/.activities.NavigationActivity

# 调用返回键
driver.keyevent(4)

# 显示等待
element = WebDriverWait(driver, 3, .3). \
    until(lambda x: x.find_element_by_xpath('//*[contains(@text, "再次点击")]'))
print(element.text)

# 通过目标元素文本信息定位
# element = driver.find_element_by_xpath('//*[contains(@text, "再次点击")]')

# 展示页面
time.sleep(3)
# 退出驱动对象
driver.quit()