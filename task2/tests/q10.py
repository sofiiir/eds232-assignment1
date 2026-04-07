OK_FORMAT = True

test = {   'name': 'q10',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> np.isclose(sm_slope, beta_1, atol=0.0001)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(sm_intercept, beta_0, atol=0.0001)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(sm_r2, R2, atol=0.0001)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
