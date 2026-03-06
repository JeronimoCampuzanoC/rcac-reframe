import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import run_before, sanity_function


@rfm.simple_test
class PartitionSanityTest(rfm.RunOnlyRegressionTest):
    descr = 'Basic partition sanity check on Negishi'
    valid_systems = ['negishi:cpu', 'negishi:gpu', 'negishi:highmem']
    valid_prog_environs = ['*']
    executable = 'hostname'

    @run_before('run')
    def set_account(self):
        # Set the account for job submission
        self.job.options += ['--account=rcac']

        # Request GPU resources if running on the gpu partition
        if self.current_partition.name == 'gpu':
            self.job.options += ['--gres=gpu:1']
            self.job.options += ['--cpus-per-task=10'] # rule 10 CPUs per GPU you request

        # Request highmem resources if running on the highmem partition
        if self.current_partition.name == 'highmem':
            self.job.options += ['--cpus-per-task=64'] # rule 64 CPUs per highmem you request

    @sanity_function
    def assert_hostname_output(self):
        return sn.assert_found(r'\S+', self.stdout)

    maintainers = ['JeronimoCampuzanoC']
    tags = {'sanity', 'smoke'}
