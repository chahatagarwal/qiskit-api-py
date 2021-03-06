import warnings

from .IBMQuantumExperience import IBMQuantumExperience  # noqa
from .IBMQuantumExperience import ApiError
from .IBMQuantumExperience import BadBackendError
from .IBMQuantumExperience import CredentialsError
from .IBMQuantumExperience import RegisterSizeError

__version__ = '2.0.4'  # this should match setup.py:version parameter

warnings.warn('The qiskit-api-py package is deprecated. please use the '
              'new provider for accessing IBMQ backends: qiskit-ibmq-provider',
              DeprecationWarning)
