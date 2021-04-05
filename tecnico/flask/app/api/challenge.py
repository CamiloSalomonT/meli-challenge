import io
import uuid
import threading

from flask import request
from flask_restx import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage

import app.data.reader as Reader
import app.control.pipeline as Pipeline
import app.common.configuration as conf


ns = Namespace("MeLi Challenge", description="Endpoint para probar el challenge")

upload_parser = reqparse.RequestParser()
upload_parser.add_argument("file", location="files", type=FileStorage, required=True)

import time
import contextlib

import app.control.pipeline as Pipeline


@contextlib.contextmanager
def time_consumption(test):
    t0 = time.time()
    yield
    print("Time consumption for {}: {:.3f}s".format(test, time.time() - t0))


@ns.route("")
class Challenge(Resource):
    """Flask resource to publish the challenge's endpoint."""

    ch_th = None
    da_th = None
    io_scope = "IO"
    datapath = conf.asString(io_scope, "filepath")
    enconding = conf.asString(io_scope, "encoding")

    def get(self):
        """Este método te dirá si se está ejecutando algun pipeline"""
        if self.ch_th and self.ch_th.is_alive():
            ret = "Currently executing pipeline!"
        else:
            if self.ch_th:
                self.ch_th = None
            ret = "Nothing running!"
        return {"message": ret}

    def post(self):
        """Utiliza este método para ejecutar el pipeline sobre el archivo parametrizado en la configuración"""
        if self.ch_th and self.ch_th.is_alive():
            ret = "Pipeline in execution!"
        else:
            if self.ch_th:
                self.ch_th = None
            self.ch_th = threading.Thread(target=Pipeline.call_file_pipeline, args=[self.datapath])
            self.ch_th.start()
            ret = "Launching the pipeline..."
        return {"message": ret}

    @ns.expect(upload_parser)
    def put(self):
        """Utiliza este servicio para ejecutar el pipeline sobre tu propio archivo. Son soportados los formatos jsonlines y csv... por el momento"""
        with time_consumption("PUT"):
            if self.ch_th and self.ch_th.is_alive():
                return {"message": "Pipeline in execution!"}
            else:
                filename = uuid.uuid4()
                chunk_size = conf.asInteger("IO", "chunk_size")
                uploads_path = conf.asString("IO", "uploads_path")
                filepath = uploads_path + str(filename)
                with open(filepath, "w") as f:
                    chunk_size = 128
                    chunks = Reader.read_lines(request.stream, chunk_size)

                    for dirty_chunk in chunks:
                        chunk = self.clean_lines(dirty_chunk)
                        if not (self.ch_th and self.ch_th.is_alive()):
                            self.ch_th = threading.Thread(target=Pipeline.call_chunk_pipeline, args=[chunk])
                            self.ch_th.start()
                        else:
                            for line in chunk:
                                f.write(line + "\n")
            self.ch_th = threading.Thread(target=Pipeline.call_file_pipeline, args=[filepath])
            self.ch_th.start()
            return {"message": "Launching the pipeline..."}

    def clean_lines(self, lines):
        new_lines = []
        for line in lines:
            nline = line.decode("utf-8").strip()
            if not (nline.startswith("-----") or nline.startswith("Content") or not nline):
                new_lines.append(nline)
        return new_lines
