import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.builtins import performance_function, run_before, sanity_function


@rfm.simple_test
class PingSelfPerformanceTest(rfm.RunOnlyRegressionTest):
    descr = 'Ping localhost with 3 packets and check runtime threshold'
    maintainers = ['JeronimoCampuzanoC']
    tags = {'sanity', 'performance', 'network'}

    valid_systems = ['negishi:cpu', 'negishi:gpu', 'negishi:highmem']
    valid_prog_environs = ['*']
    executable = 'ping'
    executable_opts = ['-c', '3', '127.0.0.1']

    reference = {
        '*': {
            'ping_time_seconds': (3.0, None, 0, 's')
        }
    }

    @run_before('run')
    def set_account(self):
        # Set the account for job submission
        self.job.options += ['--account=rcac']

    @sanity_function
    def assert_ping_succeeded(self):
        return sn.assert_found(r'3 packets transmitted, 3 received, 0% packet loss', self.stdout)

    @performance_function('s')
    def ping_time_seconds(self):
        total_ms = sn.extractsingle(
            r'time\s+(?P<total_ms>\d+)ms',
            self.stdout,
            'total_ms',
            int
        )
        return total_ms / 1000.0

    reference = {
        '*': {
            'ping_time_seconds': (3.0, None, 0, 's')
        }
    }

    
