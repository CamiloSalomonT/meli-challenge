import logging
import threading
from flask_restx import Resource

import app.control.pipeline as CtrlPipeline
import app.common.configuration as Config


class Pipeline(Resource):
    """Flask resource to publish the challenge's endpoint."""

    th = None
    datapath = Config.asString("FileReader", "filepath")
    
    def get(self):
        if self.th and self.th.is_alive():
            ret = "Currently executing pipeline!"
        else:
            if self.th:
                self.th = None
            ret = "Nothing running!"
        return {"message": ret}

    def post(self):
        if self.th and self.th.is_alive():
            logging.info("Entró aca")
            ret = "Pipeline in execution!"
        else:
            logging.info("Entró aca")
            if self.th:
                self.th = None
            self.th = threading.Thread(target=CtrlPipeline.call_pipeline, args=[self.datapath])
            self.th.start()
            ret = "Launching the pipeline..."
        return {"message": ret}
