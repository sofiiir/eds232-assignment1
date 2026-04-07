OK_FORMAT = True

test = {   'name': 'q8',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> "dna_advantage" in df.columns\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (df["dna_advantage"] == df["dna_richness"] - df["trad_richness"]).all()\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> df["dna_advantage"].iloc[0] == -4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> df["dna_advantage"].iloc[1] == 30\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
