from core.assertions import assert_greater_than_zero 

def test_dashboard_loaded_successfully(dashboard_page):
    assert dashboard_page.is_logo_visible(), "Cogniquest logo not visible"
    assert dashboard_page.is_home_breadcrumb_visible(), "Home breadcrumb missing"
    assert dashboard_page.is_sidebar_home_selected(), "Sidebar Home not selected"
    assert dashboard_page.is_table_header_visible(), "Model table header missing"

   # row_count = dashboard_page.get_table_row_count()
   # assert_greater_than_zero(row_count, "No models found in dashboard table")

   # assert dashboard_page.is_trained_status_present(), "Training status icon missing"
   # assert dashboard_page.is_action_menu_present(), "Action menu not visible"

def test_open_model_and_processing_dashboard(
    dashboard_page,
    model_landing_page
):
    MODEL_NAME = "TAAS"    