#!/bin/sh -e

uvicorn --host 0.0.0.0 --port 5000 --log-level debug app:app
