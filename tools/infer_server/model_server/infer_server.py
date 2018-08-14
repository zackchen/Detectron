#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 Qihoo.com, Inc. All Rights Reserved
#

"""
@file infer_server.py.py
@author: chenzhen (chenzhen@360.cn)
@date: 2018/8/14
"""
import logging
import time
from concurrent import futures
import grpc
import infer_server_pb2
import infer_server_pb2_grpc


class DetectronServiceImpl(infer_server_pb2_grpc.DetectronServiceServicer):
    def Detect(self, request, context):
        logging.info('Get detection request')
        resp = infer_server_pb2.DetectResponse()
        resp.request_id = "123"

        return resp


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    infer_server_pb2_grpc.add_DetectronServiceServicer_to_server(DetectronServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    logging.info('Detectron model service is listening...')
    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':

    main()
