import connexion
from connexion.exceptions import OAuthProblem

TOKEN_DB = {"asdf1234567890": {"uid": 100}}


def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)

    if not info:
        raise OAuthProblem("Invalid token")

    return info


def get_secret(user) -> str:
    return f"You are {user} and the secret is 'wbevuec'"


if __name__ == "__main__":
    app = connexion.FlaskApp(__name__)
    app.add_api("openapi.yaml")
    app.run(port=8080)


# to test: curl -H "X-Auth: asdf1234567890" http://localhost:8080/secret