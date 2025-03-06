FROM arm64v8/python:3.7

# install required debian packages

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        gfortran \
        libopenblas-dev \
        ninja-build \
        libatlas-base-dev \
        libhdf5-dev \
        cmake

RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# install rust, install retworkx, remove rust

RUN wget https://static.rust-lang.org/dist/rust-nightly-aarch64-unknown-linux-gnu.tar.gz -nv && \
        tar -xvzf rust-nightly-aarch64-unknown-linux-gnu.tar.gz && \
        ./rust-nightly-aarch64-unknown-linux-gnu/install.sh && \
        pip --no-cache-dir install retworkx && \
        /usr/local/lib/rustlib/uninstall.sh && \
        rm rust-nightly-aarch64-unknown-linux-gnu.tar.gz && \
        rm -rf rust-nightly-aarch64-unknown-linux-gnu/

# install python3 packages

RUN pip --no-cache-dir install \
        matplotlib ipykernel jupyter

RUN pip --no-cache-dir install \
        cython numpy scikit-build h5py

# need scikit-build before cmake will install

RUN pip --no-cache-dir install \
        cmake

# Install pylatexenc to avoid Qiskit plot issues
RUN pip --no-cache-dir install pylatexenc

# pyscf pinned, as I cannot get pip to install later versions

ENV LDFLAGS="-L/usr/lib/aarch64-linux-gnu -lopenblas"
ENV PYSCF_INC_DIR="/usr/lib/aarch64-linux-gnu:/usr/include"
RUN pip --no-cache-dir install pyscf


RUN pip --no-cache-dir install \
        qiskit

COPY notebooks /notebooks

WORKDIR "/notebooks"

EXPOSE 8888

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]





