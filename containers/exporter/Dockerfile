FROM fedora:40
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN dnf install -y \
      python3 \
      git \
      make \
      yq \
      openssl \
      qemu-img \
      qemu-system-aarch64 \
      edk2-aarch64 \
    && dnf clean all \
    && rm -rf /var/cache/dnf

ENV UV_PYTHON=python3.12 VIRTUAL_ENV=/jumpstarter
RUN uv venv /jumpstarter && \
    uv pip install \
      "git+https://github.com/jumpstarter-dev/jumpstarter#subdirectory=packages/jumpstarter-all"
ENV PATH="/jumpstarter/bin:$PATH"
