FROM quay.io/che-incubator/che-code:latest
USER 0

# copy all .vsix files to /default-extensions directory
RUN mkdir --mode=775 /default-extensions
COPY --chmod=755 *.vsix /default-extensions/

# Download default extensions and to use within the container
RUN mkdir --mode=775 /default-extensions
RUN curl -L https://open-vsx.org/api/llvm-vs-code-extensions/vscode-clangd/0.1.33/file/llvm-vs-code-extensions.vscode-clangd-0.1.33.vsix -o /default-extensions/llvm-vs-code-extensions.vscode-clangd.vsix && \
    curl -L https://open-vsx.org/api/ms-vscode/cmake-tools/1.20.53/file/ms-vscode.cmake-tools-1.20.53.vsix -o /default-extensions/ms-vscode.cmake-tools.vsix && \
    curl -L https://open-vsx.org/api/PKief/material-icon-theme/5.21.1/file/PKief.material-icon-theme-5.21.1.vsix -o /default-extensions/pkief.material-icon-theme.vsix && \
    curl -L https://open-vsx.org/api/ms-python/python/2025.4.0/file/ms-python.python-2025.4.0.vsix -o /default-extensions/ms-python.python.vsix && \
    if [ "$TARGETARCH" = "arm64" ]; then \
        curl -L https://open-vsx.org/api/ms-python/debugpy/linux-arm64/2025.6.0/file/ms-python.debugpy-2025.6.0@linux-arm64.vsix -o /default-extensions/ms-python.debugpy.vsix \
    else \
        curl -L https://open-vsx.org/api/ms-python/debugpy/linux-x64/2025.6.0/file/ms-python.debugpy-2025.6.0@linux-x64.vsix -o /default-extensions/ms-python.debugpy.vsix \
    fi; && \
    curl -L https://open-vsx.org/api/redhat/vscode-yaml/1.17.0/file/redhat.vscode-yaml-1.17.0.vsix -o /default-extensions/redhat.vscode-yaml.vsix && \
    curl -L https://open-vsx.org/api/redhat/vscode-tekton-pipelines/1.0.1/file/redhat.vscode-tekton-pipelines-1.0.1.vsix -o /default-extensions/redhat.vscode-tekton-pipelines.vsix

RUN chmod 755 /default-extensions/.vsix 

# add instruction to the script to copy default extensions to the working container
RUN echo "cp -r /default-extensions /checode/" >> /entrypoint-init-container.sh