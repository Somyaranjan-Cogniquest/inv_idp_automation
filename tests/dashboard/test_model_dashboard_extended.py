def test_trained_count_visible(dashboard_page):
    assert dashboard_page.is_trained_count_visible()

def test_action_menu_visible(dashboard_page):
    assert dashboard_page.is_action_menu_present()

def test_refresh_model_action(dashboard_page):
    dashboard_page.click_refresh_on_first_model()
    assert dashboard_page.get_table_row_count() > 0