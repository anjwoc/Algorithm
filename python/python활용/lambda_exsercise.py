files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

result = list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files))
print(result)


