def teste_site(site):
    import requests
    try:
        requests.get(site).status_code
        print('site online! ')
    except:
        print('site offile! ')

teste_site('https://www.youtube.com')