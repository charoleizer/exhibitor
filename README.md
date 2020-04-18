# exhibitor

## reminder

Build a venv and remove privileges
```sh
$ sudo python3 -m venv venv
$ sudo chown -R user:user venv/
```

Choose the interpreter on IDE and install the packages
```sh
$ pip install -r requirements.txt
```
Run app.py file

Go to http://localhost:5000/graphql test queries

Query example :
```sh
{
  allProduct {
    edges {
      node {
        txName
        txCategory {
          txName
        }
        tx1stBrand {
          txName
        }
        txPlatform {
          txName
        }
      }
    }
  }
}

```
