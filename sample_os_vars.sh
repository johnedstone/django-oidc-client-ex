# Sample only - OS variables needed - put this file outside your project

export SOURCE_REPOSITORY_URL=git@github.com:namespace/repository # Use for origin/openshift
export CONTEXT_DIR=directory_path # Use for origin/openshift if needed
export APPLICATION_DOMAIN=vanity_url # User for origin/openshift. This optional for origin/openshift.
export PIP_PROXY=ip:port # Use when behind a firewall

export DEBUG='off' # Use for production. Not needed for localhost
export ALLOWED_HOSTS=your_app.com # Use for production webserver. For localhost and origin/openshift use defaults
export SECRET_KEY='your_secret_key' # Django SECRET_KEY, not needed for localhost
export ADMIN_URL=your_custom_adm_url # default is admin

export OP_NAME=your-creative-name-for-your-OP-config
export SCOPE='openid profile email' # Provided by your OP, this is a sample
export AUTHORIZATION_ENDPOINT='https://op-fqdn/...' # Provided by your OP
export TOKEN_ENDPOINT='https://op-fqdn/...' # Provided by your OP
export USERINFO_ENDPOINT='https://op-fqdn/...' # Provided by your OP
export ISSUER='https://op-fqdn' # FQDN of your OP
export JWKS_URI='https://op-fqdn/...' # Provided by your OP
export CLIENT_ID='client_id' # Provided by your OP
export CLIENT_SECRET='passwd' # Provided by your OP
export REDIRECT_URIS='http://your_app.com/openid/callback/login/' # Set by the pip package - django-oidc
export POST_LOGOUT_REDIRECT_URIS='http://your_app.com/openid/callback/logout/' # Set by the pip package - django-oidc - not sure if all OPs use this
