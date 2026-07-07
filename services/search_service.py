from database.database import get_connection


def create_search(user_id, brand, model, max_price, max_km):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO searches
        (user_id, brand, model, max_price, max_km)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        brand,
        model,
        max_price,
        max_km
    ))

    conn.commit()
    conn.close()