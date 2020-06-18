import requests
import json
# key = '&key=' + 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
# fields = '&fields=place_id,formatted_address,name,geometry'
# language = '&language=zh-CN'
# place_id = "ChIJO9PO9ATTwoARzNYR9D1MyWU"
# url2 = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=%s%s%s%s' % (place_id, key, language, key)
# res2 = requests.get(url2)
# json_str2 = res2.content.decode()
# data2 = json.loads(json_str2)
# with open('hello' + '_2.json', 'w', encoding='utf-8') as f:
#     json.dump(data2, f, ensure_ascii=False, indent=4)

# key = 'AIzaSyC2VUsehdGp0LS7uZgETWd_OoBA7DpHIYU'
# token = 'CrQCJgEAAIsIomUSkYHnfaiAe7JOD4UmvIS7X8ZrpX21kxFazhDLFtncKzLjgsJLIMmDlDlOwOVpwZdtDB4QPiBeofka2j9RQl6yUgogeV7gbW6qLla3olbcNigRklM3E3qTNBchl1EgS0AiBPjITn09EefsmM7ct2aed_3R_hSQcW8FS0gy0hQkBvxygBF5ALSGp9091bMvavQh3dIhEFQMgofnqK2NbVDqVcBVq8L0DtT1GL_DWh491TtgbP9DzKx9omInof-4zpy2p1tK0U-TaZMMnCfpSLW1bm8e0MQL2UHAn3wzSzkSKgtAQ1HkCMQaSbGK9xsM-qvqtz_LxuaWDQrpWGq56XfgH5rEht8AAYvJtY3Ehg1VQqYuzhAfKsA55eA6iSWn1nVDbFuAxB67Ui-e0dwSEEU6uIVXUwU0CBYXvTQxyfgaFEA303awp31Nz7huW28rdClvpzcb'
# next_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&pagetoken=%s" % (key, token)
# next_res = requests.get(next_url)
# next_json_str = next_res.content.decode()
# next_data = json.loads(next_json_str)
# with open('hello' + '_333.json', 'w', encoding='utf-8') as f:
#     json.dump(next_data, f, ensure_ascii=False, indent=4)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}
proxies = {'http': 'http://lum-customer-sstrade-zone-residential-country-us:4xcrhdlj831p@zproxy.lum-superproxy.io:22225',
            'https': 'https://lum-customer-sstrade-zone-residential-country-us:4xcrhdlj831p@zproxy.lum-superproxy.io:22225'}

res = requests.get(url='http://www.google.com/search?q=mail+@+freudenhaus-online.de&start=0',headers=headers,proxies=proxies)
print(res)