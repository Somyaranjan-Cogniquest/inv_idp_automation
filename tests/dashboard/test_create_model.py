#Covers: TC_21 → TC_30, TC_32
def test_navigate_to_create_model(dashboard_page):
    dashboard_page.click_create_model()
    assert dashboard_page.is_create_model_page_open()

def test_mandatory_field_validation(create_model_page):
    create_model_page.click_next()
    assert create_model_page.is_error_visible()

def test_model_name_input(create_model_page):
    create_model_page.enter_model_name("TestModel")
    assert create_model_page.get_model_name_value() == "TestModel"
    
def test_special_characters_in_model_name(create_model_page):
    create_model_page.enter_model_name("@@@@")
    assert create_model_page.is_error_visible()

def test_model_name_length_limit(create_model_page):
    create_model_page.enter_model_name("A" * 256)
    assert create_model_page.is_error_visible()

def test_click_next_after_mandatory_fields(create_model_page):
    create_model_page.fill_mandatory_fields()
    create_model_page.click_next()

def test_create_model_success(create_model_page, dashboard_page):
    model_name = "AutoModel_01"
    create_model_page.create_model(model_name)
    assert dashboard_page.is_model_present(model_name)

def test_cancel_create_model(create_model_page):
    create_model_page.click_cancel()
    assert create_model_page.is_dashboard_open()

def test_duplicate_model_name(create_model_page):
    create_model_page.create_model("TAAS")
    assert create_model_page.is_error_visible()

def test_breadcrumb_navigation_after_create(create_model_page):
    create_model_page.click_breadcrumb_home()
    assert create_model_page.is_dashboard_open()