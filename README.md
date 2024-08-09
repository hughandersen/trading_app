# Test Trading App

## Introduction    
This is an attempt to create a trading app using Ibeam to connect to IBKR API, and a trading script.  Ibeam is needed because the IBKR API needs a localhost to be authenticated, although IBKR say that this is changing to Auth2.0.       
There is no trading methodology here, just a small script to test the connection.     
The idea is to build a multi-container app, one container hosting Ibeam, and the other hosting the connection script, then this app can run in the cloud.    
The connection between the trading app container and the Ibeam container doesn't work, and has been raised as an issue in the Ibeam Github repo.    

## Method   
1. download the files
2. install Docker desktop
3. create your own env.list with your IBKR paper account credentials
4. pull Ibeam image from Docker
5. create trading app docker image using ``docker build -t test_api_connection:latest -f dockerfile.test_api .``
6. build the multi-container app using ``docker compose -f docker_compose_test_app.yaml up --build``
7. check Docker Desktop to see if the images and containers have been created and are running.

## Next Steps
Once the connection works, write some trading algorithms using a PAPER account.   
