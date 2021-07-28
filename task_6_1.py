from requests import utils, get
response = utils.get_unicode_from_response\
    (get('https://d2xzmw6cctk25h.cloudfront.net/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt'))

with open('content.txt', 'w+', encoding='utf-8') as f:
    f.writelines(response)
    f.seek(0)
    for line in f:
        l = line.replace('\n', '').replace('"', '').split(' ')
        result = (l[0], l[5], l[6])
        print(result)
