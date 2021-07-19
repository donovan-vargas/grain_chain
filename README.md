# Backend developer position challenge

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone `https://github.com/donovan-vargas/grain_chain.git`
$ cd grain_chain
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ make
```
Once `pip` has finished downloading the dependencies
activate virtualenv:

```sh
$ source p/bin/activate
```
File default room matriz (can you edit to test diferents arrays)
```sh
$ data/room.txt
```

run flask server app:

```sh
$ python app.py
```
routes GET

to `http://127.0.0.1:5000/bulbs_status/`.

## routes 
`http://127.0.0.1:5000/bulbs_status/` Returns html template whit results

Can add a new txt in path data/

`http://127.0.0.1:5000/bulbs_status/?filename=<filename>` Returns html template whit results specific filename

## unittest
python -m unittest tests/room_test.py

