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
                    'environs': ['gnu', 'intel'],
                    'max_jobs': 100
                },
                {
                    'name': 'gpu',
                    'descr': 'GPU Accelerated Nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-p gpu'],
                    'environs': ['gnu', 'gnu-cuda']
                },
                {
                    'name': 'highmem',
                    'descr': 'High Memory Nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-p highmem'],
                    'environs': ['gnu']
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'gnu',
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        },
        {
            'name': 'intel',
            'cc': 'icc',
            'cxx': 'icpc',
            'ftn': 'ifort'
        },
        {
            'name': 'gnu-cuda',
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran',
            'modules': ['cuda']
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
