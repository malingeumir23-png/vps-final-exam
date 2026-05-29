from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

from database import engine, Base, get_db
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


ANALYTICS_DB = "postgresql://ecommerce_user:CloudComp%232026@localhost:5432/analytics_db"
analytics_engine = create_engine(ANALYTICS_DB)

@app.post("/products")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    db_product = models.Product(
        name=product.name,
        price=product.price
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


@app.get("/products")
def get_products(db: Session = Depends(get_db)):

    return db.query(models.Product).all()


@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):

    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    db_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    return db.query(models.User).all()


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


@app.post("/orders")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):

    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):

    return db.query(models.Order).all()


@app.get("/analytics")
def get_analytics():

    summary = pd.read_sql(
        "SELECT * FROM sales_summary",
        analytics_engine
    )

    top_products = pd.read_sql(
        "SELECT * FROM top_products",
        analytics_engine
    )

    return {
        "total_orders": int(summary["total_orders"][0]),
        "total_revenue": int(summary["total_revenue"][0]),
        "top_product": int(top_products["product_id"][0])
    }

from sqlalchemy import create_engine
import pandas as pd