def test_easings():
    import src.common.easings as easings


    print(easings.calc_easing(4, 0.5))
    assert easings.calc_easing(1, 0.5) == 0.5
    assert easings.calc_easing(1, 1.0) == 1.0
    assert easings.calc_easing(1, 0.0) == 0.0
