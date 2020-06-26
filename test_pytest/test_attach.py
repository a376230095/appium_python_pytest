import allure

#这里是显示纯文本的方式，attachment_type必须是TEXT的类型
def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

#这里是显示HTML，第一个参数是html的代码，估计可以用file，第二个参数是这个html的标题是什么
def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","html测试块",attachment_type=allure.attachment_type.HTML)

#由于图片是一个文件，所以得用attach.file方法，第一个是file的路径，路径是linux的方式，第二个参数指定了name，就是图片的title，第三个是对应的图片的文件类型是PNG
def test_attach_picture():
    allure.attach.file(r"./demo_picture.png",name="这是一个图片",attachment_type=allure.attachment_type.PNG)