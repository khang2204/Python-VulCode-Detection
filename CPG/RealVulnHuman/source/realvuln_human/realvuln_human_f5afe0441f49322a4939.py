def decrypt_bank_acct_num(request, user_id):  # pylint: disable=unused-argument
    form = request.POST
    if not form:
        return HttpResponse("No form")

    account_num = request.POST['account_number']
    curr_user = utils.current_user(request)
    response = HttpResponse()
    try:
        pay = Pay.objects.get(
            user=curr_user, bank_account_num=account_num
        )
        decrypted_account_num = pay.decrypt_bank_num()
        response['success'] = True
        response.content = decrypted_account_num
        return response
    except Pay.DoesNotExist:
        response['success'] = False
        return response
