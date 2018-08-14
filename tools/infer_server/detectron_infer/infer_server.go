package detectron_infer

import (
  "net/http"
  "golang.org/x/net/context"
  "github.com/grpc-ecosystem/grpc-gateway/runtime"
  "google.golang.org/grpc"
)
   
func Run(endpoint *string) error {
  ctx := context.Background()
  ctx, cancel := context.WithCancel(ctx)
  defer cancel()
   
  mux := runtime.NewServeMux()
  opts := []grpc.DialOption{grpc.WithInsecure()}
  err := RegisterDetectronServiceHandlerFromEndpoint(ctx, mux, *endpoint, opts)
  if err != nil {
    return err
  }
   
  return http.ListenAndServe(":8080", mux)
}


