from seleniumpage import driver
import time
# word=input('请输入商品：')

def urlss(word):
    urls = ['https://m.1688.com/offer_search/-6D7033.html?keywords={}'.format(word)]
    for url in urls:
        print('正在获取{}'.format(url))
        driver.get(url)
        print('已获取完{}'.format(url))
        js_ = "var q=document.documentElement.scrollTop=120000"
        for i in range(6):
            driver.execute_script(js_)
            time.sleep(8)
            print('第{}次已下滑完！！！from_url:{}'.format(i+1,url[0:18]))
        driver.close()
# urlss(word)