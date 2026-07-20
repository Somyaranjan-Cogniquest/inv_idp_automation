from core.base_page import BasePage
from locators import model_landing_locators as loc



class ModelLandingPage(BasePage):

    def validate_breadcrumb(self, model_name):

        assert self.is_visible(
            loc.BREADCRUMB_HOME
        ), "Home breadcrumb missing"

        assert model_name in self.page.locator(
            loc.BREADCRUMB_MODEL
        ).inner_text(), "Model breadcrumb incorrect"


    def validate_model_heading(self, model_name):

        heading_text = self.page.locator(
            loc.MODEL_NAME_HEADING
        ).inner_text()

        assert model_name in heading_text, \
            "Model name heading mismatch"


    def validate_all_cards_present(self):

        assert self.is_visible(
            loc.CONFIGURE_MODEL_CARD
        ), "Configure Model card missing"

        assert self.is_visible(
            loc.TRAINING_CARD
        ), "Training card missing"

        assert self.is_visible(
            loc.PROCESSING_DASHBOARD_CARD
        ), "Processing Dashboard card missing"

        assert self.is_visible(
            loc.DOCUMENT_ANALYTICS_CARD
        ), "Document Analytics card missing"


    def open_processing_dashboard(self):

        self.click(loc.PROCESSING_DASHBOARD_CARD)

    def open_training(self):
        self.click(loc.TRAINING_CARD)
    

        