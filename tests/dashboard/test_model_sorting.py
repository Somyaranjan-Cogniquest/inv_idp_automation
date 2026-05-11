def test_sort_by_model_id(dashboard_page):
    dashboard_page.sort_by_column("Model ID")
    assert dashboard_page.get_table_row_count() > 0

def test_sort_by_date_created(dashboard_page):
    dashboard_page.sort_by_column("Date Created")
    assert dashboard_page.get_table_row_count() > 0