# NBCV-api
API that allows you to publish your resume.
> FastAPI version of the old NBCV api.

### Roadmap
#### Current features
* Education
* Job experience
* trainings
* languages
* skills
* portfolio
* Auth and users management

#### In progress
* error management
* No 'happy path' use cases

#### Planned features
* logging and audit functionalities
* more data in each entity
  * media
  * links
  * logos
* containerization
* queues
* front-end consumer

## How to try it
Once cloned, execute in your CLI:

```
cd nbcv-api
uvicorn main:api
```
Then, go to [the docs in OpenAPI](https://localhost:8000/docs) to see the features and try them.

To test the security workflow, you can use [this Postman collection](https://www.getpostman.com/collections/381893ccc42d0b792242).

Keep in mind that this is a work in progress, so you're not going to receive emails. In order to test it fast, look to the server log to copipaste the tokens.

This is **not** a production code. If you want to use this code in your project, **modify the prints in the security/util functions to email the info that is being logged**.