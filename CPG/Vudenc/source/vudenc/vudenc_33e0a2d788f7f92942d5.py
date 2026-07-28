from django.conf.urls import include, url
from pretix.control.views import attendees, auth, dashboards, event, help, item, main, orders, organizer, user, vouchers
urlpatterns = [url('^logout$', auth.logout, name='auth.logout'), url(
    '^login$', auth.login, name='auth.login'), url('^register$', auth.
    register, name='auth.register'), url('^forgot$', auth.Forgot.as_view(),
    name='auth.forgot'), url('^forgot/recover$', auth.Recover.as_view(),
    name='auth.forgot.recover'), url('^$', dashboards.user_index, name=
    'index'), url('^settings$', user.UserSettings.as_view(), name=
    'user.settings'), url('^organizers/$', organizer.OrganizerList.as_view(
    ), name='organizers'), url('^organizers/add$', organizer.
    OrganizerCreate.as_view(), name='organizers.add'), url(
    '^organizer/(?P<organizer>[^/]+)/edit$', organizer.OrganizerUpdate.
    as_view(), name='organizer.edit'), url('^events/$', main.EventList.
    as_view(), name='events'), url('^events/add$', main.EventCreateStart.
    as_view(), name='events.add'), url('^event/(?P<organizer>[^/]+)/add',
    main.EventCreate.as_view(), name='events.create'), url(
    '^event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/', include([url('^$',
    dashboards.event_index, name='event.index'), url('^live/$', event.
    EventLive.as_view(), name='event.live'), url('^settings/$', event.
    EventUpdate.as_view(), name='event.settings'), url('^settings/plugins$',
    event.EventPlugins.as_view(), name='event.settings.plugins'), url(
    '^settings/permissions$', event.EventPermissions.as_view(), name=
    'event.settings.permissions'), url('^settings/payment$', event.
    PaymentSettings.as_view(), name='event.settings.payment'), url(
    '^settings/tickets$', event.TicketSettings.as_view(), name=
    'event.settings.tickets'), url('^settings/email$', event.MailSettings.
    as_view(), name='event.settings.mail'), url('^settings/invoice$', event
    .InvoiceSettings.as_view(), name='event.settings.invoice'), url(
    '^settings/display', event.DisplaySettings.as_view(), name=
    'event.settings.display'), url('^items/$', item.ItemList.as_view(),
    name='event.items'), url('^items/add$', item.ItemCreate.as_view(), name
    ='event.items.add'), url('^items/(?P<item>\\d+)/$', item.
    ItemUpdateGeneral.as_view(), name='event.item'), url(
    '^items/(?P<item>\\d+)/variations$', item.ItemVariations.as_view(),
    name='event.item.variations'), url('^items/(?P<item>\\d+)/up$', item.
    item_move_up, name='event.items.up'), url('^items/(?P<item>\\d+)/down$',
    item.item_move_down, name='event.items.down'), url(
    '^items/(?P<item>\\d+)/delete$', item.ItemDelete.as_view(), name=
    'event.items.delete'), url('^categories/$', item.CategoryList.as_view(),
    name='event.items.categories'), url(
    '^categories/(?P<category>\\d+)/delete$', item.CategoryDelete.as_view(),
    name='event.items.categories.delete'), url(
    '^categories/(?P<category>\\d+)/up$', item.category_move_up, name=
    'event.items.categories.up'), url(
    '^categories/(?P<category>\\d+)/down$', item.category_move_down, name=
    'event.items.categories.down'), url('^categories/(?P<category>\\d+)/$',
    item.CategoryUpdate.as_view(), name='event.items.categories.edit'), url
    ('^categories/add$', item.CategoryCreate.as_view(), name=
    'event.items.categories.add'), url('^questions/$', item.QuestionList.
    as_view(), name='event.items.questions'), url(
    '^questions/(?P<question>\\d+)/delete$', item.QuestionDelete.as_view(),
    name='event.items.questions.delete'), url(
    '^questions/(?P<question>\\d+)/up$', item.question_move_up, name=
    'event.items.questions.up'), url('^questions/(?P<question>\\d+)/down$',
    item.question_move_down, name='event.items.questions.down'), url(
    '^questions/(?P<question>\\d+)/$', item.QuestionUpdate.as_view(), name=
    'event.items.questions.edit'), url('^questions/add$', item.
    QuestionCreate.as_view(), name='event.items.questions.add'), url(
    '^quotas/$', item.QuotaList.as_view(), name='event.items.quotas'), url(
    '^quotas/(?P<quota>\\d+)/$', item.QuotaUpdate.as_view(), name=
    'event.items.quotas.edit'), url('^quotas/(?P<quota>\\d+)/delete$', item
    .QuotaDelete.as_view(), name='event.items.quotas.delete'), url(
    '^quotas/add$', item.QuotaCreate.as_view(), name=
    'event.items.quotas.add'), url('^vouchers/$', vouchers.VoucherList.
    as_view(), name='event.vouchers'), url('^vouchers/tags/$', vouchers.
    VoucherTags.as_view(), name='event.vouchers.tags'), url(
    '^vouchers/(?P<voucher>\\d+)/$', vouchers.VoucherUpdate.as_view(), name
    ='event.voucher'), url('^vouchers/(?P<voucher>\\d+)/delete$', vouchers.
    VoucherDelete.as_view(), name='event.voucher.delete'), url(
    '^vouchers/add$', vouchers.VoucherCreate.as_view(), name=
    'event.vouchers.add'), url('^vouchers/bulk_add$', vouchers.
    VoucherBulkCreate.as_view(), name='event.vouchers.bulk'), url(
    '^orders/(?P<code>[0-9A-Z]+)/transition$', orders.OrderTransition.
    as_view(), name='event.order.transition'), url(
    '^orders/(?P<code>[0-9A-Z]+)/resend$', orders.OrderResendLink.as_view(),
    name='event.order.resendlink'), url(
    '^orders/(?P<code>[0-9A-Z]+)/invoice$', orders.OrderInvoiceCreate.
    as_view(), name='event.order.geninvoice'), url(
    '^orders/(?P<code>[0-9A-Z]+)/invoices/(?P<id>\\d+)/regenerate$', orders
    .OrderInvoiceRegenerate.as_view(), name='event.order.regeninvoice'),
    url('^orders/(?P<code>[0-9A-Z]+)/invoices/(?P<id>\\d+)/reissue$',
    orders.OrderInvoiceReissue.as_view(), name='event.order.reissueinvoice'
    ), url('^orders/(?P<code>[0-9A-Z]+)/extend$', orders.OrderExtend.
    as_view(), name='event.order.extend'), url(
    '^orders/(?P<code>[0-9A-Z]+)/comment$', orders.OrderComment.as_view(),
    name='event.order.comment'), url('^orders/(?P<code>[0-9A-Z]+)/$',
    orders.OrderDetail.as_view(), name='event.order'), url(
    '^orders/(?P<code>[0-9A-Z]+)/download/(?P<output>[^/]+)$', orders.
    OrderDownload.as_view(), name='event.order.download'), url(
    '^invoice/(?P<invoice>[^/]+)$', orders.InvoiceDownload.as_view(), name=
    'event.invoice.download'), url('^orders/overview/$', orders.OverView.
    as_view(), name='event.orders.overview'), url('^orders/export/$',
    orders.ExportView.as_view(), name='event.orders.export'), url(
    '^orders/go$', orders.OrderGo.as_view(), name='event.orders.go'), url(
    '^orders/$', orders.OrderList.as_view(), name='event.orders'), url(
    '^attendees/$', attendees.AttendeeList.as_view(), name=
    'event.attendees')])), url('^help/(?P<topic>[^.]+)$', help.HelpView.
    as_view(), name='help')]
