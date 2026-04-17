def test_lead_time_calculation():
    initial_time = 60
    optimized_time = 45
    reduction = (initial_time - optimized_time) / initial_time
    assert reduction == 0.25 # Vérifie que la réduction est bien de 25%
