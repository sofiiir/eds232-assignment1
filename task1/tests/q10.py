OK_FORMAT = True

test = {   'name': 'q10',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> pivot.index.name == "gear_cat"\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> pivot.columns.names[-1] == "marker_cat"\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(pivot.loc["single", ("union", "multiple")], 103.0, atol=0.1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(pivot.loc["multiple", ("union", "single")], 16.03, atol=0.1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(pivot.loc["single", ("dna_advantage", "multiple")], 30.0, atol=0.1)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
