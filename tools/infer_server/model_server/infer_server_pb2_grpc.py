# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import infer_server_pb2 as infer__server__pb2


class DetectronServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Detect = channel.unary_unary(
        '/detectron.infer.DetectronService/Detect',
        request_serializer=infer__server__pb2.DetectRequest.SerializeToString,
        response_deserializer=infer__server__pb2.DetectResponse.FromString,
        )


class DetectronServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Detect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DetectronServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Detect': grpc.unary_unary_rpc_method_handler(
          servicer.Detect,
          request_deserializer=infer__server__pb2.DetectRequest.FromString,
          response_serializer=infer__server__pb2.DetectResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'detectron.infer.DetectronService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
