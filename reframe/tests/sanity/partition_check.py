import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import sanity_function


@rfm.simple_test
class PartitionSanityTest(rfm.RunOnlyRegressionTest):
    descr = 'Basic partition sanity check on Negishi'
    valid_systems = ['negishi:cpu', 'negishi:gpu', 'negishi:highmem']
    valid_prog_environs = ['*']
    executable = 'hostname'

    @sanity_function
    def assert_hostname_output(self):
        return sn.assert_found(r'\S+', self.stdout)

    maintainers = ['JeronimoCampuzanoC']
    tags = {'sanity', 'smoke'}
