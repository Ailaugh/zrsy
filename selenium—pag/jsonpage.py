import os, re
from mogodbpage import table
def mogo():
    root = 'D:\Desktop\zrsy\zrsy_list'
    file_list = os.listdir(root)
    for file in file_list:
        content = open('D:\Desktop\zrsy\zrsy_list\{}'.format(file), 'r', encoding='utf-8')
        a = content.read()
        img_list = re.findall('"offerPicUrl":"(.*?)"', a)  # 图片链接
        sale_list = re.findall('"saleQuantity":"(.*?)"', a)  # 销量
        price_list = re.findall('"price":"(.*?)"', a)  # 价格
        simp_list = re.findall('"simpleSubject":"(.*?)"', a)  # 标题

        base_url = 'https://m.1688.com/offer/'
        id_url = re.findall('"id":"([0-9]{3,})"', a)
        memberId_url = re.findall('"memberId":"(.*?)"', a)

        url_list1 = []  # 商品的url
        if id_url and memberId_url:
            for id, me in zip(id_url, memberId_url):
                url_list = base_url + id + '.html?spm=' + me
                url_list1.append(url_list)

        for title, img, price, sale, url in zip(simp_list, img_list, price_list, sale_list, url_list1):
            y = {'title': title, 'img': img, 'price': price, 'sale': sale, 'url': url,'from_url':url[0:18]}
            table.insert(y)

# mogo()