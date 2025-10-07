
import json
from sqlalchemy.orm import Session
from backend import crud, schemas
from backend.database import SessionLocal
from backend.models import Product, Category

def seed_data():
    db: Session = SessionLocal()
    
    # Read data from the JSON file
    with open('public/data.json', 'r') as f:
        data = json.load(f)
    
    # Seed Products
    products_data = data.get("products", [])
    db.query(Product).delete()
    for product_data in products_data:
        images_src_list = [img['src'] for img in product_data.get('images', []) if 'src' in img]
        product_data['images'] = images_src_list
        product_schema = schemas.Product(**product_data)
        crud.create_product(db=db, product=product_schema)

    # Seed Categories
    categories_data = data.get("categories", [])
    db.query(Category).delete()
    for i, category_data in enumerate(categories_data):
        # Add a unique ID to the category data
        category_data['id'] = f"cat{i+1}"
        category_schema = schemas.Category(**category_data)
        crud.create_category(db=db, category=category_schema)
        
    db.close()
    print("Database has been seeded successfully with products and categories!")

if __name__ == "__main__":
    seed_data()
