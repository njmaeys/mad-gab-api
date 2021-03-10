# mad-gab-api

# Runs a Mad Gab api that you can pull from

### Build
example build version: `0.0.0`
```console
$ docker build -t njmaeys/mad-gab-api:<build version> .
$ docker push njmaeys/mad-gab-api:<build version>
```

### Run it
```console
$ docker pull njmaeys/mad-gab-api:<build version>
$ docker run -d -p 5000:80 njmaeys/mad-gab-api:<build version>
```

# Requests

The base url is: **https://gabs.pandablade.com**

Get all of the mad gabs available  
**/allgabs**

```console
$ curl -X GET https://gabs.pandablade.com/allgabs
```

Response example
```
{
  "data": {
    "gab": {
      "0": "Pretty Shack Scent"
      "1": "Ape Hand Hub Hair"
      ...
    }
    "gabValue": {
      "0": "A British Accent"
      "1": "A Panda Bear"
      ...
    }
  }
}
```
---
Get one mad gab
**/onegabs**

```console
$ curl -X GET https://gabs.pandablade.com/onegabs
```

Response example
```
{
  "data": {
    "gab": "Pretty Shack Scent"
    "gabValue": "A British Accent"
  }
}
```