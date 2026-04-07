OK_FORMAT = True

test = {   'name': 'q9',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> n_large == 7\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (large_lakes["area_ha"] > 1000).all()\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (large_lakes["total_vol_liter"] > df["total_vol_liter"].median()).all()\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(mean_union_large, large_lakes["union"].mean(), atol=0.01)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
