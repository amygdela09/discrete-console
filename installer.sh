#!/bin/bash

sudo apt-get update
sudo apt-get install proxychains
sudo apt-get install python3
sudo cp discrete-console /bin/
sudo chmod +x /bin/discrete-console
echo Done. Type sudo discrete-console.
