# Colors API test

[![N|Solid](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)](https://nodesource.com/products/nsolid)

This application is a API REST service wich provides colors informations rendered in Json or Xml format. The datas avaible are :
  - The color name
  - The color code
  - The pantom_value
  - A associated date

# Features

  - Search for colors infos by ID number
  - Access colors infos with pagination 
  - GET Json or Xml render

### Tech

Dillinger uses a number of open source projects to work properly:

* [Django 2.2] - Python Django Framework
* [Rest-Framework] - Rest-Framework
* [REST Framework XML] - third-party package


### Installation

To run the application, first download the git repo:

```sh
$ git clone https://github.com/athd92/Api-test-colors
```
Once done, go inside the mysite folder with:
```sh
$ cd mysite
```
then, to start, execute the command:
```sh
$ docker-compose up
```

### Usage

This API REST provides informations about colors. 

Request examples:

Get all colors sorted by id (pagination -> 3 objects per page) in JSON response

```sh
$ http://0.0.0.0:8000/colors/?page=1&format=json
```

Get a specific objet color infos by id and JSON format:

```sh
$ http://0.0.0.0:8000/colors/4/?format=json
```

Get a specific objet color infos by id and XML format:

```sh
$ http://0.0.0.0:8000/colors/4/?format=xml
```

