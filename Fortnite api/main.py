from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def clean_text(text):
    # Remove extra spaces and tags
    cleaned_text = ' '.join(text.split())
    return cleaned_text

def get_status(url):
    # Send a GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Create a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with class "component-container border-color is-group"
        elements = soup.find_all(class_="component-container border-color is-group")

        # Create a list to store cleaned data
        status_data = []

        # Iterate through found elements and add their cleaned text to the list
        for element in elements:
            status_data.append(clean_text(element.text))
    else:
        # Handle the error if the request is not successful
        status_data = ["Failed to fetch data from the specified URL."]

    return status_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fortnite_status', methods=['GET'])
def fortnite_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'fortnite_status': {'status': status_data[0]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/epic_games_store_status', methods=['GET'])
def epic_games_store_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'epic_games_store_status': {'status': status_data[1]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/rocket_league_status', methods=['GET'])
def rocket_league_status():
    url = "https://status.epicgames.com/?game=rocket-league"
    status_data = get_status(url)
    return jsonify({'rocket_league_status': {'status': status_data[5]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/epic_online_services_status', methods=['GET'])
def epic_online_services_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'epic_online_services_status': {'status': status_data[8]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/unreal_engine_status', methods=['GET'])
def unreal_engine_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'unreal_engine_status': {'status': status_data[10]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/epic_website_status', methods=['GET'])
def epic_website_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'epic_website_status': {'status': status_data[12]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/developer_portal_status', methods=['GET'])
def developer_portal_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'developer_portal_status': {'status': status_data[8]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/twinmotion_status', methods=['GET'])
def twinmotion_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'twinmotion_status': {'status': status_data[9]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/rocket_league_sideswipe_status', methods=['GET'])
def rocket_league_sideswipe_status():
    url = "https://status.epicgames.com/?game=rocket-league-sideswipe"
    status_data = get_status(url)
    return jsonify({'rocket_league_sideswipe_status': {'status': status_data[6]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/lego_fortnite_status', methods=['GET'])
def lego_fortnite_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'lego_fortnite_status': {'status': status_data[3]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/support_a_creator_status', methods=['GET'])
def support_a_creator_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'support_a_creator_status': {'status': status_data[7]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/ue_marketplace_status', methods=['GET'])
def ue_marketplace_status():
    url = "https://status.epicgames.com/"
    status_data = get_status(url)
    return jsonify({'ue_marketplace_status': {'status': status_data[11]}}), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/api/scrape_images', methods=['GET'])
def scrape_images_api():
    site_url = 'https://universofortnite.com/ru/tienda-de-hoy-en-fortnite/'
    excluded_image_urls = [
        'https://universofortnite.com/wp-content/plugins/gtranslate/flags/24/es.png',
        'https://universofortnite.com/wp-content/uploads/2021/03/Logo-Footer-Universo-Fortnite-300x71.png',
        'https://universofortnite.com/wp-content/uploads/2021/03/pavos-gratis-para-fortnite-168x88.jpg',
        'https://universofortnite.com/wp-content/uploads/2021/03/conseguir-skins-gratis-en-fortnite-168x88.jpg',
        'https://universofortnite.com/wp-content/uploads/2021/03/tienda-de-hoy-fortnite-actualizada-1-168x88.jpg',
        'https://universofortnite.com/wp-content/uploads/2021/03/consejos-para-ganar-en-fortnite-168x88.jpg',
        'https://universofortnite.com/wp-content/plugins/social-media-widget/images/cutout/64/youtube.png',
        'https://universofortnite.com/wp-content/plugins/social-media-widget/images/cutout/64/twitter.png',
        'https://universofortnite.com/wp-content/plugins/social-media-widget/images/cutout/64/facebook.png',
        'https://universofortnite.com/wp-content/uploads/2021/03/Logo-Universo-Fortnite-1.png',
        'https://universofortnite.com/wp-content/uploads/fortnite/item_I%20Still%20Haven',
        'https://universofortnite.com/wp-content/uploads/fortnite/item_Can',
        'https://universofortnite.com/wp-content/uploads/fortnite/item_Nothing'
    ]

    try:
        response = requests.get(site_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        image_urls = []

        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url and img_url not in excluded_image_urls:
                image_urls.append(img_url)

        return jsonify({'image_urls': image_urls})

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Failed to scrape image URLs.'}), 500



if __name__ == '__main__':
    app.run(debug=True)
