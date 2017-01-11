#!/usr/bin/env bash
# run as sudo
source /home/vagrant/django-oidc-client-ex/unset_os_vars.sh
source /home/vagrant/configurations/django-oidc-client-ex/django_oidc_client_ex.prd.docker.sh

docker run --rm -p 8080:8080 \
-e DEBUG="${DEBUG}" \
-e SECRET_KEY="${SECRET_KEY}" \
-e ALLOWED_HOSTS="${ALLOWED_HOSTS}" \
-e ADMIN_URL="${ADMIN_URL}" \
-e OP_NAME="${OP_NAME}" \
-e SCOPE="${SCOPE}" \
-e AUTHORIZATION_ENDPOINT="${AUTHORIZATION_ENDPOINT}" \
-e TOKEN_ENDPOINT="${TOKEN_ENDPOINT}" \
-e USERINFO_ENDPOINT="${USERINFO_ENDPOINT}" \
-e ISSUER="${ISSUER}" \
-e JWKS_URI="${JWKS_URI}" \
-e CLIENT_ID="${CLIENT_ID}" \
-e CLIENT_SECRET="${CLIENT_SECRET}" \
-e REDIRECT_URIS="${REDIRECT_URIS}" \
-e POST_LOGOUT_REDIRECT_URIS="${POST_LOGOUT_REDIRECT_URIS}" \
--label oidc oidc:latest
