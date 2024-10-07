Build the image
` docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/brando-brando-sandbox/my-repo/rabbitmq-monitor:latest .`

Push the image to Artifact Registry
` docker push us-central1-docker.pkg.dev/brando-brando-sandbox/my-repo/rabbitmq-monitor:latest`

Install Custom Metrics Stackdriver Adapter in your cluster
`kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-stackdriver/master/custom-metrics-stackdriver-adapter/deploy/production/adapter_new_resource_model.yaml`
