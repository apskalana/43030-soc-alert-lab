FROM python:3.12-slim
WORKDIR /app
COPY frequency.py update_readme.sh entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh /app/update_readme.sh
ENTRYPOINT ["/app/entrypoint.sh"]
