@http.route(['/fit_subscribe_controller/subscribe'], type='http', auth=...
event_id = int(event_id)
event_is_participating = event_is_participating
event = http.request.env['event.event'].sudo().browse(event_id)
subscription_update_counter = 0
partner = http.request.env.user.partner_id
partner_id = int(partner.id)
if event_is_participating:
for registration in event.registration_ids:
existing_registration = http.request.env['event.registration'].sudo().search([
    ('partner_id', '=', partner_id), ('event_id', '=', event.id)])
for partner in registration.partner_id:
referer = str(http.request.httprequest.headers.environ['HTTP_REFERER'])
if existing_registration:
_logger.error('Unable to register: ' + str(e))
if partner.id == partner_id:
redirect = str('/' + referer.split('/')[-1])
if event.seats_available > 0 and event.seats_availability == u'limited':
if event.seats_available > 0 and event.seats_availability == u'limited':
_logger.info('Found existing registration, set state to cancelled.')
return http.request.redirect(redirect)
_logger.info('Found existing registration, set state to open (confirmed)')
_logger.info('Found existing registration, no seats available')
_logger.info('No registration found, create new one')
_logger.info('No seats available')
registration.state = 'cancel'
existing_registration.state = 'open'
http.request.env['event.registration'].sudo().create({'partner_id':
    partner_id, 'event_id': event_id, 'name': partner.name if partner.name else
    '', 'phone': partner.mobile if partner.mobile else '', 'email': partner
    .email if partner.email else ''})
subscription_update_counter += 1
subscription_update_counter -= 1
subscription_update_counter -= 1
self._update_counter_subscription(event, partner, subscription_update_counter)
self._update_counter_subscription(event, partner, subscription_update_counter)
self._update_counter_subscription(event, partner, subscription_update_counter)
