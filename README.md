# __Pixagram Backend Service API__

This is a python (Python 3.12.0) appication writen using the [FastApi](https://fastapi.tiangolo.com/) framework

This is a simple REST application that allows uploading and commenting on images.

This application has [Frontend](https://github.com/charlesreign/pixa_frontend) that consumes the enpoints exposed

This application uses SQLite for it's database needs

There are eight(8) main api endpoints exposed

| API                   |Purpose                                    |
|-----------------------|-------------------------------------------|
|/user/create           | endpoint for creating new user            |
|/post/create           | endpoint for creating new post            |
|/post/all              | endpoint for getting all posts            |
|/post/image            | endpoint for uploading images             |
|/post/delete/{id}      | endpoint for deleting post base on id     |
|/login                 | login endpoint                            |
|/comment/create        | creating a comment on post endpoint       |
|/comment/all/{post_id} | getting a comment based on id endpoint    |


## __To setup project locally__
Git clone the project onto your local machine. cd into project directory.
create and activate your virtual environment

```
python -m venv venv
source venv/bin/activate (on linux)
.\venv\Scripts\activate (on windows)
pip install --upgrade pip
pip install -r requirements.txt
```
## __To run project__
```
uvicorn main:api
```