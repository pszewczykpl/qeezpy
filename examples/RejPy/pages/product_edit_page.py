from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from qeezpy import Page


class EditProductPage(Page):
    PRODUCT_PARAMS_SYSTEM_INPUT = (By.ID, 'productParam.product')
    PRODUCT_PARAMS_SYSTEM_ID_INPUT = (By.ID, 'productParam.productSystemId')
    PRODUCT_PARAMS_SYMBOL_INPUT = (By.ID, 'productParam.symbol')
    PRODUCT_PARAMS_VERSION_INPUT = (By.ID, 'productParam.versionString')
    PRODUCT_PARAMS_NAME_INPUT = (By.ID, 'productParam.productName')
    PRODUCT_PARAMS_CATEGORY_INPUT = (By.ID, 'productParam.category')
    PRODUCT_PARAMS_ACCUMULATION_PRODUCT_INPUT = (By.ID, 'productParam.accumulationProduct')
    PRODUCT_PARAMS_ACCUMULATION_DISTRIBUTOR_INPUT = (By.ID, 'productParam.accumulationDistributor')
    PRODUCT_PARAMS_GROUP_INPUT = (By.ID, 'productParam.productGroup')
    PRODUCT_PARAMS_SYSTEM_GROUP_INPUT = (By.ID, 'productParam.productGroupsDictionaryItem')
    PRODUCT_PARAMS_DISTRIBUTOR_INPUT = (By.ID, 'productParam.partnersDictionaryItem')
    PRODUCT_PARAMS_FUND_TYPE_INPUT = (By.ID, 'productParam.fundType')
    PRODUCT_PARAMS_DESCRIPTION_INPUT = (By.ID, 'productParam.description')
    PRODUCT_PARAMS_COMPANY_INPUT = (By.ID, 'productParam.unit')
    PRODUCT_PARAMS_STATUS_INPUT = (By.ID, 'productParam.status')
    PRODUCT_PARAMS_AVAILABILITY_INPUT = (By.ID, 'productParam.availability')
    PRODUCT_PARAMS_SALE_FROM_DATE_INPUT = (By.ID, 'productParam.saleFrom')
    PRODUCT_PARAMS_SALE_TO_DATE_INPUT = (By.ID, 'productParam.saleTo')
    PRODUCT_PARAMS_POLL_REQUIRED_INPUT = (By.ID, 'productParam.pollRequired')
    PRODUCT_PARAMS_PRINT_FORM_REQUIRED_INPUT = (By.ID, 'productParam.printPolicyFormRequired')
    PRODUCT_PARAMS_PRINT_CERT_REQUIRED_INPUT = (By.ID, 'productParam.printPolicyCertRequired')

    PRODUCT_PARAMS_SOURCE_PRODUCT_CHECK_INPUT = (By.ID, 'productParam.filesCopyCheck')
    PRODUCT_PARAMS_SOURCE_PRODUCT_INPUT = (By.ID, 'productParam.productParamSource')

    MANAGE_FILES_BUTTON = (By.NAME, '_eventId_manageFiles')
    PRODUCT_PARAMS_POLICY_FORM_FILE_INPUT = (By.ID, 'productParam.policyForm')
    PRODUCT_PARAMS_POLICY_DEFINITION_FILE_INPUT = (By.ID, 'productParam.policyFormDefinition')
    PRODUCT_PARAMS_POLICY_CALCULATOR_FILE_INPUT = (By.ID, 'productParam.calculatorFormDefinition')

    MANAGE_PARAMS_BUTTON = (By.NAME, '_eventId_addParam')
    MANAGE_SUBSCRIPTIONS_BUTTON = (By.NAME, '_eventId_subscriptions')

    MANAGE_DOCS_BUTTON = (By.NAME, '_eventId_manageDocuments')
    PRODUCT_PARAMS_POLICY_PRINT_FILE_INPUT = (By.ID, 'productParam.policyPrintForm')
    PRODUCT_PARAMS_POLICY_BI_PRINT_FILE_INPUT = (By.ID, 'productParam.biPolicyPrintForm')
    PRODUCT_PARAMS_POLICY_ADDITIONAL_PRINT_FILE_INPUT = (By.ID, 'productParam.additionalPrint')

    MANAGE_ORDERS_BUTTON = (By.NAME, '_eventId_orders')

    PRODUCT_PARAMS_KIND_INPUT = (By.ID, 'productParam.productKind')
    PRODUCT_PARAMS_TYPE_INPUT = (By.ID, 'productParam.productType')
    PRODUCT_PARAMS_CLIENT_TYPE_INPUT = (By.ID, 'productParam.clientType')
    PRODUCT_PARAMS_FORM_POLICY_TYPE_INPUT = (By.ID, 'productParam.policyType')
    PRODUCT_PARAMS_PRESENTATION_TYPE_INPUT = (By.ID, 'productParam.presentationType')
    PRODUCT_PARAMS_REFRESH_BUTTON_LABEL_INPUT = (By.ID, 'refreshLabelCode')
    PRODUCT_PARAMS_SERIES_INPUT = (By.ID, 'seria')
    PRODUCT_PARAMS_SUBSCRIPTION_NUMBER_INPUT = (By.ID, 'nr_subskrypcji')
    PRODUCT_PARAMS_QUOTES_NAME_INPUT = (By.ID, 'productParam.quotesName')
    PRODUCT_PARAMS_RESET_COUNTER_CASE_INPUT = (By.ID, 'productParam.resetCounter')
    PRODUCT_PARAMS_SHOW_SUMMARY_INPUT = (By.ID, 'productParam.showSummary')
    PRODUCT_PARAMS_PRINT_PREVIEW_INPUT = (By.ID, 'productParam.printPreview')
    PRODUCT_PARAMS_REQUIRES_AUTHORIZATION_INPUT = (By.ID, 'productParam.requiresAuthorization')
    PRODUCT_PARAMS_REQUIRES_TU_AUTHORIZATION_INPUT = (By.ID, 'productParam.requiresAuthorizationTU')
    PRODUCT_PARAMS_REQUIRES_INDIVIDUAL_AUTHORIZATION_INPUT = (By.ID, 'productParam.individualAuthorization')
    PRODUCT_PARAMS_REGULAR_PAYMENT_INPUT = (By.ID, 'productParam.regularPayment')
    PRODUCT_PARAMS_HIDE_INSURED_INPUT = (By.ID, 'productParam.hideSameInsured')
    PRODUCT_PARAMS_CONTEST_INPUT = (By.ID, 'productParam.contest')
    PRODUCT_PARAMS_PAYMENT_CALC_INPUT = (By.ID, 'productParam.paymentCalculator')
    PRODUCT_PARAMS_SEND_PDF_INPUT = (By.ID, 'productParam.sendPdf')
    PRODUCT_PARAMS_ONLY_ALLOWED_IP_INPUT = (By.ID, 'productParam.onlyAllowedIp')
    PRODUCT_PARAMS_ALLOWED_IP_INPUT = (By.ID, 'productParam.allowedIP')

    SAVE_BUTTON = (By.NAME, '_eventId_save')
    CANCEL_BUTTON = (By.NAME, '_eventId_cancel')

    ADD_NEW_SUBSCRIPTION_BUTTON = (By.NAME, '_eventId_initSubscription')

    SUBSCRIPTIONS_NUMBER_INPUT = (By.ID, 'subscription.number')
    SUBSCRIPTIONS_DATE_FROM_INPUT = (By.ID, 'subscription.dateFrom')
    SUBSCRIPTIONS_DATE_TO_INPUT = (By.ID, 'subscription.dateTo')
    SUBSCRIPTIONS_PARAM_KEY_INPUT = (By.ID, 'subscriptionParam.key')
    SUBSCRIPTIONS_PARAM_VALUE_INPUT = (By.ID, 'subscriptionParam.value')

    ADD_PARAM_BUTTON = (By.NAME, '_eventId_addParam')
    SAVE_SUBSCRIPTION_BUTTON = (By.NAME, '_eventId_saveSubscription')

    PARAM_KEY_INPUT = (By.ID, 'paramValue.key')
    PARAM_VALUE_INPUT = (By.ID, 'paramValue.value')

    PARAM_ACCOUNT_NUMBER_INPUT = (By.ID, 'formTransferData.accountNumber')
    PARAM_ACCOUNT_OWNER_INPUT = (By.ID, 'formTransferData.partner')
    PARAM_PAYEE_DATA_FROM_PARTNER_INPUT = (By.ID, 'formTransferData.payeeDataFromPartner')

    ADD_TRANSFER_DATA_BUTTON = (By.NAME, '_eventId_addTransferData')

    PARAM_MASK_INPUT = (By.ID, 'mask')
    PARAM_MASK_OWNER_INPUT = (By.ID, 'tempMaskOwner')

    ADD_MASK_BUTTON = (By.NAME, '_eventId_addMask')

    ADD_NEW_OPERATION_BUTTON = (By.NAME, '_eventId_new')
    SUBMIT_BUTTON = (By.NAME, '_eventId_back')
    # CANCEL_BUTTON = (By.NAME, '_eventId_cancel')

    OPERATION_ORDER_DEFINITION_INPUT = (By.ID, 'operation.orderDefinition')
    OPERATION_ORDER_COMMENT_INPUT = (By.ID, 'operation.comment')
    OPERATION_ORDER_FROM_DATE_INPUT = (By.ID, 'operation.fromDate')
    OPERATION_ORDER_TO_DATE_INPUT = (By.ID, 'operation.toDate')
    OPERATION_ORDER_CONDITION_INPUT = (By.ID, 'operation.condition')
    OPERATION_ORDER_RIGHT_LIST_INPUT = (By.ID, 'rightList')
    ADD_TO_LIST_BUTTON = (By.NAME, '_eventId_addToList')
    REMOVE_FROM_LIST_BUTTON = (By.NAME, '_eventId_removeFromList')

    OPERATION_ORDER_SHOW_PLACE_INPUT = (By.ID, 'operation.showPlace')
    OPERATION_ORDER_STATUS_INPUT = (By.ID, 'operation.status')
    OPERATION_ORDER_BLOCKING_INPUT = (By.ID, 'operation.blocking')
    OPERATION_ORDER_CONFIRM_REQUEST_INPUT = (By.ID, 'operation.confirmRequired')

    ADD_OPERATION_BUTTON = (By.NAME, '_eventId_add')
    # SUBMIT_BUTTON = (By.NAME, '_eventId_back')
    # CANCEL_BUTTON = (By.NAME, '_eventId_cancel')


    ##
    # EDYCJA PRODUKTU - INFORMACJE OGÓLNE
    ##
    def enter_product_params_system(self, product_params_system):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_SYSTEM_INPUT))
        select.select_by_visible_text(product_params_system)

    def enter_product_params_system_id(self, product_params_system_id):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_SYSTEM_ID_INPUT))
        select.select_by_visible_text(product_params_system_id)

    def enter_product_params_version(self, product_params_version):
        self.find_element(*self.PRODUCT_PARAMS_VERSION_INPUT).send_keys(product_params_version)

    def enter_product_params_name(self, name):
        self.find_element(*self.PRODUCT_PARAMS_NAME_INPUT).send_keys(name)

    def enter_product_params_category(self, category):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_CATEGORY_INPUT))
        select.select_by_visible_text(category)

    def enter_product_params_accumulation_product(self, accumulation_product):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_ACCUMULATION_PRODUCT_INPUT))
        select.select_by_visible_text(accumulation_product)

    def enter_product_params_accumulation_distributor(self, accumulation_distributor):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_ACCUMULATION_DISTRIBUTOR_INPUT))
        select.select_by_visible_text(accumulation_distributor)

    def enter_product_params_group(self, group):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_GROUP_INPUT))
        select.select_by_visible_text(group)

    def enter_product_params_system_group(self, system_group):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_SYSTEM_GROUP_INPUT))
        select.select_by_visible_text(system_group)

    def enter_product_params_distributor(self, distributor):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_DISTRIBUTOR_INPUT))
        select.select_by_visible_text(distributor)

    def enter_product_params_fund_type(self, fund_type):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_FUND_TYPE_INPUT))
        select.select_by_visible_text(fund_type)

    def enter_product_params_description(self, description):
        self.find_element(*self.PRODUCT_PARAMS_DESCRIPTION_INPUT).send_keys(description)

    def enter_product_params_company(self, company):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_COMPANY_INPUT))
        select.select_by_visible_text(company)

    def enter_product_params_status(self, status):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_STATUS_INPUT))
        select.select_by_visible_text(status)

    def enter_product_params_availability(self, availability):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_AVAILABILITY_INPUT))
        select.select_by_visible_text(availability)

    def enter_product_params_sale_from_date(self, date):
        self.find_element(*self.PRODUCT_PARAMS_SALE_FROM_DATE_INPUT).send_keys(date)

    def enter_product_params_sale_to_date(self, date):
        self.find_element(*self.PRODUCT_PARAMS_SALE_TO_DATE_INPUT).send_keys(date)

    def click_product_params_poll_required(self):
        self.find_element(*self.PRODUCT_PARAMS_POLL_REQUIRED_INPUT).click()

    def click_product_params_print_form_required(self):
        self.find_element(*self.PRODUCT_PARAMS_PRINT_FORM_REQUIRED_INPUT).click()

    def click_product_params_print_cert_required(self):
        self.find_element(*self.PRODUCT_PARAMS_PRINT_CERT_REQUIRED_INPUT).click()

    ##
    # EDYCJA PRODUKTU - PRODUKTY SZABLONOWE
    ##
    def click_product_params_source_product_check(self):
        self.find_element(*self.PRODUCT_PARAMS_SOURCE_PRODUCT_CHECK_INPUT).click()

    def enter_product_params_source_product(self, source_product):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_SOURCE_PRODUCT_INPUT))
        select.select_by_visible_text(source_product)

    ##
    # EDYCJA PRODUKTU - FORMULARZE WNIOSKU I PROCES OBSŁUGI
    ##
    def click_manage_files_button(self):
        self.find_element(*self.MANAGE_FILES_BUTTON).click()

    def enter_product_params_policy_form_file(self, policy_form_file):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_POLICY_FORM_FILE_INPUT))
        select.select_by_visible_text(policy_form_file)

    def enter_product_params_policy_definition_file(self, policy_definition_file):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_POLICY_DEFINITION_FILE_INPUT))
        select.select_by_visible_text(policy_definition_file)

    def enter_product_params_policy_calculator_file(self, policy_calculator_file):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_POLICY_CALCULATOR_FILE_INPUT))
        select.select_by_visible_text(policy_calculator_file)

    ##
    # EDYCJA PRODUKTU - PARAMETRY PRODUKTU
    ##
    def click_manage_params_button(self):
        self.find_element(*self.MANAGE_PARAMS_BUTTON).click()

    def click_manage_subscriptions_button(self):
        self.find_element(*self.MANAGE_SUBSCRIPTIONS_BUTTON).click()

    ##
    # EDYCJA PRODUKTU - SZABLONY I DOKUMENTY
    ##
    def click_manage_docs_button(self):
        self.find_element(*self.MANAGE_DOCS_BUTTON).click()

    def enter_product_params_policy_print_file(self, policy_print_file):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_POLICY_PRINT_FILE_INPUT))
        select.select_by_visible_text(policy_print_file)

    def enter_product_params_policy_bi_print_file(self, policy_bi_print_file):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_POLICY_BI_PRINT_FILE_INPUT))
        select.select_by_visible_text(policy_bi_print_file)

    def enter_product_params_policy_additional_print_file(self, policy_additional_print_file):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_POLICY_ADDITIONAL_PRINT_FILE_INPUT))
        select.select_by_visible_text(policy_additional_print_file)

    ##
    # EDYCJA PRODUKTU - DYSPOZYCJE
    ##
    def click_manage_orders_button(self):
        self.find_element(*self.MANAGE_ORDERS_BUTTON).click()

    ##
    # EDYCJA PRODUKTU - DODATKOWE PARAMETRY
    ##
    def enter_product_params_kind(self, kind):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_KIND_INPUT))
        select.select_by_visible_text(kind)

    def enter_product_params_type(self, typ):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_TYPE_INPUT))
        select.select_by_visible_text(typ)

    def enter_product_params_client_type(self, client_type):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_CLIENT_TYPE_INPUT))
        select.select_by_visible_text(client_type)

    def enter_product_params_form_policy_type(self, form_policy_type):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_FORM_POLICY_TYPE_INPUT))
        select.select_by_visible_text(form_policy_type)

    def enter_product_params_presentation_type(self, presentation_type):
        select = Select(self.find_element(*self.PRODUCT_PARAMS_PRESENTATION_TYPE_INPUT))
        select.select_by_visible_text(presentation_type)

    def enter_product_params_refresh_button_label(self, label):
        self.find_element(*self.PRODUCT_PARAMS_REFRESH_BUTTON_LABEL_INPUT).send_keys(label)

    def enter_product_params_series(self, series):
        self.find_element(*self.PRODUCT_PARAMS_SERIES_INPUT).send_keys(series)

    def enter_product_params_subscription_number(self, subscription_number):
        self.find_element(*self.PRODUCT_PARAMS_SUBSCRIPTION_NUMBER_INPUT).send_keys(subscription_number)

    def enter_product_params_quotes_name(self, name):
        self.find_element(*self.PRODUCT_PARAMS_QUOTES_NAME_INPUT).send_keys(name)

    def click_product_params_reset_counter_case(self):
        self.find_element(*self.PRODUCT_PARAMS_RESET_COUNTER_CASE_INPUT).click()

    def click_product_params_show_summary(self):
        self.find_element(*self.PRODUCT_PARAMS_SHOW_SUMMARY_INPUT).click()

    def click_product_params_print_preview(self):
        self.find_element(*self.PRODUCT_PARAMS_PRINT_PREVIEW_INPUT).click()

    def click_product_params_requires_authorization(self):
        self.find_element(*self.PRODUCT_PARAMS_REQUIRES_AUTHORIZATION_INPUT).click()

    def click_product_params_requires_tu_authorization(self):
        self.find_element(*self.PRODUCT_PARAMS_REQUIRES_TU_AUTHORIZATION_INPUT).click()

    def click_product_params_requires_individual_authorization(self):
        self.find_element(*self.PRODUCT_PARAMS_REQUIRES_INDIVIDUAL_AUTHORIZATION_INPUT).click()

    def click_product_params_regular_payment(self):
        self.find_element(*self.PRODUCT_PARAMS_REGULAR_PAYMENT_INPUT).click()

    def click_product_params_hide_insured(self):
        self.find_element(*self.PRODUCT_PARAMS_HIDE_INSURED_INPUT).click()

    def click_product_params_(self):
        self.find_element(*self.PRODUCT_PARAMS_HIDE_INSURED_INPUT).click()

    def click_product_params_contest(self):
        self.find_element(*self.PRODUCT_PARAMS_CONTEST_INPUT).click()

    def click_product_params_payment_calc(self):
        self.find_element(*self.PRODUCT_PARAMS_PAYMENT_CALC_INPUT).click()

    def click_product_params_send_pdf(self):
        self.find_element(*self.PRODUCT_PARAMS_SEND_PDF_INPUT).click()

    def click_product_params_only_allowed_ip(self):
        self.find_element(*self.PRODUCT_PARAMS_ONLY_ALLOWED_IP_INPUT).click()

    def enter_product_params_allowed_ip(self, ip):
        self.find_element(*self.PRODUCT_PARAMS_ALLOWED_IP_INPUT).send_keys(ip)

    def click_save_button(self):
        self.find_element(*self.SAVE_BUTTON).click()

    def click_cancel_button(self):
        self.find_element(*self.CANCEL_BUTTON).click()

    ##
    # ZARZĄDZAJ OKRESAMI SUBSKRYPCJI
    ##
    def return_subscriptions_table(self):
        subscriptions = []
        table = self.driver.find_elements(By.XPATH, "//form/div//div[@class='boxContent_lvl1']/div/table/tbody/tr")
        i = 0
        for tr in table:
            subscription = [i]
            td = tr.find_elements(By.TAG_NAME, 'td')
            for cell in td:
                subscription.append(cell.text)
            subscriptions.append(subscription)
            i = i + 1

        return subscriptions

    def click_subscription_details_button(self, number):
        self.find_element(*(By.ID, "det_" + str(number[0]))).click()

    def click_subscription_delete_button(self, number):
        self.find_element(*(By.ID, "del_" + str(number[0]))).click()

    def click_add_new_subscription_button(self):
        self.find_element(*self.ADD_NEW_SUBSCRIPTION_BUTTON).click()

    ##
    # SZCZEGÓŁY NOWEGO/WYBRANEGO OKRESU SUBSKRYPCJI
    ##
    def enter_subscriptions_number(self, number):
        self.find_element(*self.SUBSCRIPTIONS_NUMBER_INPUT).send_keys(number)

    def enter_subscriptions_date_from(self, date):
        self.find_element(*self.SUBSCRIPTIONS_DATE_FROM_INPUT).send_keys(date)

    def enter_subscriptions_date_to(self, date):
        self.find_element(*self.SUBSCRIPTIONS_DATE_TO_INPUT).send_keys(date)

    def enter_subscriptions_param_key(self, key):
        self.find_element(*self.SUBSCRIPTIONS_PARAM_KEY_INPUT).send_keys(key)

    def enter_subscriptions_param_value(self, value):
        self.find_element(*self.SUBSCRIPTIONS_PARAM_VALUE_INPUT).send_keys(value)

    def click_add_param_button(self):
        self.find_element(*self.ADD_PARAM_BUTTON).click()

    def click_save_subscription_button(self):
        self.find_element(*self.SAVE_SUBSCRIPTION_BUTTON).click()

    ##
    # Zarządzanie parametrami produktu
    ##
    def enter_param_key(self, key):
        self.find_element(*self.PARAM_KEY_INPUT).send_keys(key)

    def enter_param_value(self, value):
        self.find_element(*self.PARAM_VALUE_INPUT).send_keys(value)

    def enter_param_account_number(self, number):
        self.find_element(*self.PARAM_ACCOUNT_NUMBER_INPUT).send_keys(number)

    def enter_param_account_owner(self, owner):
        select = Select(self.find_element(*self.PARAM_ACCOUNT_OWNER_INPUT))
        select.select_by_visible_text(owner)

    def click_param_payee_data_from_partner(self):
        self.find_element(*self.PARAM_PAYEE_DATA_FROM_PARTNER_INPUT).click()

    def click_add_transfer_data_button(self):
        self.find_element(*self.ADD_TRANSFER_DATA_BUTTON).click()

    def enter_param_mask(self, mask):
        self.find_element(*self.PARAM_MASK_INPUT).send_keys(mask)

    def enter_param_mask_owner(self, owner):
        select = Select(self.find_element(*self.PARAM_MASK_OWNER_INPUT))
        select.select_by_visible_text(owner)

    def click_add_mask_button(self):
        self.find_element(*self.ADD_MASK_BUTTON).click()

    # DYSPOZYCJE EDYCJA
    def return_orders_table(self):
        orders = []
        table = self.driver.find_elements(By.XPATH, "//table[@id='productList']/tbody/tr")
        i = 0
        for tr in table:
            order = [i]
            td = tr.find_elements(By.TAG_NAME, 'td')
            for cell in td:
                order.append(cell.text)
            orders.append(order)
            i = i + 1

        return orders

    def enter_operation_status(self, status):
        select = Select(self.find_element(*self.OPERATION_ORDER_STATUS_INPUT))
        select.select_by_visible_text(status)

    def click_submit_button(self):
        self.find_element(*self.SUBMIT_BUTTON).click()
