options = ['yolov7-ICCV', 'yolov7', 'yolov7-gold']
models = {}

for m in options:
    models[m] = m + '.pt'
print(models)