# Spotify Playlist Creator

Uma aplicação Python simples para criar playlists na sua conta do Spotify.

## Como usar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Clone este repositório para o seu ambiente local.
3. Instale as dependências necessárias executando o seguinte comando:

   ```shell
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na mesma pasta do arquivo `main.py` e adicione as seguintes variáveis:

   ```plaintext
   SPOTIPY_USERNAME=seu-nome-de-usuario
   SPOTIPY_CLIENT_ID=seu-client-id
   SPOTIPY_CLIENT_SECRET=seu-client-secret
   SPOTIPY_REDIRECT_URI=sua-redirect-uri
   ```

   Certifique-se de substituir `seu-nome-de-usuario`, `seu-client-id`, `seu-client-secret` e `sua-redirect-uri` pelas suas informações do Spotify.

5. Execute o seguinte comando para criar a playlist:

   ```shell
   python main.py
   ```

   A playlist "Romanticas anos 80" será criada na sua conta do Spotify e preenchida com músicas românticas dos anos 80.

6. Verifique a saída no console para obter informações sobre a playlist criada e as músicas adicionadas.

---

Sinta-se à vontade para personalizar a lista de músicas no arquivo `main.py` de acordo com suas preferências.

Para obter mais informações sobre como configurar e usar o Spotify Playlist Creator, consulte a documentação do projeto.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou problemas relacionados a este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
