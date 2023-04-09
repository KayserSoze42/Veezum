import time

from Veezum.pages.status_page import StatusPage


def test_goto_url() -> None:
    page = StatusPage()

    page.goto()

    pageURL = page.map.driver.current_url

    assert pageURL == "https://frs.gov.cz/en/ioff/application-status"

def test_getFromInput_id() -> None:

    page = StatusPage()

    page.map.setDriver()

    page.goto()

    formInputID = page.map.getFormInput().get_attribute("id")

    page.map.tearDown()

    assert formInputID == "edit-ioff-zov"

def test_formInput_inner_text() -> None:

    page = StatusPage()

    page.map.setDriver()

    page.goto()

    page.enterID("ABCD123456789")

    time.sleep(2.5)

    formInputText = page.map.getFormInput().get_attribute("value")

    page.map.tearDown()

    assert formInputText == "ABCD123456789"

def test_getSubmitButton_id() -> None:

    page = StatusPage()

    page.map.setDriver()

    page.goto()

    formInputID = page.map.getSubmitButton().get_attribute("id")

    page.map.tearDown()

    assert formInputID == "edit-submit-button"

def test_getResultSpan_warning_className() -> None:

    page = StatusPage()

    page.map.setDriver()

    page.goto()

    page.enterID("ABCD123456789")

    time.sleep(2.5)

    page.submit()

    spanElementClassName = page.map.getResultSpan().get_attribute("class")

    page.map.tearDown()

    assert spanElementClassName == "alert alert-warning"

def test_getResultSpan_not_found_text() -> None:

    page = StatusPage()

    page.map.setDriver()

    page.goto()

    page.enterID("ABCD123456789")

    time.sleep(2.5)

    page.submit()

    spanElementText = page.map.getResultSpan().get_attribute("innerText")

    page.map.tearDown()

    assert spanElementText == "Not found"

def test_getResultID_placeholder_inner_text() -> None:

    page = StatusPage()

    page.map.setDriver()

    page.goto()

    page.enterID("ABCD123456789")

    time.sleep(2.5)

    page.submit()

    placeholderResultID = page.map.getResultID().get_attribute("innerText")

    page.map.tearDown()

    assert placeholderResultID == "ABCD123456789"




