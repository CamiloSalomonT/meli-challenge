import time
import contextlib

import app.control.pipeline as Pipeline


@contextlib.contextmanager
def time_consumption(test):
    t0 = time.time()
    yield
    print("Time consumption for {}: {:.3f}s".format(test, time.time() - t0))


# with time_consumption("mini"):
#     Pipeline.call_pipeline("sample_data/tech_sample.csv")


with time_consumption("sample"):
    Pipeline.call_pipeline("/sample_data/technical_challenge_data.csv")