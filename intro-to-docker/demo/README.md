# Demo: containerizing an application for portability
## Steps
1. Create a REST API with [FastAPI](https://fastapi.tiangolo.com/)
2. Create a Docker image for the API
3. Publish the image to a private image registry (Google Cloud Artifact Registry)
4. Deploy the service on Cloud

## 1. Create a REST API with FastAPI
- Goal: instead of giving users code itself, provide a service interface (REST API) of your program
- If you do not know what API is, spend 5 mins with [this video](https://www.youtube.com/watch?v=-mN3VyJuCjM)
- i.e., If you send a certain request, the task is completed
- e.g., serving machine learning model inference using a Decision Tree
- Use decorators (like```@app.post("/predict")```) to define endpoints
- FastAPI automatically validate the data types if we use ```pydantic```

## 2. Create a Docker image for the API
- Goal: package the entire code for portability
- A Docker container is a standardized, executable unit of software that packages up code and all its dependencies
- Write a Dockerfile that is a blueprint, specifying all the steps necessary to create a complete and runnable application environment within a Docker container

- Building images - the process of building an image based on a Dockerfile
```bash
docker build -t <image name> . # . represents the current directory
```
If you want to run the image locally,

```bash
# -p 8080:8080 maps the local port 8080 to the VM port 8080
docker run -it -p 8080:8080 <image name>
```

- You can send a POST message to the URL (see ```user.py``` file or use Postman)
  - Endpoint: ```http://localhost:8080/predict```
  - Body needs to be a JSON ```{"feature1" : 1, "feature2" : 2, "feature3" : 3, "feature4" : 4}```

## 3. Publish the image to Artifact Registry
- Goal: upload the image to a registry so it can be shared. Here, we assume a private registry (typically used within a corporate), using Google Cloud Artifact Registry
- Follow the steps described in the two sections
    - https://cloud.google.com/build/docs/build-push-docker-image#create_a_docker_repository_in
    - https://cloud.google.com/build/docs/build-push-docker-image#build_an_image_using_dockerfile

Example:
```bash
gcloud artifacts repositories create myinf \
 --repository-format=docker --location=us-west2 \
 --description="Docker repository"

gcloud builds submit --region=us-west2 \
 --tag us-west2-docker.pkg.dev/<project name>/myinf/infser:tag1
```
- Once it's built and registered, you can find the image tag (e.g., ```us-west2-docker.pkg.dev/<project name>/pmyinf/infser:tag1```)

- Note: When you are on an ARM CPU machine (Apple Silicon), this local build will generate an image for the ARM architecture. Google Cloud does not assume the ARM arch and does not accept it in Cloud Run. Make sure you use the 3a step with Cloud Build.

## 4. Deploy the service on Cloud
- Go to Google Cloud "Cloud Run"
- From the Service tab, click "Deploy Container" button
- Container image URL should be the URL to the published image 
  - If you followed 3a, use the tag name (like ```us-west2-docker.pkg.dev/...```)
  - Check the container port matches with the exposed port in your Dockerfile
  - For the Authentication part, select "Allow unauthenticated invocations"
- Once deployed, you can find the service URL (like ```https://infser-image-611571974386.us-west2.run.app```)
- You can send a POST message to the URL (see ```user.py``` file or use Postman)
  - Endpoint: ```https://infser-image-611571974386.us-west2.run.app/predict``` 
  - Body needs to be a JSON ```{"feature1" : 1, "feature2" : 2, "feature3" : 3, "feature4" : 4}```

## References
- Build, tag, and publish an image: https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/