@order_items_router.get("/{order_id}")
def get_all_order_items(order_id: int, dbs: Session = Depends(connect_to_db)):
    raw_query = f"""SELECT
    order_items.id,
    foods.food_name,
    foods.price,
    order_items.quantity
        FROM order_items
        JOIN foods
        ON foods.id = order_items.food_id
        WHERE order_items.order_id = {order_id}
        ;"""
    all_items = dbs.execute(text(raw_query))
    result = []
    for id, food_name, price, qty in all_items:
        temp = {"id": id, "food_name": food_name, "price": price, "qty": qty}
        result.append(temp)
    return result

