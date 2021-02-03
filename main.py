from selenium import webdriver

url = "https://www.daraz.pk/catalog/?q=cat+food&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937CYCIx2"
driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)

products = driver.find_elements_by_class_name('c2prKC')
i = 1

for product in products:
    name = product.find_element_by_xpath(f'//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[2]/a').text
    price = product.find_element_by_xpath(f'//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[3]/span').text
    try:
        discount = product.find_element_by_xpath(f'//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[4]/span[2]').text
    except Exception as e:
        discount = 'No Discount'
    print(f'{name} | {price} | {discount}')
    i += 1