from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.page import Page


class PollPage(Page):
    SAME_PERSON_YES_INPUT = (By.ID, "samePerson0")
    SAME_PERSON_NOT_INPUT = (By.ID, "samePerson1")
    NEXT_BUTTON = (By.NAME, "_eventId_next")

    INSURER_PROTECTIVE_TYPE_1_INPUT = (By.ID, "insurerProtectiveType0")
    INSURER_PROTECTIVE_TYPE_2_INPUT = (By.ID, "insurerProtectiveType1")
    INSURER_NATIONALITY_INPUT = (By.ID, "insurerNationality")
    INSURER_PESEL_INPUT = (By.ID, "insurerPesel")
    INSURER_LAST_NAME_INPUT = (By.ID, "insurerLastName")
    INSURER_BIRTH_DATE_INPUT = (By.ID, "insurerBirthDate")
    INSURER_PASSPORT_NUMBER_INPUT = (By.ID, "insurerPassportNumber")

    INSURED_PROTECTIVE_TYPE_1_INPUT = (By.ID, "insuredProtectiveType0")
    INSURED_PROTECTIVE_TYPE_2_INPUT = (By.ID, "insuredProtectiveType1")
    INSURED_NATIONALITY_INPUT = (By.ID, "insuredNationality")
    INSURED_PESEL_INPUT = (By.ID, "insuredPesel")
    INSURED_LAST_NAME_INPUT = (By.ID, "insuredLastName")
    INSURED_BIRTH_DATE_INPUT = (By.ID, "insuredBirthDate")
    INSURED_PASSPORT_NUMBER_INPUT = (By.ID, "insuredPassportNumber")

    FILL_POLL_BUTTON = (By.NAME, "_eventId_fillPoll")
    EDIT_POLL_BUTTON = (By.NAME, "_eventId_editPoll")
    PRINT_BUTTON = (By.NAME, "_eventId_print")

    FILL_L1_POLL_BUTTON = (By.ID, "l1")
    FILL_L2_POLL_BUTTON = (By.ID, "l2")
    FILL_L3_POLL_BUTTON = (By.ID, "l3")
    FILL_L4_POLL_BUTTON = (By.ID, "l4")
    FILL_L5_POLL_BUTTON = (By.ID, "l5")
    FILL_L6_POLL_BUTTON = (By.ID, "l6")

    POLL_QUESTIONS_FIRST_NAME_INPUT = (By.ID, "imie")
    POLL_QUESTIONS_LAST_NAME_INPUT = (By.ID, "nazwisko")
    POLL_QUESTIONS_NATIONALITY_INPUT = (By.ID, "obywatelstwo")
    POLL_QUESTIONS_PESEL_INPUT = (By.ID, "pesel")
    POLL_QUESTIONS_BIRTH_DATE_INPUT = (By.ID, "data_urodzenia")
    POLL_QUESTIONS_ID_CARD_TYPE_INPUT = (By.ID, "dokument_tozsamosci_rodzaj")
    POLL_QUESTIONS_ID_CARD_NUMBER_INPUT = (By.ID, "dokument_tozsamosci_numer")
    POLL_QUESTIONS_FILL_AGREE_YES_INPUT = (By.ID, "zgoda_ankieta_wypelnia_tak")
    POLL_QUESTIONS_FILL_AGREE_NOT_INPUT = (By.ID, "zgoda_ankieta_wypelnia_nie")
    POLL_QUESTIONS_NOT_FILL_REASON_INPUT = (By.ID, "powod_odmowy_wypelnienia")
    POLL_QUESTIONS_AGREEMENT_1_YES_INPUT = (By.ID, "przekazywanie_danych_tak")
    POLL_QUESTIONS_AGREEMENT_1_NOT_INPUT = (By.ID, "przekazywanie_danych_nie")
    POLL_QUESTIONS_AGREEMENT_2_YES_INPUT = (By.ID, "dostep_internet_tak")
    POLL_QUESTIONS_AGREEMENT_2_NOT_INPUT = (By.ID, "dostep_internet_nie")

    POLL_QUESTIONS_Q2_A1_INPUT = (By.ID, "q2_a1")
    POLL_QUESTIONS_Q2_A2_INPUT = (By.ID, "q2_a2")
    POLL_QUESTIONS_Q2_A3_INPUT = (By.ID, "q2_a3")
    POLL_QUESTIONS_Q3_A1_INPUT = (By.ID, "q3_a1")
    POLL_QUESTIONS_Q3_A2_INPUT = (By.ID, "q3_a2")
    POLL_QUESTIONS_Q3_A3_INPUT = (By.ID, "q3_a3")
    POLL_QUESTIONS_Q4_A1_INPUT = (By.ID, "q4_a1")
    POLL_QUESTIONS_Q4_A2_INPUT = (By.ID, "q4_a2")
    POLL_QUESTIONS_Q4_A3_INPUT = (By.ID, "q4_a3")
    POLL_QUESTIONS_Q4_A4_INPUT = (By.ID, "q4_a4")
    POLL_QUESTIONS_Q4_A5_INPUT = (By.ID, "q4_a5")
    POLL_QUESTIONS_Q4_A6_INPUT = (By.ID, "q4_a6")
    POLL_QUESTIONS_Q4_A7_INPUT = (By.ID, "q4_a7")
    POLL_QUESTIONS_Q4_A8_INPUT = (By.ID, "q4_a8")
    POLL_QUESTIONS_Q4_A9_INPUT = (By.ID, "q4_a9")
    POLL_QUESTIONS_Q5_A1_INPUT = (By.ID, "q5_a1")
    POLL_QUESTIONS_Q5_A2_INPUT = (By.ID, "q5_a2")
    POLL_QUESTIONS_Q5_A3_INPUT = (By.ID, "q5_a3")
    POLL_QUESTIONS_Q5_A4_INPUT = (By.ID, "q5_a4")
    POLL_QUESTIONS_Q5_A5_INPUT = (By.ID, "q5_a5")
    POLL_QUESTIONS_Q5_A6_INPUT = (By.ID, "q5_a6")
    POLL_QUESTIONS_Q5_A7_INPUT = (By.ID, "q5_a7")
    POLL_QUESTIONS_Q6_A1_INPUT = (By.ID, "q6_a1")
    POLL_QUESTIONS_Q10_A1_INPUT = (By.ID, "q10_a1")
    POLL_QUESTIONS_Q10_A2_INPUT = (By.ID, "q10_a2")
    POLL_QUESTIONS_Q10_A3_INPUT = (By.ID, "q10_a3")
    POLL_QUESTIONS_Q10_A4_INPUT = (By.ID, "q10_a4")
    POLL_QUESTIONS_Q11_A1_INPUT = (By.ID, "q11_a1")
    POLL_QUESTIONS_Q11_A2_INPUT = (By.ID, "q11_a2")
    POLL_QUESTIONS_Q11_A3_INPUT = (By.ID, "q11_a3")
    POLL_QUESTIONS_Q11_A4_INPUT = (By.ID, "q11_a4")
    POLL_QUESTIONS_Q11_A5_INPUT = (By.ID, "q11_a5")
    POLL_QUESTIONS_Q11_A6_INPUT = (By.ID, "q11_a6")
    POLL_QUESTIONS_Q12_A1_INPUT = (By.ID, "q12_a1")
    POLL_QUESTIONS_Q13_A1_YES_INPUT = (By.ID, "q13_a1_tak")
    POLL_QUESTIONS_Q13_A1_NOT_INPUT = (By.ID, "q13_a1_nie")
    POLL_QUESTIONS_Q13_A2_YES_INPUT = (By.ID, "q13_a2_tak")
    POLL_QUESTIONS_Q13_A2_NOT_INPUT = (By.ID, "q13_a2_nie")
    POLL_QUESTIONS_Q14_A1_INPUT = (By.ID, "q14_a1")
    POLL_QUESTIONS_Q14_A2_INPUT = (By.ID, "q14_a2")
    POLL_QUESTIONS_Q14_A3_INPUT = (By.ID, "q14_a3")
    POLL_QUESTIONS_Q14_A4_INPUT = (By.ID, "q14_a4")
    POLL_QUESTIONS_Q14_A5_INPUT = (By.ID, "q14_a5")
    POLL_QUESTIONS_Q7_A1_INPUT = (By.ID, "q7_a1")
    POLL_QUESTIONS_Q7_A2_INPUT = (By.ID, "q7_a2")
    POLL_QUESTIONS_Q7_A3_INPUT = (By.ID, "q7_a3")
    POLL_QUESTIONS_Q7_A4_INPUT = (By.ID, "q7_a4")
    POLL_QUESTIONS_Q7_A5_INPUT = (By.ID, "q7_a5")
    POLL_QUESTIONS_Q7_A6_INPUT = (By.ID, "q7_a6")
    POLL_QUESTIONS_Q8_A1_YES_INPUT = (By.ID, "q8_a1_tak")
    POLL_QUESTIONS_Q8_A1_NOT_INPUT = (By.ID, "q8_a1_nie")
    POLL_QUESTIONS_Q8_A1_IDK_INPUT = (By.ID, "q8_a1_nie_wiem")
    POLL_QUESTIONS_Q8_A2_YES_INPUT = (By.ID, "q8_a2_tak")
    POLL_QUESTIONS_Q8_A2_NOT_INPUT = (By.ID, "q8_a2_nie")
    POLL_QUESTIONS_Q8_A2_IDK_INPUT = (By.ID, "q8_a2_nie_wiem")
    POLL_QUESTIONS_Q8_A3_YES_INPUT = (By.ID, "q8_a3_tak")
    POLL_QUESTIONS_Q8_A3_NOT_INPUT = (By.ID, "q8_a3_nie")
    POLL_QUESTIONS_Q8_A3_IDK_INPUT = (By.ID, "q8_a3_nie_wiem")
    POLL_QUESTIONS_Q8_A4_YES_INPUT = (By.ID, "q8_a4_tak")
    POLL_QUESTIONS_Q8_A4_NOT_INPUT = (By.ID, "q8_a4_nie")
    POLL_QUESTIONS_Q8_A4_IDK_INPUT = (By.ID, "q8_a4_nie_wiem")
    POLL_QUESTIONS_Q8_A5_YES_INPUT = (By.ID, "q8_a5_tak")
    POLL_QUESTIONS_Q8_A5_NOT_INPUT = (By.ID, "q8_a5_nie")
    POLL_QUESTIONS_Q8_A5_IDK_INPUT = (By.ID, "q8_a5_nie_wiem")
    POLL_QUESTIONS_Q8_A6_YES_INPUT = (By.ID, "q8_a6_tak")
    POLL_QUESTIONS_Q8_A6_NOT_INPUT = (By.ID, "q8_a6_nie")
    POLL_QUESTIONS_Q8_A6_IDK_INPUT = (By.ID, "q8_a6_nie_wiem")
    POLL_QUESTIONS_Q9_A1_YES_INPUT = (By.ID, "q9_a1_tak")
    POLL_QUESTIONS_Q9_A1_NOT_INPUT = (By.ID, "q9_a1_nie")
    POLL_QUESTIONS_Q9_A1_IDK_INPUT = (By.ID, "q9_a1_nie_pamietam")
    POLL_QUESTIONS_Q9_A2_YES_INVEST_YES_INPUT = (By.ID, "q9_a2_tak_elem_tak")
    POLL_QUESTIONS_Q9_A2_YES_INVEST_NOT_INPUT = (By.ID, "q9_a2_tak_elem_nie")
    POLL_QUESTIONS_Q9_A2_NOT_INPUT = (By.ID, "q9_a2_nie")
    POLL_QUESTIONS_Q9_A2_IDK_INPUT = (By.ID, "q9_a2_nie_pamietam")
    POLL_QUESTIONS_Q9_A3_YES_INVEST_YES_INPUT = (By.ID, "q9_a3_tak_elem_tak")
    POLL_QUESTIONS_Q9_A3_YES_INVEST_NOT_INPUT = (By.ID, "q9_a3_tak_elem_nie")
    POLL_QUESTIONS_Q9_A3_NOT_INPUT = (By.ID, "q9_a3_nie")
    POLL_QUESTIONS_Q9_A3_IDK_INPUT = (By.ID, "q9_a3_nie_pamietam")
    POLL_QUESTIONS_Q9_A4_YES_INVEST_YES_INPUT = (By.ID, "q9_a4_tak_elem_tak")
    POLL_QUESTIONS_Q9_A4_YES_INVEST_NOT_INPUT = (By.ID, "q9_a4_tak_elem_nie")
    POLL_QUESTIONS_Q9_A4_NOT_INPUT = (By.ID, "q9_a4_nie")
    POLL_QUESTIONS_Q9_A4_IDK_INPUT = (By.ID, "q9_a4_nie_pamietam")

    SAVE_BUTTON = (By.NAME, "_eventId_save")
    FINISH_BUTTON = (By.ID, "finish")

    PESEL_INPUT = (By.ID, "pesel")
    BIRTH_DATE_INPUT = (By.ID, "birthDate")
    ID_CARD_NUMBER_INPUT = (By.ID, "passportNo")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    POLICY_NUMBER_INPUT = (By.ID, "formDocumentNo")
    DEFINITION_NAME_INPUT = (By.ID, "pollDefinition")
    PARTNER_NAME_INPUT = (By.ID, "partnerId")
    UNIT_NAME_INPUT = (By.ID, "unitId")
    WORKER_NAME_INPUT = (By.ID, "workerId")

    SEARCH_BUTTON = (By.NAME, '_eventId_search')
    CLEAR_BUTTON = (By.PARTIAL_LINK_TEXT, 'Wyczyść')

    PRINT_POLL_BUTTON = (By.NAME, '_eventId_printPoll')
    PRINT_RECOMENDATION_BUTTON = (By.NAME, '_eventId_printPollRecommendation')
    PRINT_PRODUCTS_DESCRIPTION_BUTTON = (By.NAME, '_eventId_printPollRecommendedProducts')
    BACK_BUTTON = (By.NAME, '_eventId_back')

    POLL_PARTNER_NAME_INPUT = (By.ID, 'partner')
    POLL_NAME_INPUT = (By.ID, 'name')
    POLL_SYMBOL_INPUT = (By.ID, 'symbol')

    EDIT_BUTTON = (By.NAME, '_eventId_edit')
    EXPORT_BUTTON = (By.NAME, '_eventId_export')

    POLL_DEFINITION_NAME_INPUT = (By.ID, 'pollDefinition.name')
    POLL_DEFINITION_SYMBOL_INPUT = (By.ID, 'pollDefinition.symbol')
    POLL_DEFINITION_VERSION_INPUT = (By.ID, 'pollDefinition.versionString')
    POLL_DEFINITION_QUESTIONS_VERSION_INPUT = (By.ID, 'pollDefinition.questionsRevision')
    POLL_DEFINITION_QUESTIONS_DATE_INPUT = (By.ID, 'pollDefinition.questionsRevisionDate')
    POLL_DEFINITION_ACCEPTATION_REQUIRED_INPUT = (By.ID, 'pollDefinition.acceptationRequired')

    MANAGE_FILES_BUTTON = (By.NAME, '_eventId_manageFiles')

    POLL_DEFINITION_FORM_FILE_INPUT = (By.ID, 'pollDefinition.form')
    POLL_DEFINITION_FORM_DEFINITION_FILE_INPUT = (By.ID, 'pollDefinition.formDefinition')
    POLL_DEFINITION_PRINT_FILE_INPUT = (By.ID, 'pollDefinition.printForm')
    POLL_DEFINITION_BI_PRINT_FILE_INPUT = (By.ID, 'pollDefinition.biPrintForm')
    POLL_DEFINITION_PRINT_RECOMMENDATION_FILE_INPUT = (By.ID, 'pollDefinition.printRecommendation')
    POLL_DEFINITION_BI_PRINT_RECOMMENDATION_FILE_INPUT = (By.ID, 'pollDefinition.biPrintRecommendation')
    POLL_DEFINITION_PRINT_PRODUCTS_DESCRIPTION_FILE_INPUT = (By.ID, 'pollDefinition.printRecommendedProducts')
    POLL_DEFINITION_BI_PRINT_PRODUCTS_DESCRIPTION_FILE_INPUT = (By.ID, 'pollDefinition.biPrintRecommendedProducts')

    POLL_DEFINITION_FORM_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.formProtectiveType')
    POLL_DEFINITION_FORM_DEFINITION_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.formDefinitionProtectiveType')
    POLL_DEFINITION_PRINT_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.printFormProtectiveType')
    POLL_DEFINITION_BI_PRINT_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.biPrintFormProtectiveType')
    POLL_DEFINITION_PRINT_RECOMMENDATION_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.printRecommendationProtectiveType')
    POLL_DEFINITION_BI_PRINT_RECOMMENDATION_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.biPrintRecommendationProtectiveType')
    POLL_DEFINITION_PRINT_PRODUCTS_DESCRIPTION_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.printRecommendedProductsProtectiveType')
    POLL_DEFINITION_BI_PRINT_PRODUCTS_DESCRIPTION_PROTECTIVE_FILE_INPUT = (By.ID, 'pollDefinition.biPrintRecommendedProductsProtectiveType')

    CANCEL_BUTTON = (By.NAME, '_eventId_cancel')

    FILE_PATH_INPUT = (By.NAME, 'file')
    ADD_FILE_BUTTON = (By.NAME, '_eventId_add')

    SUBMIT_BUTTON = (By.NAME, '_eventId_submit')

    ##
    # ANKIETA I WNIOSEK
    ##
    
    # CZY UBEZPIECZAJĄCY I UBEZPIECZONY TO TA SAMA OSOBA
    def click_same_person_yes(self):
        self.find_element(*self.SAME_PERSON_YES_INPUT).click()

    def click_same_person_not(self):
        self.find_element(*self.SAME_PERSON_NOT_INPUT).click()

    def click_next(self):
        self.find_element(*self.NEXT_BUTTON).click()

    # DANE UBEZPIECZAJĄCEGO
    def click_insurer_protective_type_1(self):
        self.find_element(*self.INSURER_PROTECTIVE_TYPE_1_INPUT).click()

    def click_insurer_protective_type_2(self):
        self.find_element(*self.INSURER_PROTECTIVE_TYPE_2_INPUT).click()

    def enter_insurer_nationality(self, nationality):
        select = Select(self.find_element(*self.INSURER_NATIONALITY_INPUT))
        select.select_by_visible_text(nationality)

    def enter_insurer_last_name(self, last_name):
        self.find_element(*self.INSURER_LAST_NAME_INPUT).send_keys(last_name)

    def enter_insurer_birth_date(self, date):
        self.find_element(*self.INSURER_BIRTH_DATE_INPUT).send_keys(date)

    def enter_insurer_pesel(self, pesel):
        self.find_element(*self.INSURER_PESEL_INPUT).send_keys(pesel)

    # DANE UBEZPIECZONEGO
    def click_insured_protective_type_1(self):
        self.find_element(*self.INSURED_PROTECTIVE_TYPE_1_INPUT).click()

    def click_insured_protective_type_2(self):
        self.find_element(*self.INSURED_PROTECTIVE_TYPE_2_INPUT).click()

    def enter_insured_nationality(self, nationality):
        select = Select(self.find_element(*self.INSURED_NATIONALITY_INPUT))
        select.select_by_visible_text(nationality)

    def enter_insured_last_name(self, last_name):
        self.find_element(*self.INSURED_LAST_NAME_INPUT).send_keys(last_name)

    def enter_insured_birth_date(self, date):
        self.find_element(*self.INSURED_BIRTH_DATE_INPUT).send_keys(date)

    def enter_insured_pesel(self, pesel):
        self.find_element(*self.INSURED_PESEL_INPUT).send_keys(pesel)

    # WYSZUKIWANIE ANKIETY KLIENTA
    def click_fill_poll(self):
        self.find_element(*self.FILL_POLL_BUTTON).click()

    def click_edit_poll(self):
        self.find_element(*self.EDIT_POLL_BUTTON).click()

    def click_print(self):
        self.find_element(*self.PRINT_BUTTON).click()

    # LISTA ANKIET
    def click_fill_l1_poll(self):
        self.find_element(*self.FILL_L1_POLL_BUTTON).click()

    def click_fill_l2_poll(self):
        self.find_element(*self.FILL_L2_POLL_BUTTON).click()

    def click_fill_l3_poll(self):
        self.find_element(*self.FILL_L3_POLL_BUTTON).click()

    def click_fill_l4_poll(self):
        self.find_element(*self.FILL_L4_POLL_BUTTON).click()

    def click_fill_l5_poll(self):
        self.find_element(*self.FILL_L5_POLL_BUTTON).click()

    def click_fill_l6_poll(self):
        self.find_element(*self.FILL_L6_POLL_BUTTON).click()

    ##
    # DANE UBEZPIECZAJĄCEGO / DANE UBEZPIECZONEGO
    ##
    def enter_client_name(self, name):
        self.find_element(*self.POLL_QUESTIONS_FIRST_NAME_INPUT).send_keys(name)

    def enter_client_surname(self, surname):
        self.find_element(*self.POLL_QUESTIONS_LAST_NAME_INPUT).send_keys(surname)

    def enter_client_nationality(self, nationality):
        select = Select(self.find_element(*self.POLL_QUESTIONS_NATIONALITY_INPUT))
        select.select_by_visible_text(nationality)

    def enter_client_pesel(self, pesel):
        self.find_element(*self.POLL_QUESTIONS_PESEL_INPUT).send_keys(pesel)

    def enter_client_birth_date(self, birth_date):
        self.find_element(*self.POLL_QUESTIONS_BIRTH_DATE_INPUT).send_keys(birth_date.strftime("%Y-%m-%d"))

    def enter_client_id_card_type(self, id_card_type):
        select = Select(self.find_element(*self.POLL_QUESTIONS_ID_CARD_TYPE_INPUT))
        select.select_by_visible_text(id_card_type)

    def enter_client_id_card_number(self, id_card_number):
        self.find_element(*self.POLL_QUESTIONS_ID_CARD_NUMBER_INPUT).send_keys(id_card_number)

    def click_client_fill_agree_yes(self):
        self.find_element(*self.POLL_QUESTIONS_FILL_AGREE_YES_INPUT).click()

    def click_client_fill_agree_not(self):
        self.find_element(*self.POLL_QUESTIONS_FILL_AGREE_NOT_INPUT).click()

    def click_client_agreement_1_yes(self):
        self.find_element(*self.POLL_QUESTIONS_AGREEMENT_1_YES_INPUT).click()

    def click_client_agreement_1_not(self):
        self.find_element(*self.POLL_QUESTIONS_AGREEMENT_1_NOT_INPUT).click()

    def click_client_agreement_2_yes(self):
        self.find_element(*self.POLL_QUESTIONS_AGREEMENT_2_YES_INPUT).click()

    def click_client_agreement_2_not(self):
        self.find_element(*self.POLL_QUESTIONS_AGREEMENT_2_NOT_INPUT).click()

    # PYTANIA ANKIETY
    def click_poll_questions_q2_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q2_A1_INPUT).click()

    def click_poll_questions_q2_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q2_A2_INPUT).click()

    def click_poll_questions_q2_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q2_A3_INPUT).click()

    def click_poll_questions_q3_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q3_A1_INPUT).click()

    def click_poll_questions_q3_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q3_A2_INPUT).click()

    def click_poll_questions_q3_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q3_A3_INPUT).click()

    def click_poll_questions_q4_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A1_INPUT).click()

    def click_poll_questions_q4_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A2_INPUT).click()

    def click_poll_questions_q4_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A3_INPUT).click()

    def click_poll_questions_q4_a4(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A4_INPUT).click()

    def click_poll_questions_q4_a5(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A5_INPUT).click()

    def click_poll_questions_q4_a6(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A6_INPUT).click()

    def click_poll_questions_q4_a7(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A7_INPUT).click()

    def click_poll_questions_q4_a8(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A8_INPUT).click()

    def click_poll_questions_q4_a9(self):
        self.find_element(*self.POLL_QUESTIONS_Q4_A9_INPUT).click()

    def click_poll_questions_q5_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A1_INPUT).click()

    def click_poll_questions_q5_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A2_INPUT).click()

    def click_poll_questions_q5_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A3_INPUT).click()

    def click_poll_questions_q5_a4(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A4_INPUT).click()

    def click_poll_questions_q5_a5(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A5_INPUT).click()

    def click_poll_questions_q5_a6(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A6_INPUT).click()

    def click_poll_questions_q5_a7(self):
        self.find_element(*self.POLL_QUESTIONS_Q5_A7_INPUT).click()

    def enter_poll_questions_q6(self, value):
        self.find_element(*self.POLL_QUESTIONS_Q6_A1_INPUT).send_keys(value)

    def click_poll_questions_q10_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q10_A1_INPUT).click()

    def click_poll_questions_q10_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q10_A2_INPUT).click()

    def click_poll_questions_q10_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q10_A3_INPUT).click()

    def click_poll_questions_q10_a4(self):
        self.find_element(*self.POLL_QUESTIONS_Q10_A4_INPUT).click()

    def click_poll_questions_q11_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q11_A1_INPUT).click()

    def click_poll_questions_q11_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q11_A2_INPUT).click()

    def click_poll_questions_q11_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q11_A3_INPUT).click()

    def click_poll_questions_q11_a4(self):
        self.find_element(*self.POLL_QUESTIONS_Q11_A4_INPUT).click()

    def click_poll_questions_q11_a5(self):
        self.find_element(*self.POLL_QUESTIONS_Q11_A5_INPUT).click()

    def click_poll_questions_q11_a6(self):
        self.find_element(*self.POLL_QUESTIONS_Q11_A6_INPUT).click()

    def enter_poll_questions_q12(self, value):
        self.find_element(*self.POLL_QUESTIONS_Q12_A1_INPUT).send_keys(value)

    def click_poll_questions_q13_a1_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q13_A1_YES_INPUT).click()

    def click_poll_questions_q13_a1_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q13_A1_NOT_INPUT).click()

    def click_poll_questions_q13_a2_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q13_A2_YES_INPUT).click()

    def click_poll_questions_q13_a2_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q13_A2_NOT_INPUT).click()

    def click_poll_questions_q14_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q14_A1_INPUT).click()

    def click_poll_questions_q14_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q14_A2_INPUT).click()

    def click_poll_questions_q14_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q14_A3_INPUT).click()

    def click_poll_questions_q14_a4(self):
        self.find_element(*self.POLL_QUESTIONS_Q14_A4_INPUT).click()

    def click_poll_questions_q14_a5(self):
        self.find_element(*self.POLL_QUESTIONS_Q14_A5_INPUT).click()

    def click_poll_questions_q7_a1(self):
        self.find_element(*self.POLL_QUESTIONS_Q7_A1_INPUT).click()

    def click_poll_questions_q7_a2(self):
        self.find_element(*self.POLL_QUESTIONS_Q7_A2_INPUT).click()

    def click_poll_questions_q7_a3(self):
        self.find_element(*self.POLL_QUESTIONS_Q7_A3_INPUT).click()

    def click_poll_questions_q7_a4(self):
        self.find_element(*self.POLL_QUESTIONS_Q7_A4_INPUT).click()

    def click_poll_questions_q7_a5(self):
        self.find_element(*self.POLL_QUESTIONS_Q7_A5_INPUT).click()

    def click_poll_questions_q7_a6(self):
        self.find_element(*self.POLL_QUESTIONS_Q7_A6_INPUT).click()

    def click_poll_questions_q8_a1_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A1_YES_INPUT).click()

    def click_poll_questions_q8_a1_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A1_NOT_INPUT).click()

    def click_poll_questions_q8_a1_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A1_IDK_INPUT).click()

    def click_poll_questions_q8_a2_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A2_YES_INPUT).click()

    def click_poll_questions_q8_a2_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A2_NOT_INPUT).click()

    def click_poll_questions_q8_a2_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A2_IDK_INPUT).click()

    def click_poll_questions_q8_a3_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A3_YES_INPUT).click()

    def click_poll_questions_q8_a3_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A3_NOT_INPUT).click()

    def click_poll_questions_q8_a3_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A3_IDK_INPUT).click()

    def click_poll_questions_q8_a4_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A4_YES_INPUT).click()

    def click_poll_questions_q8_a4_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A4_NOT_INPUT).click()

    def click_poll_questions_q8_a4_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A4_IDK_INPUT).click()

    def click_poll_questions_q8_a5_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A5_YES_INPUT).click()

    def click_poll_questions_q8_a5_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A5_NOT_INPUT).click()

    def click_poll_questions_q8_a5_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A5_IDK_INPUT).click()

    def click_poll_questions_q8_a6_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A6_YES_INPUT).click()

    def click_poll_questions_q8_a6_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A6_NOT_INPUT).click()

    def click_poll_questions_q8_a6_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q8_A6_IDK_INPUT).click()

    def click_poll_questions_q9_a1_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A1_YES_INPUT).click()

    def click_poll_questions_q9_a1_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A1_NOT_INPUT).click()

    def click_poll_questions_q9_a1_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A1_IDK_INPUT).click()

    def click_poll_questions_q9_a2_yes_invest_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A2_YES_INVEST_YES_INPUT).click()

    def click_poll_questions_q9_a2_yes_invest_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A2_YES_INVEST_NOT_INPUT).click()

    def click_poll_questions_q9_a2_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A2_NOT_INPUT).click()

    def click_poll_questions_q9_a2_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A2_IDK_INPUT).click()

    def click_poll_questions_q9_a3_yes_invest_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A3_YES_INVEST_YES_INPUT).click()

    def click_poll_questions_q9_a3_yes_invest_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A3_YES_INVEST_NOT_INPUT).click()

    def click_poll_questions_q9_a3_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A3_NOT_INPUT).click()

    def click_poll_questions_q9_a3_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A3_IDK_INPUT).click()

    def click_poll_questions_q9_a4_yes_invest_yes(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A4_YES_INVEST_YES_INPUT).click()

    def click_poll_questions_q9_a4_yes_invest_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A4_YES_INVEST_NOT_INPUT).click()

    def click_poll_questions_q9_a4_not(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A4_NOT_INPUT).click()

    def click_poll_questions_q9_a4_idk(self):
        self.find_element(*self.POLL_QUESTIONS_Q9_A4_IDK_INPUT).click()

    def click_save(self):
        self.find_element(*self.SAVE_BUTTON).click()

    def click_finish(self):
        self.find_element(*self.FINISH_BUTTON).click()
