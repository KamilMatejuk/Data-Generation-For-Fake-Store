
CATEGORIES = ['Food', 'Fruit', 'Vegetable', 'Electronics', 'AGD', 'Clothes']

TABLE_FIELDS = {
    'Customer': ['mail', 'name', 'surname', 'date_of_birth', 'description'],
    'Address': ['country', 'city', 'state', 'street', 'street_number', 'apartment_number', 'postal_code', 'fk_customer'],
    'Photo': ['name', 'file_name', 'upload_date', 'file_extension', 'fk_offer'],
    'Category': ['name','description','fk_category'],
    'Offer': ['name', 'description', 'price', 'offer_date', 'quantity', 'fk_customer', 'fk_category'],
    'Purchase': ['quantity', 'additional_info', 'rating', 'purchase_date', 'fk_offer', 'fk_customer'],
    'Delivery': ['expected_arrival', 'delivery_type', 'status', 'sent_date', 'fk_address', 'fk_purchase'],
}