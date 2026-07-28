def _update_counter_subscription(self, event, partner,...
event_cat = str(event.event_type_id.name).lower()
ai_monthly = http.request.env['fit.subscription'].sudo().search([(
    'subscription_type', '=', 'ai_montly'), ('subscription_partner', '=',
    partner.id)])
cf_monthly = http.request.env['fit.subscription'].sudo().search([(
    'subscription_type', '=', 'cf_montly'), ('subscription_partner', '=',
    partner.id)])
bc_monthly = http.request.env['fit.subscription'].sudo().search([(
    'subscription_type', '=', 'bc_montly'), ('subscription_partner', '=',
    partner.id)])
bc_tickets = http.request.env['fit.subscription'].sudo().search([(
    'subscription_type', '=', 'bc_tickets'), ('subscription_partner', '=',
    partner.id)])
bz_tickets = http.request.env['fit.subscription'].sudo().search([(
    'subscription_type', '=', 'bz_tickets'), ('subscription_partner', '=',
    partner.id)])
if ai_monthly.subscription_is_active:
return
if event_cat == 'bokszaktraining':
if bz_tickets:
if event_cat == 'bootcamp':
bz_tickets.subscription_counter += subscription_update_counter
if bc_monthly and bc_monthly.subscription_is_active:
return
if cf_monthly and cf_monthly.subscription_is_active:
return
if bc_tickets:
bc_tickets.subscription_counter += subscription_update_counter
