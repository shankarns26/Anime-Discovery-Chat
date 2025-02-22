from flask import Flask, render_template, request, jsonify
import requests
import random
import time

app = Flask(__name__)

# Dictionary to store genre IDs from MyAnimeList
GENRE_MAP = {
    'action': 1,
    'adventure': 2,
    'comedy': 4,
    'drama': 8,
    'fantasy': 10,
    'horror': 14,
    'mystery': 7,
    'romance': 22,
    'sci-fi': 24,
    'slice of life': 36,
    'sports': 30,
    'supernatural': 37
}

def get_anime_by_genre(genre):
    genre_id = GENRE_MAP.get(genre.lower())
    if not genre_id:
        return {"error": "Genre not found"}
    
    try:
        url = f"https://api.jikan.moe/v4/anime?genres={genre_id}&limit=5&order_by=score&sort=desc"
        response = requests.get(url)
        time.sleep(1)  # Add delay to respect API rate limits
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and data['data']:
                anime_list = data['data']
                return [{"title": anime['title'], 
                        "synopsis": anime['synopsis'],
                        "image_url": anime['images']['jpg']['image_url'],
                        "score": anime.get('score', 'N/A')} 
                        for anime in anime_list]
            return {"error": "No anime found for this genre"}
        return {"error": f"API error: {response.status_code}"}
    except Exception as e:
        return {"error": f"Error fetching anime: {str(e)}"}

def get_anime_info(anime_name):
    try:
        url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"
        response = requests.get(url)
        time.sleep(1)  # Add delay to respect API rate limits
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and data['data']:
                anime = data['data'][0]
                return {
                    "title": anime['title'],
                    "synopsis": anime['synopsis'],
                    "image_url": anime['images']['jpg']['image_url'],
                    "score": anime.get('score', 'N/A'),
                    "episodes": anime.get('episodes', 'N/A'),
                    "status": anime.get('status', 'N/A'),
                    "aired": anime.get('aired', {}).get('string', 'N/A')
                }
        return {"error": "Anime not found"}
    except Exception as e:
        return {"error": f"Error fetching anime info: {str(e)}"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', '').lower().strip()
        request_type = data.get('type', '')

        if request_type == 'genre':
            genre = message.lower()
            if genre in GENRE_MAP:
                anime_list = get_anime_by_genre(genre)
                if "error" not in anime_list:
                    recommendations = "\n\n".join([
                        f" {anime['title']}\n Score: {anime['score']}\n {anime['synopsis'][:150]}..." 
                        for anime in anime_list
                    ])
                    return jsonify({
                        "response": f"Here are some top-rated {genre} anime:\n\n{recommendations}\n\nYou can get more details about any anime by using the Search option!"
                    })
                return jsonify({"response": f"Sorry, I couldn't fetch {genre} recommendations at the moment. Please try again."})
        
        elif request_type == 'search':
            anime_name = message.replace("tell me about", "").strip()
            anime_info = get_anime_info(anime_name)
            if "error" not in anime_info:
                response = (
                    f" {anime_info['title']}\n\n"
                    f" Score: {anime_info['score']}\n"
                    f" Episodes: {anime_info['episodes']}\n"
                    f" Aired: {anime_info['aired']}\n"
                    f" Status: {anime_info['status']}\n\n"
                    f" Synopsis:\n{anime_info['synopsis']}"
                )
                return jsonify({
                    "response": response,
                    "image_url": anime_info['image_url']
                })
            return jsonify({"response": "Sorry, I couldn't find information about that anime. Please check the spelling or try another anime."})
        
        return jsonify({
            "response": "Please use the buttons above to either browse by genre or search for a specific anime!"
        })
    
    except Exception as e:
        return jsonify({
            "response": "Sorry, I encountered an error. Please try again."
        })

if __name__ == '__main__':
    app.run(debug=True)
