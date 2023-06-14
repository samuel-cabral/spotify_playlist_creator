import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

def criar_playlist_spotify():
    load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
    username = os.getenv("SPOTIPY_USERNAME")
    playlist_name = "Romanticas anos 80"
    scope = "playlist-modify-public"
    client_id = os.getenv("SPOTIPY_CLIENT_ID")  # Obtém o client_id do ambiente
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")  # Obtém o client_secret do ambiente
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")  # Obtém a redirect URI do ambiente

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    # Nova lista de músicas
    musicas = [
        'Jantar dos namorados',
        'Fulminante - Mumuzinho',
        'Camisa 10 - Turma do pagode',
        'A vida é boa com você - Bryan Behr',
        "You're still the one - Shania Twain",
        'De janeiro a janeiro - Roberta Campos e Nando Reis',
        "Livina on' a prayer - Bon Jovi",
        'Perfect - Ed Sheeran',
        'Só hoje - Jota Quest',
        'Um amor puro - Djavan',
        'Slave to love - Brian Ferry',
        'Forever - Kiss',
        'Borbulhas de amor - Fagner',
        'Mágica - Calcinha Preta',
        'Diga sim pra mim - Desejo de Menina',
        'Meu anjo azul - Forró Anjo Azul',
        'Eu te amo tanto - Meninos de barão',
        'Isso é imortal - gatinha manhosa',
        'Feitos um pro outro - Desejo de menina',
        'Pétalas neon - noda de caju',
        'Carta branca - banda magníficos',
        'Manchete nos jornais - Calcinha Preta',
        'De janeiro a janeiro - Limão com mel',
        'Fica comigo - limão com mel',
        'Pra sempre - limão com mel',
        'Pode se achegar - Agnes e Tiago Iorc',
        'Felicidade - Marcelo Jeneci',
        'Parbólicas - Dingo',
        'Layla - Eric Clapton',
        'New light - John Mayer',
        'Só você - Fábio Jr',
        'How deep is your love - Bee Gees',
        'A dama de vermelho - Waldik Soriano',
        'Sentir teu calor - noda de caju',
        "(Everything I do) I do it for you",
        'Heaven - Bryan Adams',
        'The Outfield - Your love',
        'The time of my life - Bill Medley, Jennifer Warnes',
        'Nós dois - Pedro Valença',
        'Não há nada mais lindo do que amanhecer',
        'A dança - Tiago nacarato',
        'De olhos abertos - Pedro Valença',
        'Caneta e papel - os Arrais',
        'Só nos dois - Tim Bernardes',
        'High school musical',
        'Você me faz tão bem - Hélvio Sodré',
        'Um sonho de amor - Edson e Batista Lima',
        'Evidências - Chitãozinho e Xororó',
        'Paraquedas - Gabriel Diniz',
        'Nocaute - Jorge e Mateus',
        'Os anjos cantam - Jorge e Mateus',
        'Está noite foi maravilhosa - Leonardo',
        'É por você que eu canto - Leandro e Leonardo',
        'É você - Marisa Monte',
        'Meet me halfway - Black eyed peas',
        'Milk and toast and honey - Roxette',
        'Hungry eyes - Eric Carmen',
        'Every breath you take - The Police',
        'Sorriso resplandecente - Dragon Ball',
        'Morando do nordeste - Lairton',
        'Eles se amam - Vocal Livre',
        'ALL star - Nando Reis',
        'Ana Vitória',
        'Por onde andei - Nando Reis',
        'Pensando em você - Moska',
        'Por você - Frejat',
        'Meu abrigo - Melim',
        'Olhos certos - Detonautas',
        'Você me faz tão bem - Detonautas',
        "I won't give up - Jason Mraz",
        'Envelhecer com você - Lorena Chaves',
        'Se for com você - Estevão Queiroga',
        'Velha infância - Tribalistas',
        'Sala de reboco - Luiz Gonzaga',
        'Give me love - Ed Sheeran'
    ]

    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)
    playlist_id = playlist["id"]

    track_uris = []
    for musica in musicas:
        results = sp.search(q=musica, type="track", limit=1)
        if len(results["tracks"]["items"]) > 0:
            track_uris.append(results["tracks"]["items"][0]["uri"])

    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

    # Exibe mensagem de sucesso
    print("Playlist criada com sucesso:")
    print("Nome da playlist:", playlist_name)
    print("ID da playlist:", playlist_id)
    print("Músicas adicionadas à playlist:")

    for track_uri in track_uris:
        track_info = sp.track(track_uri)
        print("-", track_info["name"], "-", track_info["artists"][0]["name"])

if __name__ == "__main__":
    criar_playlist_spotify()
