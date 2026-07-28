def input_mail():...
mail = InputMail()
mail.fdoc = TestDoc({})
mail._chash = '123'
mail.as_dict = lambda : None
return mail
