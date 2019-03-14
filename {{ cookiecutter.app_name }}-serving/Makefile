NUM_OF_WORKERS := $(shell python -c 'import multiprocessing as mp; print(mp.cpu_count() * 2 + 1)')

serve:
	gunicorn --bind 0.0.0.0:80 src.server:app -w 4