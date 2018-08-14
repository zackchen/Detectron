package main

import (
	"flag"
	"github.com/golang/glog"
	"./detectron_infer"

)

var (
	endpoint = flag.String("Model server endpoint", ":50051", "Model server endpoint")
  )

func main() {
	flag.Parse()
	defer glog.Flush()
	 
	if err := detectron_infer.Run(endpoint); err != nil {
	  glog.Fatal(err)
	}
  }