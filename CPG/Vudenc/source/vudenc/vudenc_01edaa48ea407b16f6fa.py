@login_required...
columnlist = ['extracted_text_id', 'id', 'raw_cas', 'raw_chem_name',
    'raw_min_comp', 'raw_central_comp', 'raw_max_comp', 'unit_type__title']
dg = DataGroup.objects.get(pk=pk)
et = ExtractedText.objects.filter(data_document__data_group=dg).first()
if et:
dg_name = dg.get_name_as_slug()
qs = ExtractedChemical.objects.filter(extracted_text__data_document__id=pk
    ).values(*columnlist)
qs = ExtractedChemical.objects.filter(
    extracted_text__data_document__data_group_id=pk).values(*columnlist)
return render_to_csv_response(qs, filename='raw_extracted_records.csv',
    use_verbose_names=False)
return render_to_csv_response(qs, filename=dg_name +
    '_raw_extracted_records.csv', field_header_map={'id':
    'ExtractedChemical_id'}, use_verbose_names=False)
