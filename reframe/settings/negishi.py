"""Negishi cluster-specific ReFrame configuration."""

site_configuration = {
    'systems': [
        {
            'name': 'negishi',
            'descr': 'RCAC Negishi Cluster',
            'hostnames': ['login.*.negishi'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'cpu',
                    'descr': 'Standard CPU Nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-p cpu'],
                    'environs': ['builtin'],
                    'max_jobs': 100
                },
                {
                    'name': 'gpu',
                    'descr': 'GPU Accelerated Nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-p gpu'],
                    'environs': ['builtin']
                },
                {
                    'name': 'highmem',
                    'descr': 'High Memory Nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-p highmem'],
                    'environs': ['builtin']
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'builtin',
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        }
    ],
    'logging': [
        {
            'level': 'debug',
            'handlers': [
                {
                    'type': 'file',
                    'name': 'reframe.log',
                    'level': 'debug',
                    'format': '[%(asctime)s] %(levelname)s: %(check_name)s: %(message)s',
                    'append': False
                },
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info'
                }
            ]
        }
    ]
}
