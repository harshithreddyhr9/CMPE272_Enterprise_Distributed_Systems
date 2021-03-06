# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calc_pb2 as calc__pb2


class CalculatorStub(object):
  """The calculator service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Add = channel.unary_unary(
        '/Calculator/Add',
        request_serializer=calc__pb2.AddRequest.SerializeToString,
        response_deserializer=calc__pb2.AddTotal.FromString,
        )


class CalculatorServicer(object):
  """The calculator service definition.
  """

  def Add(self, request, context):
    """Sends numbers and getting total
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=calc__pb2.AddRequest.FromString,
          response_serializer=calc__pb2.AddTotal.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
