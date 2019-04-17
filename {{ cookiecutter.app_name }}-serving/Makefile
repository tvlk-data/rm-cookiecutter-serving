serve:
	gunicorn -c src/gunicorn.config.py src.gunicorn:app

swagger:
	sh scripts/start_swagger.sh

loadtest_stg:
	sh scripts/start_load_testing.sh https://raring-meerkat-stg.tvlk-data.com

loadtest_prod:
	sh scripts/start_load_testing.sh https://raring-meerkat.tvlk-data.com