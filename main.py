import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from musicas import musicas

def criar_playlist_spotify(number_of_songs):
    load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
    username = os.getenv("SPOTIPY_USERNAME")
    playlist_name = "Jantar dos Namorados"
    scope = "playlist-modify-public"
    client_id = os.getenv("SPOTIPY_CLIENT_ID")  # Obtém o client_id do ambiente
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")  # Obtém o client_secret do ambiente
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")  # Obtém a redirect URI do ambiente

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    # Verifica se a playlist já existe
    playlist_id = obter_playlist_existente(sp, username, playlist_name)

    if playlist_id:
        atualizar_playlist(sp, username, playlist_id, number_of_songs)
    else:
        criar_nova_playlist(sp, username, playlist_name, number_of_songs)

def obter_playlist_existente(sp, username, playlist_name):
    playlists = sp.user_playlists(user=username)
    for playlist in playlists["items"]:
        if playlist["name"] == playlist_name:
            return playlist["id"]
    return None

def atualizar_playlist(sp, username, playlist_id, number_of_songs):
    playlist_tracks = sp.playlist_items(playlist_id=playlist_id)
    existing_track_uris = set(item["track"]["uri"] for item in playlist_tracks["items"])

    track_uris = []
    for musica in musicas:
        if musica not in existing_track_uris:
            results = sp.search(q=musica, type="track", limit=1)
            if len(results["tracks"]["items"]) > 0:
                track_uris.append(results["tracks"]["items"][0]["uri"])

    for i in range(0, len(track_uris), number_of_songs):
        sp.playlist_add_items(playlist_id=playlist_id, items=track_uris[i:i+number_of_songs])

    # Exibe mensagem de sucesso
    print("Playlist atualizada com sucesso:")
    exibir_playlist_info(sp, playlist_id, len(track_uris))

def criar_nova_playlist(sp, username, playlist_name, number_of_songs):
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)
    playlist_id = playlist["id"]

    track_uris = []
    for musica in musicas:
        results = sp.search(q=musica, type="track", limit=1)
        if len(results["tracks"]["items"]) > 0:
            track_uris.append(results["tracks"]["items"][0]["uri"])

    for i in range(0, len(track_uris), number_of_songs):
        sp.playlist_add_items(playlist_id=playlist_id, items=track_uris[i:i+number_of_songs])

    # Exibe mensagem de sucesso
    print("Playlist criada com sucesso:")
    exibir_playlist_info(sp, playlist_id, len(track_uris))

def exibir_playlist_info(sp, playlist_id, total_tracks):
    playlist = sp.playlist(playlist_id=playlist_id)
    print("Nome da playlist:", playlist["name"])
    print("ID da playlist:", playlist["id"])
    print("Total de músicas na playlist:", total_tracks)

if __name__ == "__main__":
    try:
        number_of_songs = int(input("Digite o tamanho dos lotes de músicas a serem adicionados: "))
        if number_of_songs <= 0 or number_of_songs > 50:
            raise ValueError("O tamanho dos lotes de músicas deve estar entre 1 e 50.")
        criar_playlist_spotify(number_of_songs)
    except ValueError as e:
        print("Erro:", str(e))
    except spotipy.exceptions.SpotifyException as e:
        print("Erro ao acessar o Spotify:", str(e))
    except Exception as e:
        print("Ocorreu um erro:", str(e))
