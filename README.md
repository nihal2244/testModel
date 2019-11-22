# testModel

### project set up
  - if required activate virtual environment

  - install required packages from requirement.txt use
  
```sh
 pip install -r requirement.txt
 ```
  - can run the project with this command after installing packages
  
```sh
python manage.py runserver
```




## API LIST
### END USER

| Name | Method | URL | Payload |
| ------ | ------ |  ------ |------ |
| User Bill List | GET | http://localhost:8000/api/enduser | user_id: 1|
| Upload File | POST | http://localhost:8000/api/enduser|  "id": 25, "user_id": 3, "invoice": "1211w","vender": "qqqqq", "buyer": "aaaaa", "bill_date": "2019-11-22", "bill_items": "dddddd", "bill_path": null, "digitized": false |



### INTERNAL USER
| Name | Method | URL | Payload |
| ------ | ------ |  ------ |------ |
| All Bill List | GET | http://127.0.0.1:8000/api/interuser | user_id: 1|
| Upload File | POST | http://localhost:8000/api/interuser|  "id": 25, "user_id": 3, "invoice": "1211w","vender": "qqqqq", "buyer": "aaaaa", "bill_date": "2019-11-22", "bill_items": "dddddd", "bill_path": null, "digitized": false |
|Retrieve Specific Bill| GET | http://127.0.0.1:8000/api/interuser/10 | None  |
|Update Specific bill| PUT| http://127.0.0.1:8000/api/interuser/10 | "invoice": "#12", "vender": "Ramesh & on Co.", "buyer": "raja","bill_items": "balls","digitized": false |
|Partial Update of Specific bill | PATCH |http://127.0.0.1:8000/api/interuser/<bill id>|"invoice": "#12"(any filed)|
|Delete bill| DELETE| http://127.0.0.1:8000/api/interuser/<bill id> |None|
  
  
  
  
  
  # Mock Data
    
 ```sh
  [
    {
        "id": 1,
        "user_id": 1,
        "invoice": "#12",
        "vender": "Ramesh",
        "buyer": "raja",
        "bill_date": "2019-11-22",
        "bill_items": "balls",
        "bill_path": "/media/billparser/bill%20collection/dummy.pdf",
        "digitized": true
    },
    {
        "id": 2,
        "user_id": 1,
        "invoice": "#12121d",
        "vender": "H&M Co.",
        "buyer": "hari",
        "bill_date": "2019-11-22",
        "bill_items": "qqwqw,wqwqw",
        "bill_path": "/media/billparser/bill%20collection/dummy_tU6CUIu.pdf",
        "digitized": false
    },
    {
        "id": 8,
        "user_id": 1,
        "invoice": "22121",
        "vender": "raj",
        "buyer": "sam",
        "bill_date": "2019-11-22",
        "bill_items": "tv",
        "bill_path": null,
        "digitized": false
    }
]
```
