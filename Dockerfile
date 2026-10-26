FROM python:3.12-slim
WORKDIR /app
COPY soc_triage.py sample_logs.jsonl ./
USER 10001
ENTRYPOINT ["python", "soc_triage.py"]
CMD ["sample_logs.jsonl"]
