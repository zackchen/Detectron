# A simple web server for Detectron

## Start
### Install dependency

- install python grpc dependency
```bash
pip install protobuf
sudo pip install grpcio
sudo pip install grpcio-tools googleapis-common-protos
```
- install golang grpc and grpc-gateway dependency
```bash

```

### Build
``` bash
protoc -I/usr/local/include -I. \
  -I$GOPATH/src \
  -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
  --go_out=plugins=grpc:. \
  proto/infer_server.proto


python -m grpc_tools.protoc -I./proto --python_out=. \
  --grpc_python_out=. \
  ./proto/infer_server.proto

  protoc -I/usr/local/include -I. \
    -I$GOPATH/src \
    -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
    --grpc-gateway_out=logtostderr=true,grpc_api_configuration=proto/infer_server.yaml:. \
    proto/infer_server.proto

```

