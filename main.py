import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from musicas import musicas

def criar_playlist_spotify():
    load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
    username = os.getenv("SPOTIPY_USERNAME")
    playlist_name = "Jantar dos Namorados 2023"
    scope = "playlist-modify-public"
    client_id = os.getenv("SPOTIPY_CLIENT_ID")  # Obtém o client_id do ambiente
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")  # Obtém o client_secret do ambiente
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")  # Obtém a redirect URI do ambiente

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    # Cria a playlist
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)
    playlist_id = playlist["id"]

    # Pesquisa músicas e as adiciona na playlist
    track_uris = []
    for musica in musicas:
        results = sp.search(q=musica, type="track", limit=1)
        if len(results["tracks"]["items"]) > 0:
            track_uris.append(results["tracks"]["items"][0]["uri"])
            # Imprime a música adicionada
            track_info = results["tracks"]["items"][0]
            print("Música adicionada:", track_info["name"], "-", track_info["artists"][0]["name"])

    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

    # Exibe mensagem de sucesso
    print("Playlist criada com sucesso:")
    print("Nome da playlist:", playlist_name)
    print("ID da playlist:", playlist_id)

if __name__ == "__main__":
    criar_playlist_spotify()
