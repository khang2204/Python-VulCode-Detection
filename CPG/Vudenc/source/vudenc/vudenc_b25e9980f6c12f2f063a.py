def load_model_objects():...
user = User.objects.create_user(username='Karyn', password='specialP@55word')
superuser = User.objects.create_superuser(username='SuperKaryn', password=
    'specialP@55word', email='me@epa.gov')
ds = DataSource.objects.create(title='Data Source for Test',
    estimated_records=2, state='AT', priority='HI')
script = Script.objects.create(title='Test Download Script', url=
    'http://www.epa.gov/', qa_begun=False, script_type='DL')
exscript = Script.objects.create(title='Test Extraction Script', url=
    'http://www.epa.gov/', qa_begun=False, script_type='EX')
gt = GroupType.objects.create(title='Composition', code='CO')
dg = DataGroup.objects.create(name='Data Group for Test', description=
    'Testing...', data_source=ds, download_script=script, downloaded_by=
    user, downloaded_at=timezone.now(), group_type=gt, csv=
    'register_records_matching.csv', url='https://www.epa.gov')
dt = DocumentType.objects.create(title='MSDS', code='MS', group_type=gt)
doc = DataDocument.objects.create(title='test document', data_group=dg,
    document_type=dt, filename='example.pdf')
p = Product.objects.create(data_source=ds, upc='Test UPC for ProductToPUC')
puc = PUC.objects.create(gen_cat='Test General Category', prod_fam=
    'Test Product Family', prod_type='Test Product Type', description=
    'Test Product Description', last_edited_by=user, kind='FO')
extext = ExtractedText.objects.create(prod_name=
    'Test Extracted Text Record', data_document=doc, extraction_script=exscript
    )
ut = UnitType.objects.create(title='percent composition')
wft = WeightFractionType.objects.create(title='reported', description=
    'reported')
ec = ExtractedChemical.objects.create(extracted_text=extext, unit_type=ut,
    weight_fraction_type=wft, raw_chem_name='Test Chem Name', raw_cas=
    'test_cas')
rc = ec.rawchem_ptr
ing = Ingredient.objects.create(lower_wf_analysis=0.123456789012345,
    central_wf_analysis=0.2, upper_wf_analysis=1, script=script, rawchem_ptr=rc
    )
pt = PUCTag.objects.create(name='Test PUC Attribute')
pd = ProductDocument.objects.create(product=p, document=doc)
ehp = ExtractedHabitsAndPractices.objects.create(extracted_text=extext,
    product_surveyed='Test Product Surveyed', prevalence='Continuous')
return dotdict({'user': user, 'superuser': superuser, 'ds': ds, 'script':
    script, 'exscript': exscript, 'dg': dg, 'doc': doc, 'p': p, 'puc': puc,
    'extext': extext, 'ut': ut, 'wft': wft, 'rc': rc, 'ec': ec, 'pt': pt,
    'pd': pd, 'ing': ing, 'dt': dt, 'gt': gt, 'ehp': ehp})
