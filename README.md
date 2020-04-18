[![CircleCI](https://circleci.com/gh/charoleizer/exhibitor.svg?style=svg)](https://circleci.com/gh/charoleizer/exhibitor)
<a href="https://codeclimate.com/github/charoleizer/exhibitor/test_coverage"><img src="https://api.codeclimate.com/v1/badges/0e81e50d6f1219a2603e/test_coverage" /></a>
[![Maintainability](https://api.codeclimate.com/v1/badges/0e81e50d6f1219a2603e/maintainability)](https://codeclimate.com/github/charoleizer/exhibitor/maintainability)

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
