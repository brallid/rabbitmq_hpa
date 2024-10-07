Build the image
` docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/brando-brando-sandbox/my-repo/rabbitmq-monitor:latest .`

Push the image to Artifact Registry
` docker push us-central1-docker.pkg.dev/brando-brando-sandbox/my-repo/rabbitmq-monitor:latest`
