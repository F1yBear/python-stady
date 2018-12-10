import yaml

with open("D:/swagger.yaml")as swagger:
    files = yaml.load(swagger)
print(files)
y = yaml.dump(files)
print(y)
