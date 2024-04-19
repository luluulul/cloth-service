import requests


def test_get_all_cloths(url: str):
    res = requests.get(url).json()
    assert (res == [{'cloths_id': 1,
                     'name': 'Kany West',
                     'brand': '47',
                     'genre': '1 billion',
                     'price': 'rap, R&B, electronic, gospel'},
                    {'cloths_id': 2,
                     'name': 'Валерий Меладзе',
                     'brand': '58',
                     'genre': '45 millions',
                     'price': 'поп, рок, эстрадная песня'},
                    {'cloths_id': 3,
                     'name': 'Billie Eilish',
                     'brand': '22',
                     'genre': '300 millions',
                     'price': 'rap, pop'},
                    {'cloths_id': 4,
                     'name': 'The Weeknd',
                     'brand': '34',
                     'genre': '700 millions',
                     'price': 'rap, R&B'},
                    {'cloths_id': 5,
                     'name': 'Eminem',
                     'brand': '51',
                     'genre': '1 billion',
                     'price': 'rap, hip-hop'}])


def test_get_cloth_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {'cloths_id': 1,
                    'name': 'Kany West',
                    'brand': '47',
                    'genre': '1 billion',
                    'price': 'rap, R&B, electronic, gospel'})


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/cloths/'
    test_get_cloth_by_id(URL + '1')
    test_get_all_cloths(URL)
