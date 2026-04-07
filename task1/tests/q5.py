OK_FORMAT = True

test = {   'name': 'q5',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> "dna_richness" in stats.columns and "trad_richness" in stats.columns\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(stats.loc["mean", "dna_richness"], 12.382353, atol=0.01)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(stats.loc["mean", "trad_richness"], 12.073529, atol=0.01)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(stats.loc["median", "dna_richness"], 9.5, atol=0.01)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
