# Setup
1. install deps
    ```bash
    pipenv install
    ```
# Usage
1. Activate working pipenv shell:
    ```bash
    pipenv shell
    ```
2. Run API server
    ```bash
    uvicorn notification_service.receive_token_api:app --reload
    ```
3. To test if API is working:
   ```bash
   curl -i -X POST -H 'Content-Type: application/json' -d '{"token": "something"}' https://thenis.co.uk/receive-token/
   ```

# TODO:
1. vo file `/etc/systemd/system/rundjangoserver.service` prepisat startovaci skript tak, aby to pustalo fastapi
