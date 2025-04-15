FROM quay.io/che-incubator/che-code:latest
USER 0

# copy all .vsix files to /default-extensions directory
RUN mkdir --mode=775 /default-extensions
COPY --chmod=755 ./default-extensions/*.vsix /default-extensions/
RUN mkdir --mode=775 /multi-arch
COPY --chmod=755 ./multi-arch/*.vsix /multi-arch/

RUN if [ "$TARGETARCH" = "arm64" ]; then \
        cp ./multi-arch/ms-python.debugpy-arm64.vsix /default-extensions/ms-python.debugpy.vsix; \
    else \
        cp ./multi-arch/ms-python.debugpy-amd64.vsix /default-extensions/ms-python.debugpy.vsix; \
    fi;

# Remove multi-arch directory
RUN rm -rf /multi-arch

# add instruction to the script to copy default extensions to the working container
RUN echo "cp -r /default-extensions /checode/" >> /entrypoint-init-container.sh