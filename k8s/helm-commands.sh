helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add my-repo https://charts.bitnami.com/bitnami

helm install mysql bitnami/mysql --values values/mysql.yaml
helm install redis bitnami/redis --values values/redis.yaml
helm install prometheus prometheus-community/kube-prometheus-stack