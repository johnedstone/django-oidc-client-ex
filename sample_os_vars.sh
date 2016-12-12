# Sample only - OS variables needed - put this file outside your project

# Django SECRET_KEY
export SECRET_KEY='your_secret_key'

# Not needed for localhost (default is on), off for prd
# export DEBUG='off'

# Optional for localhost, as default values will probably work
# export ALLOWED_HOSTS=your_app.com

export ADMIN_URL=your_custom_adm_url

export OP_NAME=your-creative-name-for-your-OP-config

# Given to you by your OP, this is a sample
export SCOPE='openid,profile,email'

# Provided to you by your OP
export AUTHORIZATION_ENDPOINT='https://op-fqdn/...'

# Provided to you by your OP
export TOKEN_ENDPOINT='https://op-fqdn/...'

# Provided to you by your OP
export USERINFO_ENDPOINT='https://op-fqdn/...'

# FQDN of your OP
export ISSUER='https://op-fqdn'

# Provided to you by your OP
export JWKS_URI='https://op-fqdn/...'

# Provided to you by your OP
export CLIENT_ID='client_id'

# Provided to you by your OP
export CLIENT_SECRET='passwd'

# set by the pip package - django-oidc
export REDIRECT_URIS='http://your_app.com/openid/callback/login/'

# set by the pip package - django-oidc - not sure if all OPs use this
export POST_LOGOUT_REDIRECT_URIS='http://your_app.com/openid/callback/logout/'
