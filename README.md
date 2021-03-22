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

#### In progress
* error management
* No 'happy path' use cases

#### Planned features
* auth
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
