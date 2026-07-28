def update_sold_statusDONOTUSE():...
sql = """
    DONT DO THIS UNLESS ABSOLUTELT SURE ABOUT QTY BETTER TO DO VIA IMPORT???????
    update set it.workflow_state = 'Sold'

    select it.item_code, bin.actual_qty
    from `tabItem` it
    right join `tabBin` bin
    on bin.item_code = it.item_code

    right join `zEbayListings` el
    on el.sku = it.item_code
    where el.qty =0 and bin.actual_qty =0
    """
