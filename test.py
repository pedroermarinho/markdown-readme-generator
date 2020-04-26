from generator import infos

data=infos.get_info_readme()
print(data.credits)

for info in data.credits:
    print(info["name"])
    print(info["type"])
    print(info["url"])