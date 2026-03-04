import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class PartitionSanityTest(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Check if partitions and environments load correctly'
        # Run on all partitions defined in negishi.py
        self.valid_systems = ['negishi:cpu', 'negishi:gpu', 'negishi:highmem']
        
        # Test across all supported environments for each partition
        self.valid_prog_environs = ['*']
        
        # Simple command to check the hostname and current environment
        self.executable = 'hostname'
        self.sanity_patterns = sn.assert_found(r'negishi', self.stdout)
        
        self.maintainers = ['Jeronimo Campuzano'] [cite: 4]
        self.tags = {'sanity', 'smoke'} [cite: 17]

    @rfm.run_before('run')
    def set_slurm_options(self):
        # Ensure we only request 1 node and a short time for sanity checks
        self.job.options = ['--nodes=1', '--time=00:05:00']