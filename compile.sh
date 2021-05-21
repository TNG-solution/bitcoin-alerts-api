sudo docker run \
  -it \
  --name btc --rm \
  -p 5000:5000 \
  -v /home/djcharles26/Documents/Python/bitcoin-alerts-api:/home/btc \
  -v /home/djcharles26/Documents/Python/bitcoin-alerts-api/data:/home/btc/data \
  -e RUNTIME=development \
  -e PORT=5000 \
  -e CERVER_RECEIVE_BUFFER_SIZE=4096 -e CERVER_TH_THREADS=4 \
  -e CERVER_CONNECTION_QUEUE=4 \
  tngsolution/btc-alert-api:development /bin/bash