FROM rust:latest
WORKDIR /work
ENTRYPOINT ["cargo"]
CMD ["build"]
