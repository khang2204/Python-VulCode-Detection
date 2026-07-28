@login_required...
columnlist = ['filename', 'title', 'document_type', 'url', 'organization']
dg = DataGroup.objects.filter(pk=pk).first()
if dg:
columnlist.insert(0, 'id')
qs = DataDocument.objects.filter(data_group_id=0).values(*columnlist)
qs = DataDocument.objects.filter(data_group_id=pk).values(*columnlist)
return render_to_csv_response(qs, filename='registered_records.csv',
    use_verbose_names=False)
return render_to_csv_response(qs, filename=dg.get_name_as_slug() +
    '_registered_records.csv', field_header_map={'id': 'DataDocument_id'},
    use_verbose_names=False)
