import os
import tempfile
import pytest
from flaskr import flaskr

@pytest.fixture
def client():
  db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
  flaskr.app.config['TESTING'] = True

  os.close(db_fd)
  os.unlink(flaskr.app.config['DATABASE'])
