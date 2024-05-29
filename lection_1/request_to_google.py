import requests

# Отправляем GET-запрос к google.com
response = requests.get('https://www.google.com/search?q=speedtest&sca_esv=d312657b286d9ff2&sxsrf=ADLYWILrqNqhwJ74d2kzwRzG2pcyKM1vkw%3A1716401086432&ei=vjNOZtbtGeiNxc8P87e_qAM&ved=0ahUKEwjWxLGo7KGGAxXoRvEDHfPbDzUQ4dUDCA8&uact=5&oq=speedtest&gs_lp=Egxnd3Mtd2l6LXNlcnAiCXNwZWVkdGVzdDIKEAAYgAQYQxiKBTIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLATIIEAAYgAQYywEyCBAAGIAEGMsBMggQABiABBjLAUjxXFDKBVikEnACeAGQAQCYAYUBoAGiBaoBAzIuNLgBA8gBAPgBAZgCCKACwQXCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICBhAAGAcYHsICBxAjGLECGCeYAwCIBgGQBgqSBwMyLjagB90g&sclient=gws-wiz-serp')

# Проверяем, не пустое ли тело ответа
if response.content:
    print('work')
    print(response.content)