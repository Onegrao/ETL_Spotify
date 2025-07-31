#Funções de Extração de dados
import os # Para 
import spotipy # Para interagir com a API do spotify
from spotipy.oauth2 import SpotifyOAuth # Para autenticação com a API do spotify
from dotenv import load_dotenv # Para carregar variaveis personalizadas do arquivo .env

def get_spotify_data(): 
    load_dotenv() # Carrega as variaveis do arquivo .env

    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="user-read-recently-played"
    ))

def extract_recent_tracks(limit=50):
    #Conecta ao Spotify
    sp = get_spotify_data()

    #Obtem as musicas recentemente tocadas
    results = sp.current_user_recently_played(limit=limit)
    return results['items']