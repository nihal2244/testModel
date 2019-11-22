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
