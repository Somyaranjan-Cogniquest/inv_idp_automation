from pages.monitoring_page import MonitoringPage

def test_monitoring_flow(training_page):

    assert training_page.is_monitoring_disabled()

    training_page.open_monitoring()

    mp = MonitoringPage(training_page.page)
    assert mp.is_monitoring_page_open()
    assert mp.is_monitoring_table_visible()

    mp.get_summary_data()
    mp.select_topic("InvoiceHeader")

    mp.go_back()
    assert training_page.is_training_page_open()