```
docker image build -t onkabu-beapp:latest .
```

```
docker container run -p 8000:8000 -v ${PWD}:/app --name onkabu-beapp onkabu-beapp:latest
```