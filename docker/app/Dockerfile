FROM --platform=linux/amd64 bitnami/python:3.11 as builder-image

ARG APP_PATH="/home/appuser/app"

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3 -m venv "$APP_PATH/venv"
ENV VIRTUAL_ENV="$APP_PATH/venv"
ENV PATH="$APP_PATH/venv/bin:$PATH"

# Install required packages
RUN install_packages libpq-dev netcat

# install requirements
COPY requirements.txt requirements-ci.txt
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements-ci.txt


FROM --platform=linux/amd64 bitnami/python:3.11 AS runner-image

ARG APP_PATH="/home/appuser/app"

# Install required packages
RUN install_packages libpq-dev netcat

RUN useradd --create-home appuser
COPY --from=builder-image "$APP_PATH/venv" "$APP_PATH/venv"

WORKDIR "$APP_PATH"
COPY --chown=appuser:appuser ./ ./
USER appuser

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

# activate virtual environment
ENV VIRTUAL_ENV="$APP_PATH/venv"
ENV PATH="$APP_PATH/venv/bin:$PATH"

# Setup entrypoint script
RUN sed -i 's/\r$//g' "$APP_PATH/docker/entrypoint.sh"
RUN chmod +x "$APP_PATH/docker/entrypoint.sh"

ENTRYPOINT ["/home/appuser/app/docker/entrypoint.sh"]
