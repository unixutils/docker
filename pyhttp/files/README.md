# APPLICATION FILES

## writeIndex.py
This python script is packaged in the docker image and run at entry point,  when container is started. The purpose of this script is to start a http server and serve index.html. The contents of index.html are the various objects used as a part of the deployed container, such as config maps, secrets and env variables as a demonstration of the objects themselves.

This script may evolve, keeping in mind that the main purpose of the PyHTTP project is to explore kubernetes only.
