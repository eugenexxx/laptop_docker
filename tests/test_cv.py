def test_cv(app):
    # Open homepage shop.by in browser, maximize window
    app.session.open_homepage()

    # app.steps.go_to_form()
    app.steps.go_to_form()
    app.steps.fill_in_form_send_cv()
    app.steps.submit_button()