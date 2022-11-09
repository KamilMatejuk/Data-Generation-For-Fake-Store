CATEGORIES = ['Food', 'Fruit', 'Vegetable', 'Electronics', 'AGD', 'Clothes']

TABLE_FIELDS = {
    'Customer': ['customer_id', 'mail', 'name', 'surname', 'date_of_birth', 'description'],
    'Address': ['address_id', 'country', 'city', 'state', 'street', 'street_number', 'apartment_number', 'postal_code', 'fk_customer'],
    'Photo': ['photo_id', 'name', 'file_name', 'upload_date', 'file_extension', 'fk_offer'],
    'Category': ['category_id', 'name','description','fk_category'],
    'Offer': ['offer_id', 'name', 'description', 'price', 'offer_date', 'quantity', 'fk_customer', 'fk_category'],
    'Purchase': ['purchase_id', 'quantity', 'additional_info', 'rating', 'purchase_date', 'fk_offer', 'fk_customer'],
    'Delivery': ['delivery_id', 'expected_arrival', 'delivery_type', 'status', 'sent_date', 'fk_address', 'fk_purchase'],
}