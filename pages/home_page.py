from selenium.webdriver.common.by import By
from pages.page import Page


class HomePage(Page):
    POLICY_SEARCH_BUTTON = (By.ID, 'menu_policy_search')

    FORM_SEARCH_BUTTON = (By.ID, 'menu_form_search')

    FORM_FILL_BUTTON = (By.ID, 'menu_form_fill')
    FORM_REGISTER_BLANK_BUTTON = (By.ID, 'menu_prod_list')
    FORM_NON_STANDARD_BUTTON = (By.ID, 'menu_non_standard_form')
    CASE_SEARCH_BUTTON = (By.ID, 'menu_case_search')
    DOCS_OWU_BUTTON = (By.ID, 'menu_form_owu')
    DOCS_ARCHIVE_BUTTON = (By.ID, 'menu_form_documents')
    DOCS_DIST_BUTTON = (By.ID, 'menu_form_distributor_documents')

    POLL_SEARCH_BUTTON = (By.ID, 'menu_poll_search')

    CLIENT_ADD_BUTTON = (By.ID, 'menu_client_add')
    CLIENT_SEARCH_BUTTON = (By.ID, 'menu_client_search')
    WORKER_ADD_BUTTON = (By.ID, 'menu_worker_add')
    WORKER_SEARCH_BUTTON = (By.ID, 'menu_worker_search')
    WORKER_IMPORT_BUTTON = (By.ID, 'menu_workers_import')
    WORKER_IMPORT_HISTORY_BUTTON = (By.ID, 'menu_workers_import_history')

    ROLE_ADD_BUTTON = (By.ID, 'menu_role_add')
    ROLE_SEARCH_BUTTON = (By.ID, 'menu_role_search')
    PERMISSION_PRODUCT_WORKERS_BUTTON = (By.ID, 'menu_product_workers_permissions')
    PERMISSION_PRODUCT_CLIENTS_BUTTON = (By.ID, 'menu_product_clients_permissions')

    PARTNER_ADD_BUTTON = (By.ID, 'menu_partners_add')
    PARTNER_SEARCH_BUTTON = (By.ID, 'menu_partners_search')
    UNIT_ADD_BUTTON = (By.ID, 'menu_unit_add')
    UNIT_SEARCH_BUTTON = (By.ID, 'menu_unit_search')
    REGION_ADD_BUTTON = (By.ID, 'menu_region_add')
    REGION_SEARCH_BUTTON = (By.ID, 'menu_region_search')

    MESSAGE_ADD_BUTTON = (By.ID, 'menu_message_add')
    MESSAGE_SEARCH_BUTTON = (By.ID, 'menu_message_search')
    MESSAGE_PARAMETERS_BUTTON = (By.ID, 'menu_message_parameters')
    MESSAGE_HISTORY_BUTTON = (By.ID, 'menu_message_history')

    PRODUCT_ADD_BUTTON = (By.ID, 'menu_product_add')
    PRODUCT_SEARCH_BUTTON = (By.ID, 'menu_product_search')
    ORDER_CATEGORY_ADD_BUTTON = (By.ID, 'menu_orderCategory_add')
    ORDER_CATEGORY_SEARCH_BUTTON = (By.ID, 'menu_orderCategory_search')
    ORDER_DEFINITION_ADD_BUTTON = (By.ID, 'menu_orderDefinition_add')
    ORDER_DEFINITION_SEARCH_BUTTON = (By.ID, 'menu_orderDefinition_search')
    ORDER_SEARCH_BUTTON = (By.ID, 'menu_order_search')
    POLL_DEFINITION_ADD_BUTTON = (By.ID, 'menu_pollDefinition_add')
    POLL_DEFINITION_SEARCH_BUTTON = (By.ID, 'menu_pollDefinition_search')
    PRODUCT_SHARE_BUTTON = (By.ID, 'menu_product_form_share')
    CSV_FILES_BUTTON = (By.ID, 'menu_csv_share')

    CHANGE_PASSWORD_BUTTON = (By.ID, 'menu_password_change')
    PAYMENTS_ONLINE_BUTTON = (By.ID, 'menu_payments')
    POLICY_NOTIFICATIONS_BUTTON = (By.ID, 'menu_policy_notifications')
    SYSTEM_PARAMETERS_BUTTON = (By.ID, 'menu_system_parameters')
    LOGGED_USERS_BUTTON = (By.ID, 'menu_logged_users')
    REGULATIONS_BUTTON = (By.ID, 'menu_regulations2')
    DICTIONARY_LIST_BUTTON = (By.ID, 'menu_dictionary_list')
    CLIENT_ACTIVITY_SEARCH_BUTTON = (By.ID, 'menu_clientActivity_search')
    REPORT_ADD_BUTTON = (By.ID, 'menu_report_add')
    REPORT_LIST_BUTTON = (By.ID, 'menu_report_list')
    REPORT_GENERATE_BUTTON = (By.ID, 'menu_report_generate')

    IMPORT_FROM_FILE_BUTTON = (By.ID, 'menu_import_from_file')
    USER_SESSIONS_BUTTON = (By.ID, 'menu_sessions')

    ##
    # RACHUNKI UDZIAŁÓW/POLIS
    ##
    def click_policy_search_button(self):
        self.find_element(*self.POLICY_SEARCH_BUTTON).click()

    ##
    # KLIENCI
    ##
    def click_form_search_button(self):
        self.find_element(*self.FORM_SEARCH_BUTTON).click()

    ##
    # PRODUKTY
    ##
    def click_form_fill_button(self):
        self.find_element(*self.FORM_FILL_BUTTON).click()

    def click_form_register_blank_button(self):
        self.find_element(*self.FORM_REGISTER_BLANK_BUTTON).click()

    def click_form_non_standard_button(self):
        self.find_element(*self.FORM_NON_STANDARD_BUTTON).click()

    def click_case_search_button(self):
        self.find_element(*self.CASE_SEARCH_BUTTON).click()

    def click_docs_owu_button(self):
        self.find_element(*self.DOCS_OWU_BUTTON).click()

    def click_docs_archive_button(self):
        self.find_element(*self.DOCS_ARCHIVE_BUTTON).click()

    def click_docs_dist_button(self):
        self.find_element(*self.DOCS_DIST_BUTTON).click()

    ##
    # ANKIETY
    ##
    def click_poll_search_button(self):
        self.find_element(*self.POLL_SEARCH_BUTTON).click()

    ##
    # UŻYTKOWNICY
    ##
    def click_client_add_button(self):
        self.find_element(*self.CLIENT_ADD_BUTTON).click()

    def click_client_seach_button(self):
        self.find_element(*self.CLIENT_SEARCH_BUTTON).click()

    def click_worker_add_button(self):
        self.find_element(*self.WORKER_ADD_BUTTON).click()

    def click_worker_search_button(self):
        self.find_element(*self.WORKER_SEARCH_BUTTON).click()

    def click_worker_import_button(self):
        self.find_element(*self.WORKER_IMPORT_BUTTON).click()

    def click_worker_import_history_button(self):
        self.find_element(*self.WORKER_IMPORT_HISTORY_BUTTON).click()

    ##
    # UPRAWNIENIA I ROLE
    ##
    def click_role_add_button(self):
        self.find_element(*self.ROLE_ADD_BUTTON).click()

    def click_role_search_button(self):
        self.find_element(*self.ROLE_SEARCH_BUTTON).click()

    def click_permission_product_workers_button(self):
        self.find_element(*self.PERMISSION_PRODUCT_WORKERS_BUTTON).click()

    def click_permission_product_clients_button(self):
        self.find_element(*self.PERMISSION_PRODUCT_CLIENTS_BUTTON).click()

    ##
    # PARTNERZY I ODDZIAŁY
    ##
    def click_partner_add_button(self):
        self.find_element(*self.PARTNER_ADD_BUTTON).click()

    def click_partner_search_button(self):
        self.find_element(*self.PARTNER_SEARCH_BUTTON).click()

    def click_unit_add_button(self):
        self.find_element(*self.UNIT_ADD_BUTTON).click()

    def click_unit_search_button(self):
        self.find_element(*self.UNIT_SEARCH_BUTTON).click()

    def click_region_add_button(self):
        self.find_element(*self.REGION_ADD_BUTTON).click()

    def click_region_search_button(self):
        self.find_element(*self.REGION_SEARCH_BUTTON).click()

    ##
    # KOMUNIKATY
    ##
    def click_message_add_button(self):
        self.find_element(*self.MESSAGE_ADD_BUTTON).click()

    def click_message_search_button(self):
        self.find_element(*self.MESSAGE_SEARCH_BUTTON).click()

    def click_message_parameters_button(self):
        self.find_element(*self.MESSAGE_PARAMETERS_BUTTON).click()

    def click_message_history_button(self):
        self.find_element(*self.MESSAGE_HISTORY_BUTTON).click()

    ##
    # ADMINISTRACJA PRODUKTAMI
    ##
    def click_product_add_button(self):
        self.find_element(*self.PRODUCT_ADD_BUTTON).click()

    def click_product_search_button(self):
        self.find_element(*self.PRODUCT_SEARCH_BUTTON).click()

    def click_order_category_add_button(self):
        self.find_element(*self.ORDER_CATEGORY_ADD_BUTTON).click()

    def click_order_category_search_button(self):
        self.find_element(*self.ORDER_CATEGORY_SEARCH_BUTTON).click()

    def click_order_definition_add_button(self):
        self.find_element(*self.ORDER_DEFINITION_ADD_BUTTON).click()

    def click_order_definition_search_button(self):
        self.find_element(*self.ORDER_DEFINITION_SEARCH_BUTTON).click()

    def click_order_search_button(self):
        self.find_element(*self.ORDER_SEARCH_BUTTON).click()

    def click_poll_definition_add_button(self):
        self.find_element(*self.POLL_DEFINITION_ADD_BUTTON).click()

    def click_poll_definition_search_button(self):
        self.find_element(*self.POLL_DEFINITION_SEARCH_BUTTON).click()

    def click_product_share_button(self):
        self.find_element(*self.PRODUCT_SHARE_BUTTON).click()

    def click_csv_files_button(self):
        self.find_element(*self.CSV_FILES_BUTTON).click()

    ##
    # ADMINISTRACJA
    ##
    def click_change_password_button(self):
        self.find_element(*self.CHANGE_PASSWORD_BUTTON).click()

    def click_payments_online_button(self):
        self.find_element(*self.PAYMENTS_ONLINE_BUTTON).click()

    def click_policy_notifications_button(self):
        self.find_element(*self.POLICY_NOTIFICATIONS_BUTTON).click()

    def click_system_parameters_button(self):
        self.find_element(*self.SYSTEM_PARAMETERS_BUTTON).click()

    def click_logged_users_button(self):
        self.find_element(*self.LOGGED_USERS_BUTTON).click()

    def click_regulations_button(self):
        self.find_element(*self.REGULATIONS_BUTTON).click()

    def click_dictionary_lists_button(self):
        self.find_element(*self.DICTIONARY_LIST_BUTTON).click()

    def click_client_activity_search_button(self):
        self.find_element(*self.CLIENT_ACTIVITY_SEARCH_BUTTON).click()

    ##
    # ZESTAWIENIA
    ##
    def click_report_add_button(self):
        self.find_element(*self.REPORT_ADD_BUTTON).click()

    def click_report_list_button(self):
        self.find_element(*self.REPORT_LIST_BUTTON).click()

    def click_report_generate_button(self):
        self.find_element(*self.REPORT_GENERATE_BUTTON).click()

    ##
    # IMPORT
    ##
    def click_import_from_file_button(self):
        self.find_element(*self.IMPORT_FROM_FILE_BUTTON).click()

    ##
    # SESJE UŻYTKOWNIKA
    ##
    def click_user_sessions_button(self):
        self.find_element(*self.USER_SESSIONS_BUTTON).click()
