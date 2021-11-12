## OMG Blog

### API
https://omg-blog.herokuapp.com/

### Back-office
https://omg-blog.herokuapp.com/admin

*credentials for back-office*  
admin@admin.com   
admin

#### Run project locally

* Install pipenv   
  
* Start the virtualenv
`pipenv shell`   

* Install the dependancies
`pipenv install`

* Start data base
`make migrations`  
`make migrate`

* Run:    
`make run`    

* Create super user
  `make superuser`

* Host server
 `http://localhost:8899/`

* Backoffice 
 ` http://localhost:8899/admin`

#### Shortcuts project management

- `make help`
- `make activate`
- `make deploy`
- `make down`
- `make install`
- `make migrate`
- `make migration`
- `make run`
- `make superuser`

#### API documentation

##### Doc Online
https://documenter.getpostman.com/view/994955/UV5f6tNW


#### Examples

##### Create User
https://omg-blog.herokuapp.com/api/v1/users/
```json
{
    "name": "Cláudio Siervi",
    "email": "c@s.com",
    "password": "123!@qwe"
}
```

##### Login
https://omg-blog.herokuapp.com/api/v1/auth/sign-in/
```json
{
    "email": "c@l.com",
    "password": "admin"
}
```

##### Create Post
https://omg-blog.herokuapp.com/api/v1/posts/
```json
{
    "title": "This is an article title. Not good, not bad.",
    "body": "In the body of the article we write about some thing."

}
```

##### Create Like
https://omg-blog.herokuapp.com/api/v1/likes/
```json
{
    "post": "{{POST_ID}}"
}
```
