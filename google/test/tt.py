import requests
import json
token = "CtQDxgEAABbFsbyvBEYEC_9j8D5hGy14MMnFOaE1NvO2HrbT6ynOqETYX7Kgz-NQjoRBgGPYhQN1F-tqnAfKwq4taRnzXJyQDLy9LGjaAyz_RNaFb1OEsLjS4CUjCswowtlJUz7WJ4viVK2y5CWWeWXDcVAM5_NYJq7-a2FUcZSmMcRCDeBbBwadznkMzv9zkY117MVqRWJlZM9uomjzDGeT_ZwuDtjpcfSEE1g4yjZou7y_L7qHsy9V40oXvahCtx0Vl6jxozx6MD--quZ9U3zt809sVWfbEcBdDLFPRlkzfYG92SV6_V8eS-vIauI6mQ_BMhIazR3zUVbTvgJXtnUdKKXxhrRBG-BBu6Ecc1lM2k8HqL9DgHZIfSbC8LvmE7SGjMXCrtUv-pjku5fVSs0BU9gSpm1bOio9kMM2-SJrZQG2gLZy1HH8D_V0YItSnJLe1Z7dWoJcr53oEHTGRgaBxcG-fznxxOaidF5K2kZVi59lv8krpqnVyidIH32ytVMCSuz_MrK2PvDURfUugroZ0CacMTKumK642E2v0HQFxfiMtPMUZiSRJttAlVqkJpNDSiBhHwCm76tdYgilmfEkVlBpgYA_m7JZNui-9rPh5vriq2ijEhB2ZrjlxL98ZG0UOKCeAFnyGhR35LC2tPBvih6RgpNz-xFYtqKfXQ"
key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?%s&pagetoken=' % key  + token
res = requests.get(url)
json_str = res.content.decode()
# print(json_str)
data = json.loads(json_str)
with open('test_place_search.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)