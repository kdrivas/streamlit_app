# Streamlit project

Heroku + Streamlit + FastAPI

- Test locally with docker-compose
```
	docker-compose up
```

- Deploy on Heroku
```
	### Deploy frontend
	heroku create --app <frontend_app> --remote <frontend_app_remote>
	heroku buildpacks:set heroku/python -a <frontend_app>
	heroku buildpacks:add -a <frontend_app> heroku-community/multi-procfile
	heroku config:set -a <frontend_app> PROCFILE=frontend/Procfile
	git push https://git.heroku.com/<frontend_app>.git HEAD:main

	### Deploy api
	heroku create --app <api_app> --remote <api_app_remote>
	heroku buildpacks:set heroku/python -a <api_app>
	heroku buildpacks:add -a <api_app> heroku-community/multi-procfile
	heroku buildpacks:add -a <api_app> --index 1 heroku-community/apt
	heroku config:set -a <api_app> PROCFILE=inference/Procfile
	git push https://git.heroku.com/<api_app>.git HEAD:main
```

