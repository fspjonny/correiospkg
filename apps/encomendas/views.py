import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def view_encomendas(request):
    return render(request, 'encomendas/encomendas.html')


def rastrear_encomenda(request):
    tracking_code = request.GET.get('tracking_code')

    if tracking_code:
        url = f'https://www.linkcorreios.com.br/{tracking_code}'
        
        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')


            singlepost = soup.find('div', class_='singlepost')

            if singlepost:
                status_items = singlepost.find_all('ul', class_='linha_status')

                tracking_data = []

                for status_item in status_items:
                    status_details = status_item.find_all('li')
                    status_text = [li.get_text(strip=True) for li in status_details]
                    tracking_data.append(status_text)
                return render(request, 'encomendas/encomendas.html', {'tracking_data': tracking_data, 'tracking_code': tracking_code})
        
        else:
            return render(request, 'encomendas/encomendas.html', {'error': 'Erro ao acessar o site de rastreamento.', 'tracking_code': tracking_code})
   
    return render(request, 'encomendas/encomendas.html')


def handler404(request, exception):
    return render(request, 'encomendas/404.html')
